```python
|2025-01-29 23:46:16| {
     'ablation': 0, 'bs': 150, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xb5e03d2c830>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': dapp, 'num_classes': 21,
     'optim': AdamW, 'order': 2, 'path': ./datasets/, 'patience': 30,
     'program_test': False, 'rank': 64, 'record': True, 'retrain': False,
     'rounds': 10, 'seed': 0, 'time_interval': 10, 'train_size': 500,
     'try_exp': -1, 'verbose': 10,
}
|2025-01-29 23:46:16| ********************Experiment Start********************
|2025-01-29 23:46:50| Round=1 BestEpoch=100 Ac=0.8544 Pr=0.5136 Rc=0.4455 F1=0.4567 Training_time=14.8 s 

|2025-01-29 23:47:10| Round=2 BestEpoch= 44 Ac=0.8058 Pr=0.3607 Rc=0.3635 F1=0.3613 Training_time=6.9 s 

|2025-01-29 23:47:55| Round=3 BestEpoch=136 Ac=0.8608 Pr=0.4933 Rc=0.4478 F1=0.4441 Training_time=21.5 s 

|2025-01-29 23:48:52| Round=4 BestEpoch=177 Ac=0.8738 Pr=0.4728 Rc=0.4763 F1=0.4718 Training_time=28.0 s 

|2025-01-29 23:49:12| Round=5 BestEpoch= 43 Ac=0.8188 Pr=0.3915 Rc=0.4045 F1=0.3945 Training_time=6.8 s 

|2025-01-29 23:49:31| Round=6 BestEpoch= 38 Ac=0.6117 Pr=0.3427 Rc=0.3454 F1=0.3140 Training_time=5.9 s 

|2025-01-29 23:50:03| Round=7 BestEpoch= 89 Ac=0.8252 Pr=0.4688 Rc=0.4603 F1=0.4619 Training_time=14.2 s 

|2025-01-29 23:50:44| Round=8 BestEpoch=118 Ac=0.8026 Pr=0.4272 Rc=0.4281 F1=0.4260 Training_time=18.6 s 

|2025-01-29 23:50:56| Round=9 BestEpoch= 10 Ac=0.5696 Pr=0.3126 Rc=0.2795 F1=0.2768 Training_time=1.6 s 

|2025-01-29 23:51:26| Round=10 BestEpoch= 80 Ac=0.8544 Pr=0.3985 Rc=0.4223 F1=0.4089 Training_time=12.9 s 

|2025-01-29 23:51:26| ********************Experiment Results:********************
|2025-01-29 23:51:26| AC: 0.7877 ± 0.1016
|2025-01-29 23:51:26| PR: 0.4182 ± 0.0645
|2025-01-29 23:51:26| RC: 0.4073 ± 0.0578
|2025-01-29 23:51:26| F1: 0.4016 ± 0.0624
|2025-01-29 23:51:26| train_time: 13.1226 ± 7.6802
|2025-01-29 23:51:27| Flops: 113606400
|2025-01-29 23:51:27| Params: 41426
|2025-01-29 23:51:27| Inference time: 0.65 ms
|2025-01-29 23:51:30| ********************Experiment Success********************
```

