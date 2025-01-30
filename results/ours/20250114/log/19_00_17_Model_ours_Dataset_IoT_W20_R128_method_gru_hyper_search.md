```python
|2025-01-14 19:00:17| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x742a6787ab10>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 2, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 10,
}
|2025-01-14 19:00:17| ********************Experiment Start********************
|2025-01-14 19:11:02| Round=1 BestEpoch=129 Acc=0.9251 F1=0.8829 Precision=0.8825 Recall=0.8841 Training_time=464.2 s 

|2025-01-14 19:11:02| ********************Experiment Results:********************
|2025-01-14 19:11:02| Acc: 0.9251 ± 0.0000
|2025-01-14 19:11:02| F1: 0.8829 ± 0.0000
|2025-01-14 19:11:02| P: 0.8825 ± 0.0000
|2025-01-14 19:11:02| Recall: 0.8841 ± 0.0000
|2025-01-14 19:11:02| train_time: 464.1665 ± 0.0000
|2025-01-14 19:11:03| Flops: 2937655296
|2025-01-14 19:11:03| Params: 1480789
|2025-01-14 19:11:03| Inference time: 0.41 ms
|2025-01-14 19:11:04| ********************Experiment Success********************
```

