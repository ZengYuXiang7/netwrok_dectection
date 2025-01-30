```python
|2025-01-19 16:23:39| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x72279914bf80>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 2, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-19 16:23:39| ********************Experiment Start********************
|2025-01-19 16:31:21| Round=1 BestEpoch= 47 Acc=0.9049 F1=0.8387 Precision=0.8415 Recall=0.8375 Training_time=270.5 s 

|2025-01-19 16:31:21| ********************Experiment Results:********************
|2025-01-19 16:31:21| Acc: 0.9049 ± 0.0000
|2025-01-19 16:31:21| F1: 0.8387 ± 0.0000
|2025-01-19 16:31:21| P: 0.8415 ± 0.0000
|2025-01-19 16:31:21| Recall: 0.8375 ± 0.0000
|2025-01-19 16:31:21| train_time: 270.4950 ± 0.0000
|2025-01-19 16:31:21| Flops: 1440480000
|2025-01-19 16:31:21| Params: 1028775
|2025-01-19 16:31:21| Inference time: 1.72 ms
|2025-01-19 16:31:22| ********************Experiment Success********************
```

