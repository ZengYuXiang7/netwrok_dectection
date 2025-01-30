```python
|2025-01-19 08:09:59| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7204dcd6a0c0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': mlp, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 50, 'record': True, 'retrain': True, 'rounds': 5,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-19 08:09:59| ********************Experiment Start********************
|2025-01-19 08:11:20| Round=1 BestEpoch= 94 Acc=0.7866 F1=0.6848 Precision=0.7195 Recall=0.6717 Training_time=48.0 s 

|2025-01-19 08:14:28| Round=2 BestEpoch=233 Acc=0.7938 F1=0.6967 Precision=0.7192 Recall=0.6841 Training_time=133.7 s 

|2025-01-19 08:17:27| Round=3 BestEpoch=242 Acc=0.7921 F1=0.6915 Precision=0.7118 Recall=0.6817 Training_time=125.7 s 

|2025-01-19 08:19:39| Round=4 BestEpoch=168 Acc=0.7927 F1=0.6916 Precision=0.7009 Recall=0.6870 Training_time=88.0 s 

|2025-01-19 08:22:55| Round=5 BestEpoch=263 Acc=0.7995 F1=0.6896 Precision=0.7054 Recall=0.6807 Training_time=138.3 s 

|2025-01-19 08:22:55| ********************Experiment Results:********************
|2025-01-19 08:22:55| Acc: 0.7930 ± 0.0041
|2025-01-19 08:22:55| F1: 0.6909 ± 0.0038
|2025-01-19 08:22:55| P: 0.7114 ± 0.0074
|2025-01-19 08:22:55| Recall: 0.6810 ± 0.0051
|2025-01-19 08:22:55| train_time: 106.7320 ± 34.3103
|2025-01-19 08:22:55| Flops: 708352
|2025-01-19 08:22:55| Params: 5413
|2025-01-19 08:22:55| Inference time: 0.05 ms
|2025-01-19 08:22:56| ********************Experiment Success********************
```

