```python
|2025-01-30 11:42:15| {
     'ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xbbcfc5d4530>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': cnn, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 64, 'record': True, 'retrain': False, 'rounds': 5,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-30 11:42:15| ********************Experiment Start********************
|2025-01-30 11:43:02| Round=1 BestEpoch=167 Ac=0.9572 Pr=0.6355 Rc=0.5842 F1=0.6013 Training_time=24.4 s 

|2025-01-30 11:43:42| Round=2 BestEpoch=138 Ac=0.9608 Pr=0.6440 Rc=0.5663 F1=0.5960 Training_time=19.9 s 

|2025-01-30 11:44:17| Round=3 BestEpoch=116 Ac=0.9536 Pr=0.4731 Rc=0.4710 F1=0.4718 Training_time=17.3 s 

|2025-01-30 11:44:48| Round=4 BestEpoch= 98 Ac=0.9477 Pr=0.4761 Rc=0.4624 F1=0.4681 Training_time=14.3 s 

|2025-01-30 11:45:30| Round=5 BestEpoch=147 Ac=0.9608 Pr=0.6464 Rc=0.5947 F1=0.6177 Training_time=21.5 s 

|2025-01-30 11:45:30| ********************Experiment Results:********************
|2025-01-30 11:45:30| AC: 0.9560 ± 0.0049
|2025-01-30 11:45:30| PR: 0.5750 ± 0.0821
|2025-01-30 11:45:30| RC: 0.5357 ± 0.0572
|2025-01-30 11:45:30| F1: 0.5510 ± 0.0665
|2025-01-30 11:45:30| train_time: 19.4875 ± 3.4672
|2025-01-30 11:45:30| Flops: 33480704
|2025-01-30 11:45:30| Params: 13254
|2025-01-30 11:45:30| Inference time: 0.08 ms
|2025-01-30 11:45:31| ********************Experiment Success********************
```

