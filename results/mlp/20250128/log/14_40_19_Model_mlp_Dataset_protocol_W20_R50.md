```python
|2025-01-28 14:40:19| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': protocol, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x11f421ad2570>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': mlp, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 50, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-28 14:40:19| ********************Experiment Start********************
|2025-01-28 14:46:23| Round=1 BestEpoch=113 Ac=0.5972 Pr=0.5858 Rc=0.5055 F1=0.5251 Training_time=12.5 s 

|2025-01-28 14:46:51| Round=2 BestEpoch=104 Ac=0.5936 Pr=0.5690 Rc=0.5112 F1=0.5193 Training_time=11.4 s 

|2025-01-28 14:46:51| ********************Experiment Results:********************
|2025-01-28 14:46:51| AC: 0.5954 ± 0.0018
|2025-01-28 14:46:51| PR: 0.5774 ± 0.0084
|2025-01-28 14:46:51| RC: 0.5084 ± 0.0028
|2025-01-28 14:46:51| F1: 0.5222 ± 0.0029
|2025-01-28 14:46:51| train_time: 11.9811 ± 0.5474
|2025-01-28 14:46:51| Flops: 685824
|2025-01-28 14:46:51| Params: 5231
|2025-01-28 14:46:51| Inference time: 0.06 ms
|2025-01-28 14:46:52| ********************Experiment Success********************
```

