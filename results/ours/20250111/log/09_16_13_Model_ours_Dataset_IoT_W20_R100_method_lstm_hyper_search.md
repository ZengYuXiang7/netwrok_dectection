```python
|2025-01-11 09:16:13| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7297bf6af0b0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 6, 'optim': AdamW, 'path': ./datasets/, 'patience': 30,
     'program_test': False, 'rank': 100, 'record': True, 'retrain': True,
     'rounds': 1, 'seed': 0, 'seq_method': lstm, 'time_interval': 10,
     'train_size': 500, 'verbose': 10,
}
|2025-01-11 09:16:13| ********************Experiment Start********************
|2025-01-11 09:21:23| Round=1 BestEpoch= 89 Acc=0.9188 F1=0.8774 Precision=0.8772 Recall=0.8782 Training_time=204.6 s 

|2025-01-11 09:21:23| ********************Experiment Results:********************
|2025-01-11 09:21:23| Acc: 0.9188 ± 0.0000
|2025-01-11 09:21:23| F1: 0.8774 ± 0.0000
|2025-01-11 09:21:23| P: 0.8772 ± 0.0000
|2025-01-11 09:21:23| Recall: 0.8782 ± 0.0000
|2025-01-11 09:21:23| train_time: 204.5636 ± 0.0000
|2025-01-11 09:21:24| Flops: 1175996800
|2025-01-11 09:21:24| Params: 685721
|2025-01-11 09:21:24| Inference time: 0.37 ms
|2025-01-11 09:21:25| ********************Experiment Success********************
```

