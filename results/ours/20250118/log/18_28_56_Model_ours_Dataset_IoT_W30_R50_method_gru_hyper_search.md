```python
|2025-01-18 18:28:56| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x72358dff3f50>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 4, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-18 18:28:56| ********************Experiment Start********************
|2025-01-18 18:33:18| Round=1 BestEpoch= 61 Acc=0.9059 F1=0.8464 Precision=0.8562 Recall=0.8395 Training_time=164.0 s 

|2025-01-18 18:33:18| ********************Experiment Results:********************
|2025-01-18 18:33:18| Acc: 0.9059 ± 0.0000
|2025-01-18 18:33:18| F1: 0.8464 ± 0.0000
|2025-01-18 18:33:18| P: 0.8562 ± 0.0000
|2025-01-18 18:33:18| Recall: 0.8395 ± 0.0000
|2025-01-18 18:33:18| train_time: 164.0401 ± 0.0000
|2025-01-18 18:33:18| Flops: 1362124800
|2025-01-18 18:33:18| Params: 426375
|2025-01-18 18:33:18| Inference time: 0.67 ms
|2025-01-18 18:33:18| ********************Experiment Success********************
```

