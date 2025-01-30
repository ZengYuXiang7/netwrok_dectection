```python
|2025-01-17 20:56:57| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x70616eae2b70>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 40, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-17 20:56:57| ********************Experiment Start********************
|2025-01-17 21:01:26| Round=1 BestEpoch= 86 Acc=0.9083 F1=0.8494 Precision=0.8542 Recall=0.8470 Training_time=186.0 s 

|2025-01-17 21:01:26| ********************Experiment Results:********************
|2025-01-17 21:01:26| Acc: 0.9083 ± 0.0000
|2025-01-17 21:01:26| F1: 0.8494 ± 0.0000
|2025-01-17 21:01:26| P: 0.8542 ± 0.0000
|2025-01-17 21:01:26| Recall: 0.8470 ± 0.0000
|2025-01-17 21:01:26| train_time: 186.0214 ± 0.0000
|2025-01-17 21:01:26| Flops: 661100800
|2025-01-17 21:01:26| Params: 218629
|2025-01-17 21:01:26| Inference time: 0.55 ms
|2025-01-17 21:01:27| ********************Experiment Success********************
```

