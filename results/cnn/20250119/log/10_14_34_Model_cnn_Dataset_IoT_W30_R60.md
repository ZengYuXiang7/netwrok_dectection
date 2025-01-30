```python
|2025-01-19 10:14:34| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xcc099a63e30>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': cnn, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 60, 'record': True, 'retrain': False, 'rounds': 5,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-19 10:14:34| ********************Experiment Start********************
|2025-01-19 10:14:35| Acc=0.8977 F1=0.8345 Precision=0.8583 Recall=0.8214 time=222.1 s 
|2025-01-19 10:14:35| Acc=0.9012 F1=0.8352 Precision=0.8539 Recall=0.8298 time=155.3 s 
|2025-01-19 10:14:35| Acc=0.8992 F1=0.8353 Precision=0.8745 Recall=0.8283 time=179.9 s 
|2025-01-19 10:14:36| Acc=0.8673 F1=0.7993 Precision=0.8263 Recall=0.8079 time=130.0 s 
|2025-01-19 10:14:36| Acc=0.8902 F1=0.8224 Precision=0.8421 Recall=0.8132 time=180.7 s 
|2025-01-19 10:14:36| ********************Experiment Results:********************
|2025-01-19 10:14:36| Acc: 0.8911 ± 0.0125
|2025-01-19 10:14:36| F1: 0.8253 ± 0.0139
|2025-01-19 10:14:36| P: 0.8510 ± 0.0161
|2025-01-19 10:14:36| Recall: 0.8201 ± 0.0085
|2025-01-19 10:14:36| train_time: 173.6196 ± 30.5943
|2025-01-19 10:14:36| Flops: 44405760
|2025-01-19 10:14:36| Params: 12621
|2025-01-19 10:14:36| Inference time: 0.12 ms
|2025-01-19 10:14:36| ********************Experiment Success********************
```

