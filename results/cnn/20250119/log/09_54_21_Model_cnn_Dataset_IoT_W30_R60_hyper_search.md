```python
|2025-01-19 09:54:21| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x793fb3a3c320>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': cnn, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 60, 'record': True, 'retrain': True, 'rounds': 5,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-19 09:54:21| ********************Experiment Start********************
|2025-01-19 09:59:23| Round=1 BestEpoch=365 Acc=0.8977 F1=0.8345 Precision=0.8583 Recall=0.8214 Training_time=222.1 s 

|2025-01-19 10:03:02| Round=2 BestEpoch=264 Acc=0.9012 F1=0.8352 Precision=0.8539 Recall=0.8298 Training_time=155.3 s 

|2025-01-19 10:07:12| Round=3 BestEpoch=305 Acc=0.8992 F1=0.8353 Precision=0.8745 Recall=0.8283 Training_time=179.9 s 

|2025-01-19 10:10:19| Round=4 BestEpoch=216 Acc=0.8673 F1=0.7993 Precision=0.8263 Recall=0.8079 Training_time=130.0 s 

|2025-01-19 10:14:30| Round=5 BestEpoch=305 Acc=0.8902 F1=0.8224 Precision=0.8421 Recall=0.8132 Training_time=180.7 s 

|2025-01-19 10:14:30| ********************Experiment Results:********************
|2025-01-19 10:14:30| Acc: 0.8911 ± 0.0125
|2025-01-19 10:14:30| F1: 0.8253 ± 0.0139
|2025-01-19 10:14:30| P: 0.8510 ± 0.0161
|2025-01-19 10:14:30| Recall: 0.8201 ± 0.0085
|2025-01-19 10:14:30| train_time: 173.6196 ± 30.5943
|2025-01-19 10:14:30| Flops: 44405760
|2025-01-19 10:14:30| Params: 12621
|2025-01-19 10:14:30| Inference time: 0.08 ms
|2025-01-19 10:14:32| ********************Experiment Success********************
```

