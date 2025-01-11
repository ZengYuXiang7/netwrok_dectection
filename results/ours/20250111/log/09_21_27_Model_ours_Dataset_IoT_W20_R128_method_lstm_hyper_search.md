```python
|2025-01-11 09:21:27| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7018f1003350>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 6, 'optim': AdamW, 'path': ./datasets/, 'patience': 30,
     'program_test': False, 'rank': 128, 'record': True, 'retrain': True,
     'rounds': 1, 'seed': 0, 'seq_method': lstm, 'time_interval': 10,
     'train_size': 500, 'verbose': 10,
}
|2025-01-11 09:21:27| ********************Experiment Start********************
|2025-01-11 09:27:31| Round=1 BestEpoch=110 Acc=0.9184 F1=0.8771 Precision=0.8767 Recall=0.8780 Training_time=251.6 s 

|2025-01-11 09:27:31| ********************Experiment Results:********************
|2025-01-11 09:27:31| Acc: 0.9184 ± 0.0000
|2025-01-11 09:27:31| F1: 0.8771 ± 0.0000
|2025-01-11 09:27:31| P: 0.8767 ± 0.0000
|2025-01-11 09:27:31| Recall: 0.8780 ± 0.0000
|2025-01-11 09:27:31| train_time: 251.5919 ± 0.0000
|2025-01-11 09:27:32| Flops: 1919815680
|2025-01-11 09:27:32| Params: 1120085
|2025-01-11 09:27:32| Inference time: 0.36 ms
|2025-01-11 09:27:32| ********************Experiment Success********************
```

