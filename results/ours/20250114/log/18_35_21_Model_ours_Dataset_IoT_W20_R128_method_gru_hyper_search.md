```python
|2025-01-14 18:35:21| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7e2d66f4ab10>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 10,
}
|2025-01-14 18:35:21| ********************Experiment Start********************
|2025-01-14 18:47:11| Round=1 BestEpoch=120 Acc=0.9247 F1=0.8850 Precision=0.8848 Recall=0.8858 Training_time=511.1 s 

|2025-01-14 18:47:11| ********************Experiment Results:********************
|2025-01-14 18:47:11| Acc: 0.9247 ± 0.0000
|2025-01-14 18:47:11| F1: 0.8850 ± 0.0000
|2025-01-14 18:47:11| P: 0.8848 ± 0.0000
|2025-01-14 18:47:11| Recall: 0.8858 ± 0.0000
|2025-01-14 18:47:11| train_time: 511.0785 ± 0.0000
|2025-01-14 18:47:12| Flops: 4383379456
|2025-01-14 18:47:12| Params: 2041813
|2025-01-14 18:47:12| Inference time: 0.55 ms
|2025-01-14 18:47:13| ********************Experiment Success********************
```

