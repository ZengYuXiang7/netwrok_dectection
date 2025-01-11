```python
|2025-01-10 16:17:50| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x7e8e07c4fc80>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 128,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-10 16:17:50| ********************Experiment Start********************
|2025-01-10 16:21:46| Round=1 BestEpoch= 80 Acc=0.9157 F1=0.8677 Precision=0.8738 Recall=0.8640 Training_time=147.7 s 

|2025-01-10 16:21:46| ********************Experiment Results:********************
|2025-01-10 16:21:46| Acc: 0.9157 ± 0.0000
|2025-01-10 16:21:46| F1: 0.8677 ± 0.0000
|2025-01-10 16:21:46| P: 0.8738 ± 0.0000
|2025-01-10 16:21:46| Recall: 0.8640 ± 0.0000
|2025-01-10 16:21:46| train_time: 147.7090 ± 0.0000
|2025-01-10 16:21:46| Flops: 649072640
|2025-01-10 16:21:46| Params: 625877
|2025-01-10 16:21:46| Inference time: 0.39 ms
|2025-01-10 16:21:47| ********************Experiment Success********************
```

