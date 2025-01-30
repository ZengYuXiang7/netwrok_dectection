```python
|2025-01-18 18:19:26| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x787e80fe3950>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 1, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-18 18:19:26| ********************Experiment Start********************
|2025-01-18 18:22:18| Round=1 BestEpoch=104 Acc=0.8970 F1=0.8313 Precision=0.8367 Recall=0.8277 Training_time=117.3 s 

|2025-01-18 18:22:18| ********************Experiment Results:********************
|2025-01-18 18:22:18| Acc: 0.8970 ± 0.0000
|2025-01-18 18:22:18| F1: 0.8313 ± 0.0000
|2025-01-18 18:22:18| P: 0.8367 ± 0.0000
|2025-01-18 18:22:18| Recall: 0.8277 ± 0.0000
|2025-01-18 18:22:18| train_time: 117.3234 ± 0.0000
|2025-01-18 18:22:18| Flops: 348364800
|2025-01-18 18:22:18| Params: 166725
|2025-01-18 18:22:18| Inference time: 0.25 ms
|2025-01-18 18:22:18| ********************Experiment Success********************
```

