import torch
from functools import partial
import shutil
from dl2050nn.cbs import CancelBatchException, CancelEpochException, CancelTrainException, LR_Find, Recorder
from dl2050nn.optimizers import *
from dl2050nn.log import LoggerCallback
from dl2050nn.etc import *

class Learner():
    def __init__(self, data, model, model_p, pre_p=None, opt=Adam, loss_f=None, metrics=[], cbs=[], device=None, freeze=None,
                 show=True):
        self.data = data
        self.model,self.model_p = model,model_p
        if pre_p:
            self.load(pre_p, update_best=False, show=show)
        self.device = 'cpu' if not torch.cuda.is_available() else torch.device(0) if device is None else torch.device(device)
        if show: print(f'Learner: device={self.device}\nBatch size: {data.bs}')
        self.opt = opt
        self.optf = self.opt(model.parameters())
        self.loss_f = loss_f
        if self.loss_f is not None: self.loss_f = self.loss_f.to(self.device)
        self.metrics = metrics
        self._init_cbs([LoggerCallback]+cbs)
        self.ep, self.train = 0, False
        if freeze is not None:
            model_freeze_layers(model, freeze)
        self.model.to(self.device)
        self.show = show

    @property
    def df_best(self): return self.logger.df_best

    def load(self, model_p, update_best=True, show=True):
        stats = load_model(self.model, model_p, show=show)
        if update_best:
            self.eval()
            self.logger.df_best = pd.DataFrame.from_dict(stats)
            k = 4+len(self.metrics)
            self.logger.best = self.logger.df_best.iloc[0,k]

    def save(self):
        save_model(self.model, self.model_p, self.logger.df_best.to_dict())

    def save_as(self, p):
        save_model(self.model, p, self.logger.df_best.to_dict())
    
    def _init_cbs(self, cbs):
        self.cbs = []
        for cb in cbs:
            cb = cb()
            cb.set_learner(self)
            setattr(self, cb.name, cb)
            self.cbs.append(cb)

    def _remove_cbs(self):
        for cb in self.cbs:
            cb.learner = None
        if hasattr(self, cb.name): delattr(self, cb.name)
        self.cbs.remove(cb)

    def __call__(self, event):
        res = True
        # for cb in sorted(self.cbs, key=lambda x: x._order):
        for cb in self.cbs: res = cb(event) and res
        return res

    def fit(self, eps):
        self.eps, self.loss = eps, torch.tensor(0.)
        try:
            if self('begin_fit'): return
            for ep in range(eps):
                self.ep = ep
                self.epf = ep
                self.train = True
                self.model.train()
                if not self('begin_epoch'): self.all_batches(self.data.dl1)
                self.train = False
                self.model.eval()
                with torch.no_grad(): 
                    if not self('begin_validate'): self.all_batches(self.data.dl2)
                if self('after_epoch'): break
        except CancelTrainException: self('after_cancel_train')
        finally:
            self('after_fit')

    def all_batches(self, dl):
        if not dl: return
        self.iters = len(dl)
        try:
            for self.iter,(x,y) in enumerate(dl):
                if len(x)>2: self.one_batch(x, y)
                # else: print('Skiping batch smaller that 2')
                if self.train: self.epf += 1./self.iters
        except CancelEpochException: self('after_cancel_epoch')

    def one_batch(self, x, y):
        try:
            self.x,self.y = x,y
            if self('begin_batch'): return
            self.x,self.y = x.to(self.device),y.to(self.device)
            self.y2 = self.model(self.x)
            self.y2 = torch.squeeze(self.y2,-1)
            if self('after_pred'): return
            self.loss = self.loss_f(self.y2, self.y)
            if self('after_loss'): return
            if not self.train: return
            self.loss.backward()
            if self('after_backward'): return
            self.optf.step()
            if self('after_step'): return
            self.optf.zero_grad()
        except CancelBatchException: self('after_cancel_batch')
        finally: self('after_batch')

    def lr_find(self, max_iter=100, min_lr=1e-6, max_lr=1e1):
        # Backup all cbs
        self._init_cbs([partial(LR_Find, max_iter=max_iter, min_lr=min_lr, max_lr=max_lr), Recorder])
        self.fit(10)
        # Reset optimizer status

    def eval(self):
        if not self.data.dl2:
            return
        self.model.eval()
        with torch.no_grad(): 
            if not self('begin_validate'): self.all_batches(self.data.dl2)

    def predict(self, x):
        x = self.data.encode(x)
        self.model.eval()
        with torch.no_grad():
            x = x.to(self.device)
            y = self.model(x)
        return y.detach().cpu()

    def close(self):
        self._remove_cbs()
