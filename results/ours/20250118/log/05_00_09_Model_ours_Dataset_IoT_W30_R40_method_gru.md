```python
|2025-01-18 05:00:09| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x90c670aeed0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 2, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 40, 'record': True,
     'retrain': False, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-18 05:00:09| ********************Experiment Start********************
|2025-01-18 05:00:11| Acc=0.8959 F1=0.8328 Precision=0.8398 Recall=0.8278 time=1488.4 s 
|2025-01-18 05:00:11| ********************Experiment Results:********************
|2025-01-18 05:00:11| Acc: 0.8959 ± 0.0000
|2025-01-18 05:00:11| F1: 0.8328 ± 0.0000
|2025-01-18 05:00:11| P: 0.8398 ± 0.0000
|2025-01-18 05:00:11| Recall: 0.8278 ± 0.0000
|2025-01-18 05:00:11| train_time: 1488.3971 ± 0.0000
|2025-01-18 05:00:12| Flops: 753982720
|2025-01-18 05:00:12| Params: 429149
|2025-01-18 05:00:12| Inference time: 4.54 ms
|2025-01-18 05:00:12| ********************Experiment Success********************
```

