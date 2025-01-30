```python
|2025-01-29 22:25:44| {
     'ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x6ef09805730>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': cnn, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 64, 'record': True, 'retrain': False, 'rounds': 5,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-29 22:25:44| ********************Experiment Start********************
|2025-01-29 22:26:17| Round=1 BestEpoch=158 Ac=0.8576 Pr=0.4984 Rc=0.4470 F1=0.4649 Training_time=16.4 s 

|2025-01-29 22:26:43| Round=2 BestEpoch=117 Ac=0.8350 Pr=0.4151 Rc=0.4214 F1=0.4163 Training_time=11.9 s 

|2025-01-29 22:27:07| Round=3 BestEpoch=108 Ac=0.8317 Pr=0.4813 Rc=0.4284 F1=0.4361 Training_time=11.0 s 

|2025-01-29 22:27:29| Round=4 BestEpoch=100 Ac=0.8511 Pr=0.4464 Rc=0.4052 F1=0.4146 Training_time=10.2 s 

|2025-01-29 22:28:08| Round=5 BestEpoch=185 Ac=0.8641 Pr=0.4694 Rc=0.4401 F1=0.4503 Training_time=19.7 s 

|2025-01-29 22:28:08| ********************Experiment Results:********************
|2025-01-29 22:28:08| AC: 0.8479 ± 0.0126
|2025-01-29 22:28:08| PR: 0.4621 ± 0.0290
|2025-01-29 22:28:08| RC: 0.4284 ± 0.0147
|2025-01-29 22:28:08| F1: 0.4364 ± 0.0194
|2025-01-29 22:28:08| train_time: 13.8343 ± 3.6361
|2025-01-29 22:28:08| Flops: 33579008
|2025-01-29 22:28:08| Params: 14034
|2025-01-29 22:28:08| Inference time: 0.08 ms
|2025-01-29 22:28:09| ********************Experiment Success********************
```

