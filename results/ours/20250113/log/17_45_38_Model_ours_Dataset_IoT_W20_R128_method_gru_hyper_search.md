```python
|2025-01-13 17:45:38| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x72a1176a8c20>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 16, 'verbose': 10,
}
|2025-01-13 17:45:38| ********************Experiment Start********************
|2025-01-13 17:57:24| Round=1 BestEpoch=105 Acc=0.9048 F1=0.8587 Precision=0.8657 Recall=0.8559 Training_time=498.6 s 

|2025-01-13 17:57:24| ********************Experiment Results:********************
|2025-01-13 17:57:24| Acc: 0.9048 ± 0.0000
|2025-01-13 17:57:24| F1: 0.8587 ± 0.0000
|2025-01-13 17:57:24| P: 0.8657 ± 0.0000
|2025-01-13 17:57:24| Recall: 0.8559 ± 0.0000
|2025-01-13 17:57:24| train_time: 498.5683 ± 0.0000
|2025-01-13 17:57:25| Flops: 4385083392
|2025-01-13 17:57:25| Params: 2042581
|2025-01-13 17:57:25| Inference time: 0.83 ms
|2025-01-13 17:57:25| ********************Experiment Success********************
```

