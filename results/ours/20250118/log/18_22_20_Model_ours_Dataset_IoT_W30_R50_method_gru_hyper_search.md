```python
|2025-01-18 18:22:20| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x73b68f7c6cc0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 2, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-18 18:22:20| ********************Experiment Start********************
|2025-01-18 18:25:40| Round=1 BestEpoch= 82 Acc=0.9072 F1=0.8495 Precision=0.8566 Recall=0.8451 Training_time=133.0 s 

|2025-01-18 18:25:40| ********************Experiment Results:********************
|2025-01-18 18:25:40| Acc: 0.9072 ± 0.0000
|2025-01-18 18:25:40| F1: 0.8495 ± 0.0000
|2025-01-18 18:25:40| P: 0.8566 ± 0.0000
|2025-01-18 18:25:40| Recall: 0.8451 ± 0.0000
|2025-01-18 18:25:40| train_time: 132.9846 ± 0.0000
|2025-01-18 18:25:40| Flops: 686284800
|2025-01-18 18:25:40| Params: 253275
|2025-01-18 18:25:40| Inference time: 0.40 ms
|2025-01-18 18:25:41| ********************Experiment Success********************
```

