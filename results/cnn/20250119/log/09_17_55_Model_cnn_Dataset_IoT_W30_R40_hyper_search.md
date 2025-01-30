```python
|2025-01-19 09:17:55| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x74cc5b1dd1c0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': cnn, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 40, 'record': True, 'retrain': True, 'rounds': 5,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-19 09:17:55| ********************Experiment Start********************
|2025-01-19 09:21:11| Round=1 BestEpoch=244 Acc=0.8630 F1=0.7843 Precision=0.8426 Recall=0.7743 Training_time=137.9 s 

|2025-01-19 09:25:02| Round=2 BestEpoch=290 Acc=0.8810 F1=0.8203 Precision=0.8444 Recall=0.8084 Training_time=166.0 s 

|2025-01-19 09:28:33| Round=3 BestEpoch=260 Acc=0.8679 F1=0.7934 Precision=0.8292 Recall=0.7884 Training_time=148.3 s 

|2025-01-19 09:33:35| Round=4 BestEpoch=378 Acc=0.8716 F1=0.8032 Precision=0.8220 Recall=0.7955 Training_time=219.4 s 

|2025-01-19 09:38:19| Round=5 BestEpoch=347 Acc=0.8604 F1=0.7757 Precision=0.8067 Recall=0.7717 Training_time=206.1 s 

|2025-01-19 09:38:19| ********************Experiment Results:********************
|2025-01-19 09:38:19| Acc: 0.8688 ± 0.0072
|2025-01-19 09:38:19| F1: 0.7954 ± 0.0155
|2025-01-19 09:38:19| P: 0.8290 ± 0.0139
|2025-01-19 09:38:19| Recall: 0.7876 ± 0.0136
|2025-01-19 09:38:19| train_time: 175.5318 ± 31.9818
|2025-01-19 09:38:19| Flops: 20387840
|2025-01-19 09:38:19| Params: 6021
|2025-01-19 09:38:19| Inference time: 0.09 ms
|2025-01-19 09:38:20| ********************Experiment Success********************
```

