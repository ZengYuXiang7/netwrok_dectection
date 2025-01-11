```python
|2025-01-10 01:04:13| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x7c4779579c40>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 512,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'seq_method': self, 'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-10 01:04:13| ********************Experiment Start********************
|2025-01-10 01:08:21| Round=1 BestEpoch= 72 Acc=0.8406 F1=0.7634 Precision=0.7709 Recall=0.7589 Training_time=154.5 s 

|2025-01-10 01:08:21| ********************Experiment Results:********************
|2025-01-10 01:08:21| Acc: 0.8406 ± 0.0000
|2025-01-10 01:08:21| F1: 0.7634 ± 0.0000
|2025-01-10 01:08:21| P: 0.7709 ± 0.0000
|2025-01-10 01:08:21| Recall: 0.7589 ± 0.0000
|2025-01-10 01:08:21| train_time: 154.5095 ± 0.0000
|2025-01-10 01:08:22| Flops: 2146205696
|2025-01-10 01:08:22| Params: 6718485
|2025-01-10 01:08:22| Inference time: 0.39 ms
|2025-01-10 01:08:22| ********************Experiment Success********************
```

