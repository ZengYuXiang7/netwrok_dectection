```python
|2025-01-29 22:19:41| {
     'ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xefc3dda1ee0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': mlp, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 64, 'record': True, 'retrain': False, 'rounds': 5,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-29 22:19:41| ********************Experiment Start********************
|2025-01-29 22:19:50| Round=1 BestEpoch= 23 Ac=0.8447 Pr=0.4895 Rc=0.4403 F1=0.4569 Training_time=2.2 s 

|2025-01-29 22:19:58| Round=2 BestEpoch= 21 Ac=0.7961 Pr=0.4739 Rc=0.4387 F1=0.4525 Training_time=1.9 s 

|2025-01-29 22:20:16| Round=3 BestEpoch= 95 Ac=0.8091 Pr=0.5270 Rc=0.3949 F1=0.4196 Training_time=8.5 s 

|2025-01-29 22:20:24| Round=4 BestEpoch= 23 Ac=0.8317 Pr=0.5357 Rc=0.4281 F1=0.4557 Training_time=2.1 s 

|2025-01-29 22:20:38| Round=5 BestEpoch= 58 Ac=0.7994 Pr=0.4982 Rc=0.4702 F1=0.4808 Training_time=5.2 s 

|2025-01-29 22:20:38| ********************Experiment Results:********************
|2025-01-29 22:20:38| AC: 0.8162 ± 0.0189
|2025-01-29 22:20:38| PR: 0.5048 ± 0.0232
|2025-01-29 22:20:38| RC: 0.4345 ± 0.0242
|2025-01-29 22:20:38| F1: 0.4531 ± 0.0195
|2025-01-29 22:20:38| train_time: 3.9601 ± 2.5643
|2025-01-29 22:20:38| Flops: 910336
|2025-01-29 22:20:38| Params: 6966
|2025-01-29 22:20:38| Inference time: 0.06 ms
|2025-01-29 22:20:39| ********************Experiment Success********************
```

