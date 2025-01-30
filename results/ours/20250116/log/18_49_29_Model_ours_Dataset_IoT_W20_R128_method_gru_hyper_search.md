```python
|2025-01-16 18:49:29| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7a6daae80830>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-16 18:49:29| ********************Experiment Start********************
|2025-01-16 19:17:20| Round=1 BestEpoch=140 Acc=0.9280 F1=0.8925 Precision=0.8937 Recall=0.8918 Training_time=1307.1 s 

|2025-01-16 19:17:20| ********************Experiment Results:********************
|2025-01-16 19:17:20| Acc: 0.9280 ± 0.0000
|2025-01-16 19:17:20| F1: 0.8925 ± 0.0000
|2025-01-16 19:17:20| P: 0.8937 ± 0.0000
|2025-01-16 19:17:20| Recall: 0.8918 ± 0.0000
|2025-01-16 19:17:20| train_time: 1307.1324 ± 0.0000
|2025-01-16 19:17:22| Flops: 7667634176
|2025-01-16 19:17:22| Params: 5651797
|2025-01-16 19:17:22| Inference time: 1.56 ms
|2025-01-16 19:17:23| ********************Experiment Success********************
```

