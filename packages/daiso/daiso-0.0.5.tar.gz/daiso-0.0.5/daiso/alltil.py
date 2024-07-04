import numpy as np
import random
import yaml
import wandb

#######################| Tracer |#######################
class Tracer(dict):
    def __init__(self, *args):
        for k in args:
            self[k] = 0
        self.count = 0
        self.epoch = 0
        
    def __getattr__(self, name):
        return self[name]
    
    def reset(self):
        for k in self.keys():
            self[k] = 0
        self.count = 0
        self.epoch += 1

    def add(self, **kwargs):
        for k, v in kwargs.items():
            self[k] += v
        self.count += 1

    def toss(self, **kwargs):
        return {self[k]:v/self.count for k, v in self.items()} | {"epoch":self.epoch} | kwargs
        
    def step(self):
        self.count += 1


class LogTracer(Tracer):
    def __init__(self, *args, wandb=None):
        super().__init__(args)
        assert not wandb, "No WandB"
        self.wandb = wandb
    
    def toss(self, **kwargs):
        self.wandb.log({self[k]:v/self.count for k, v in self.items()} | {"epoch":self.epoch} | kwargs)
        
#######################| WandB |#######################     

def set_wandb(yes, metric_map, opts):
    if not yes: return FakeWandb()
    import wandb
    import datetime
    now = datetime.datetime.time()
    if not opts.sweep:
        run = wandb.init(project=opts.project_name, name=opts.codename+now.strftime("-%m-%d-%H-%M"))
    else:
        run = wandb.init()
    wandb.config.update(opts) 
    print("#####|WandB Activated|#####")
    for counter in metric_map.values():
        wandb.define_metric(counter)
        for key, flag in metric_map.items():
            if flag == counter:
                wandb.define_metric(key, step_metric=counter)        

    return run

class FakeWandb():
    def __init__(self):
        print("#####|WandB De-Activated|#####")
    def __call__(self):
        print("FakeWandb")
    def init(self, *opts, **kwopts):
        return None
    def log(self, *opts, **kwopts):
        return None
    def finish(self, *opts, **kwopts):
        return None
    def define_metric(self, *opts, **kwopts):
        pass
    
    
#######################| Seed Everything |#######################
def seed_everything(seed = 42):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed) 
    torch.backends.cudnn.deterministic = False
    torch.backends.cudnn.benchmark = False    


#######################| Yami |#######################
class Config:
    def __init__(self, **entries):
        self.__dict__.update(entries)

def load_config(file_path):
    with open(file_path, 'r') as f:
        data = yaml.safe_load(f)
        return Config(**data)


#######################| Model Tracer |#######################

def trace(model):
    return ModelTracer(model)

class ModelTracer():
    def __init__(self, model):
        self.model = model
        self.params = {n:p for n, p in model.named_parameters()}
        self.keys = list(self.params.keys())
        self.no_grad_keys = [n for n, p in self.params.items() if p.grad is None]
        self.grad_keys = list(set(self.keys) - set(self.no_grad_keys))
        self.grads = {n:p.grad.data.mean() for n, p in self.params.items() if p.grad is not None}
        print(">>> Attributes")
        print(".params: parameters-dict / .keys: params' name-list / .no_grad_keys: no-grad-keys-list / .grad_keys: yes-grad-keys-list / .grads: yes-grad-dict(MEAN)")

    
    def confess(self, mode=None, grad=None): # mode: None, name, grad
        model = self.model
        mode = repr(mode) if type(mode) != str else mode
        if grad is None:
            if "None" is mode:
                return [p for p in model.parameters()]
            if "name" is mode:
                return [n for n, p in model.named_parameters()]
            if "all" is mode:
                return {n:p for n, p in model.named_parameters()}
            if "grad" is mode:
                return {n: p for n, p in ((n, p.grad.data.mean()) for n, p in model.named_parameters() if p.grad is not None)}
        if grad is True:
            if "None" is mode:
                return [p for p in model.parameters() if p.grad is not None]
            if "name" is mode:
                return [n for n, p in ((n, p) for n, p in model.named_parameters() if p.grad is not None)]
            if "all" is mode:
                return {n:p for n, p in ((n, p.grad.data.mean()) for n, p in model.named_parameters() if p.grad is not None)}
            if "grad" is mode:
                return {n: p for n, p in ((n, p.grad.data.mean()) for n, p in model.named_parameters() if p.grad is not None)}
        elif grad is False:
            if "None" is mode:
                return [p for p in model.parameters() if p.grad is None]
            if "name" is mode:
                return [n for n, p in ((n, p) for n, p in model.named_parameters() if p.grad is None)]
            if "all" is mode:
                return {n: p for n, p in ((n, p) for n, p in model.named_parameters() if p.grad is None)}
            if "grad" is mode:
                return {n: p for n, p in ((n, p) for n, p in model.named_parameters() if p.grad is None)}
            
    def search(self, target=None, keyword=None, only_key=True):
        if keyword is None or target is None: return print("Plz pass the keyword: #search(self, target=None, keyword=None)")
        
        if not only_key:
            if isinstance(target, dict): 
                return {key: target[key] for key in target.keys() if keyword in key}
            elif isinstance(target, list):
                if target is self.keys:
                    print("searched from self.param")
                    return {key: self.params[key] for key in target if keyword in key}
                elif target is self.grad_keys:
                    print("searched from self.grads")
                    return {key: self.grads[key] for key in target if keyword in key}
                elif target is self.no_grad_keys:
                    print("searched from self.param")
                    return {key: self.params[key] for key in target if keyword in key}
        else:
            if isinstance(target, dict): 
                return [key for key in target.keys() if keyword in key]
            elif isinstance(target, list):
                return [key for key in target if keyword in key]
    
def show(target):
    if isinstance(target, dict):
        for k, v in target.items():
            print(">Key:", k, "\n>Val:", v)
    elif isinstance(target, list):
        for k in target:
            print(">Key:", k)



#######################| Confess! |#######################

def confess(model, mode=None, grad=None): # mode: None, name, grad
    mode = repr(mode) if type(mode) != str else mode
    if grad is None:
        if "None" is mode:
            return [p for p in model.parameters()]
        if "name" is mode:
            return [n for n, p in model.named_parameters()]
        if "all" is mode:
            return {n:p for n, p in model.named_parameters()}
        if "grad" is mode:
            return {n:p.grad.data.mean() for n, p in model.named_parameters() if p.grad is not None}
    if grad is True:
        if "None" is mode:
            return [p for p in model.parameters() if p.grad is not None]
        if "name" is mode:
            return [n for n, p in model.named_parameters() if p.grad is not None]
        if "all" is mode:
            return {n:p for n, p in model.named_parameters() if p.grad is not None}
        if "grad" is mode:
            return {n:p.grad.data.mean() for n, p in model.named_parameters() if p.grad is not None}
    elif grad is False:
        if "None" is mode:
            return [p for p in model.parameters() if p.grad is None]
        if "name" is mode:
            return [n for n, p in model.named_parameters() if p.grad is None]
        if "all" is mode:
            return {n:p for n, p in model.named_parameters() if p.grad is None}
        if "grad" is mode:
            return {n:p for n, p in model.named_parameters() if p.grad is None}
        
#######################| Taster |#######################

class GradTracer():
    def __init__(self):
        print("###|GradTracer Activated|###")
        self.prev_state = None
        self.now_state = None
    
    def update(self, model, mode="grad", grad=True):
        self.prev_state = self.now_state
        self.now_state = confess(model, mode=mode, grad=grad)
    
    def gradgap(self, model, mode="grad", grad=True):
        if self.prev_state is self.now_state: print("GradTracer: same-grad")
        else: 
            grad_gaps = {name: (self.now_state[name] - self.prev_state[name]).mean() for name in self.prev_state.keys() if self.prev_state[name] != self.now_state[name]}
            print("#########Grad GAP")
            for name, gap in grad_gaps:
                print(f"GradTracer: {str(name)} / {gap}")