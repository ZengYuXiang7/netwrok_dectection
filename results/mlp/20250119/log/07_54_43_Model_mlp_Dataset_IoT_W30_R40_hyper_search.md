```python
|2025-01-19 07:54:43| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7af508b92d80>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': mlp, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 40, 'record': True, 'retrain': True, 'rounds': 5,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-19 07:54:43| ********************Experiment Start********************
|2025-01-19 07:58:09| Round=1 BestEpoch=283 Acc=0.7900 F1=0.6833 Precision=0.7014 Recall=0.6742 Training_time=148.5 s 

|2025-01-19 08:01:42| Round=2 BestEpoch=299 Acc=0.7978 F1=0.6998 Precision=0.7197 Recall=0.6890 Training_time=152.9 s 

|2025-01-19 08:05:02| Round=3 BestEpoch=277 Acc=0.7800 F1=0.6755 Precision=0.6913 Recall=0.6651 Training_time=143.2 s 

|2025-01-19 08:07:01| Round=4 BestEpoch=151 Acc=0.7731 F1=0.6673 Precision=0.6803 Recall=0.6646 Training_time=77.5 s 

|2025-01-19 08:09:55| Round=5 BestEpoch=236 Acc=0.7867 F1=0.6731 Precision=0.7061 Recall=0.6559 Training_time=121.9 s 

|2025-01-19 08:09:55| ********************Experiment Results:********************
|2025-01-19 08:09:55| Acc: 0.7855 ± 0.0084
|2025-01-19 08:09:55| F1: 0.6798 ± 0.0113
|2025-01-19 08:09:55| P: 0.6998 ± 0.0133
|2025-01-19 08:09:55| Recall: 0.6698 ± 0.0112
|2025-01-19 08:09:55| train_time: 128.8019 ± 27.7653
|2025-01-19 08:09:55| Flops: 517632
|2025-01-19 08:09:55| Params: 3943
|2025-01-19 08:09:55| Inference time: 0.05 ms
|2025-01-19 08:09:56| ********************Experiment Success********************
```

