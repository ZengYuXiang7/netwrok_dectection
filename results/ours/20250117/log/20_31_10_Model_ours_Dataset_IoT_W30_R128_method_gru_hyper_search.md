```python
|2025-01-17 20:31:10| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x79480835ecc0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-17 20:31:10| ********************Experiment Start********************
|2025-01-17 20:40:36| Round=1 BestEpoch= 41 Acc=0.9013 F1=0.8366 Precision=0.8425 Recall=0.8344 Training_time=287.6 s 

|2025-01-17 20:40:36| ********************Experiment Results:********************
|2025-01-17 20:40:36| Acc: 0.9013 ± 0.0000
|2025-01-17 20:40:36| F1: 0.8366 ± 0.0000
|2025-01-17 20:40:36| P: 0.8425 ± 0.0000
|2025-01-17 20:40:36| Recall: 0.8344 ± 0.0000
|2025-01-17 20:40:36| train_time: 287.6154 ± 0.0000
|2025-01-17 20:40:36| Flops: 11828105216
|2025-01-17 20:40:36| Params: 7646549
|2025-01-17 20:40:36| Inference time: 1.93 ms
|2025-01-17 20:40:37| ********************Experiment Success********************
```

