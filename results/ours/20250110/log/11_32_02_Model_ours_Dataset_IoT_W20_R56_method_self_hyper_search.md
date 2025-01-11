```python
|2025-01-10 11:32:02| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x71f2d1606720>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 56,
     'record': True, 'retrain': True, 'rounds': 1, 'seed': 0,
     'seq_method': self, 'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-10 11:32:02| ********************Experiment Start********************
|2025-01-10 11:40:52| Round=1 BestEpoch=218 Acc=0.9055 F1=0.8549 Precision=0.8579 Recall=0.8553 Training_time=404.6 s 

|2025-01-10 11:40:52| ********************Experiment Results:********************
|2025-01-10 11:40:52| Acc: 0.9055 ± 0.0000
|2025-01-10 11:40:52| F1: 0.8549 ± 0.0000
|2025-01-10 11:40:52| P: 0.8579 ± 0.0000
|2025-01-10 11:40:52| Recall: 0.8553 ± 0.0000
|2025-01-10 11:40:52| train_time: 404.6004 ± 0.0000
|2025-01-10 11:40:53| Flops: 27251840
|2025-01-10 11:40:53| Params: 84189
|2025-01-10 11:40:53| Inference time: 0.42 ms
|2025-01-10 11:40:53| ********************Experiment Success********************
```

