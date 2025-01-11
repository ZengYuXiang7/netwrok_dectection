```python
|2025-01-11 06:28:27| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'graph_encoder': gin, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7b874b886cc0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 6, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 64, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'verbose': 10,
}
|2025-01-11 06:28:27| ********************Experiment Start********************
|2025-01-11 06:52:11| Round=1 BestEpoch=231 Acc=0.7906 F1=0.7061 Precision=0.7369 Recall=0.6893 Training_time=1078.3 s 

|2025-01-11 06:52:11| ********************Experiment Results:********************
|2025-01-11 06:52:11| Acc: 0.7906 ± 0.0000
|2025-01-11 06:52:11| F1: 0.7061 ± 0.0000
|2025-01-11 06:52:11| P: 0.7369 ± 0.0000
|2025-01-11 06:52:11| Recall: 0.6893 ± 0.0000
|2025-01-11 06:52:11| train_time: 1078.2579 ± 0.0000
|2025-01-11 06:52:36| Flops: 7372800
|2025-01-11 06:52:36| Params: 31317
|2025-01-11 06:52:36| Inference time: 0.29 ms
|2025-01-11 06:52:36| ********************Experiment Success********************
```

