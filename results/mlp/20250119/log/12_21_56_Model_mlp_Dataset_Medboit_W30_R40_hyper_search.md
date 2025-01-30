```python
|2025-01-19 12:21:56| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7c07bdced3a0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': mlp, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 40, 'record': True, 'retrain': True, 'rounds': 5,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-19 12:21:56| ********************Experiment Start********************
|2025-01-19 12:35:45| Round=1 BestEpoch= 81 Acc=0.7011 F1=0.6125 Precision=0.6591 Recall=0.5952 Training_time=21.7 s 

|2025-01-19 12:36:20| Round=2 BestEpoch= 44 Acc=0.7071 F1=0.6574 Precision=0.6673 Recall=0.6529 Training_time=11.8 s 

|2025-01-19 12:37:31| Round=3 BestEpoch=118 Acc=0.7071 F1=0.6443 Precision=0.6724 Recall=0.6235 Training_time=31.3 s 

|2025-01-19 12:38:27| Round=4 BestEpoch= 87 Acc=0.7488 F1=0.6793 Precision=0.6930 Recall=0.6675 Training_time=23.1 s 

|2025-01-19 12:39:03| Round=5 BestEpoch= 47 Acc=0.7249 F1=0.6708 Precision=0.6823 Recall=0.6619 Training_time=12.6 s 

|2025-01-19 12:39:03| ********************Experiment Results:********************
|2025-01-19 12:39:03| Acc: 0.7178 ± 0.0174
|2025-01-19 12:39:03| F1: 0.6529 ± 0.0234
|2025-01-19 12:39:03| P: 0.6748 ± 0.0118
|2025-01-19 12:39:03| Recall: 0.6402 ± 0.0271
|2025-01-19 12:39:03| train_time: 20.1060 ± 7.2733
|2025-01-19 12:39:04| Flops: 444416
|2025-01-19 12:39:04| Params: 3384
|2025-01-19 12:39:04| Inference time: 0.07 ms
|2025-01-19 12:39:05| ********************Experiment Success********************
```

