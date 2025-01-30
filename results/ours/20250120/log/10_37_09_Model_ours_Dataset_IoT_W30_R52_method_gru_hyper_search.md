```python
|2025-01-20 10:37:09| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x766fe9acfbc0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 2, 'num_classes': 21, 'num_layers': 4, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 52,
     'record': True, 'retrain': True, 'rounds': 5, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-20 10:37:09| ********************Experiment Start********************
|2025-01-20 11:02:12| Round=1 BestEpoch=189 Acc=0.9146 F1=0.8602 Precision=0.8693 Recall=0.8574 Training_time=1250.2 s 

|2025-01-20 11:28:15| Round=2 BestEpoch=196 Acc=0.9181 F1=0.8711 Precision=0.8751 Recall=0.8703 Training_time=1306.8 s 

|2025-01-20 11:48:38| Round=3 BestEpoch=147 Acc=0.9226 F1=0.8653 Precision=0.8725 Recall=0.8628 Training_time=979.6 s 

|2025-01-20 12:06:04| Round=4 BestEpoch=121 Acc=0.9100 F1=0.8584 Precision=0.8589 Recall=0.8612 Training_time=807.1 s 

|2025-01-20 12:26:30| Round=5 BestEpoch=147 Acc=0.9166 F1=0.8610 Precision=0.8656 Recall=0.8580 Training_time=982.1 s 

|2025-01-20 12:26:30| ********************Experiment Results:********************
|2025-01-20 12:26:30| Acc: 0.9164 ± 0.0041
|2025-01-20 12:26:30| F1: 0.8632 ± 0.0045
|2025-01-20 12:26:30| P: 0.8683 ± 0.0056
|2025-01-20 12:26:30| Recall: 0.8619 ± 0.0046
|2025-01-20 12:26:30| train_time: 1065.1611 ± 186.2622
|2025-01-20 12:26:31| Flops: 1470782976
|2025-01-20 12:26:31| Params: 1205277
|2025-01-20 12:26:31| Inference time: 2.01 ms
|2025-01-20 12:26:32| ********************Experiment Success********************
```

