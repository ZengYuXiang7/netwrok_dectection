```python
|2025-01-29 20:28:54| {
     'ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 10, 'graph_encoder': gin, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xd2e149d3500>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 2, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 52, 'record': True,
     'retrain': False, 'rounds': 2, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-29 20:28:54| ********************Experiment Start********************
|2025-01-29 20:29:29| Round=1 BestEpoch= 79 Ac=0.8475 Pr=0.5171 Rc=0.5149 F1=0.5064 Training_time=15.6 s 

|2025-01-29 20:30:14| Round=2 BestEpoch=110 Ac=0.8475 Pr=0.6528 Rc=0.5447 F1=0.5730 Training_time=21.0 s 

|2025-01-29 20:30:14| ********************Experiment Results:********************
|2025-01-29 20:30:14| AC: 0.8475 ± 0.0000
|2025-01-29 20:30:14| PR: 0.5849 ± 0.0678
|2025-01-29 20:30:14| RC: 0.5298 ± 0.0149
|2025-01-29 20:30:14| F1: 0.5397 ± 0.0333
|2025-01-29 20:30:14| train_time: 18.3081 ± 2.7333
|2025-01-29 20:30:14| Flops: 2462720
|2025-01-29 20:30:14| Params: 11821
|2025-01-29 20:30:14| Inference time: 0.22 ms
|2025-01-29 20:30:15| ********************Experiment Success********************
```

