```python
|2025-01-19 17:31:27| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x785a47068050>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 2, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-19 17:31:27| ********************Experiment Start********************
|2025-01-19 17:33:55| Round=1 BestEpoch= 55 Acc=0.9183 F1=0.8591 Precision=0.8703 Recall=0.8530 Training_time=87.3 s 

|2025-01-19 17:33:55| ********************Experiment Results:********************
|2025-01-19 17:33:55| Acc: 0.9183 ± 0.0000
|2025-01-19 17:33:55| F1: 0.8591 ± 0.0000
|2025-01-19 17:33:55| P: 0.8703 ± 0.0000
|2025-01-19 17:33:55| Recall: 0.8530 ± 0.0000
|2025-01-19 17:33:55| train_time: 87.3301 ± 0.0000
|2025-01-19 17:33:56| Flops: 686284800
|2025-01-19 17:33:56| Params: 253275
|2025-01-19 17:33:56| Inference time: 0.42 ms
|2025-01-19 17:33:56| ********************Experiment Success********************
```

