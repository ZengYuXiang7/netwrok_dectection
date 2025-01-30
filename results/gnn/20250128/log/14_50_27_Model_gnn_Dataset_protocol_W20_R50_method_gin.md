```python
|2025-01-28 14:50:27| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': protocol, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'graph_encoder': gin, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x9ad3a772c00>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 2, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': False, 'rounds': 2, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-28 14:50:27| ********************Experiment Start********************
|2025-01-28 14:50:56| Round=1 BestEpoch= 72 Ac=0.5972 Pr=0.5178 Rc=0.5162 F1=0.5033 Training_time=11.9 s 

|2025-01-28 14:51:13| Round=2 BestEpoch= 24 Ac=0.5618 Pr=0.5192 Rc=0.4600 F1=0.4637 Training_time=4.2 s 

|2025-01-28 14:51:13| ********************Experiment Results:********************
|2025-01-28 14:51:13| AC: 0.5795 ± 0.0177
|2025-01-28 14:51:13| PR: 0.5185 ± 0.0007
|2025-01-28 14:51:13| RC: 0.4881 ± 0.0281
|2025-01-28 14:51:13| F1: 0.4835 ± 0.0198
|2025-01-28 14:51:13| train_time: 8.0549 ± 3.8239
|2025-01-28 14:51:14| Flops: 5248000
|2025-01-28 14:51:14| Params: 29777
|2025-01-28 14:51:14| Inference time: 0.24 ms
|2025-01-28 14:51:14| ********************Experiment Success********************
```

