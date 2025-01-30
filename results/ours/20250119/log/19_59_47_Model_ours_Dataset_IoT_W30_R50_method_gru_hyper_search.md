```python
|2025-01-19 19:59:47| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7040cb0b1160>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 2, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': True, 'rounds': 2, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-19 19:59:47| ********************Experiment Start********************
|2025-01-19 20:05:16| Round=1 BestEpoch=115 Acc=0.9157 F1=0.8583 Precision=0.8602 Recall=0.8579 Training_time=239.3 s 

|2025-01-19 20:13:19| Round=2 BestEpoch=181 Acc=0.9066 F1=0.8495 Precision=0.8557 Recall=0.8451 Training_time=379.7 s 

|2025-01-19 20:13:19| ********************Experiment Results:********************
|2025-01-19 20:13:19| Acc: 0.9112 ± 0.0046
|2025-01-19 20:13:19| F1: 0.8539 ± 0.0044
|2025-01-19 20:13:19| P: 0.8579 ± 0.0023
|2025-01-19 20:13:19| Recall: 0.8515 ± 0.0064
|2025-01-19 20:13:19| train_time: 309.5081 ± 70.1618
|2025-01-19 20:13:19| Flops: 868748800
|2025-01-19 20:13:19| Params: 297975
|2025-01-19 20:13:19| Inference time: 0.70 ms
|2025-01-19 20:13:20| ********************Experiment Success********************
```

