```python
|2025-01-10 15:49:37| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x7d92c1e44560>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 40,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-10 15:49:37| ********************Experiment Start********************
|2025-01-10 15:59:17| Round=1 BestEpoch=244 Acc=0.9148 F1=0.8733 Precision=0.8755 Recall=0.8735 Training_time=447.4 s 

|2025-01-10 15:59:17| ********************Experiment Results:********************
|2025-01-10 15:59:17| Acc: 0.9148 ± 0.0000
|2025-01-10 15:59:17| F1: 0.8733 ± 0.0000
|2025-01-10 15:59:17| P: 0.8755 ± 0.0000
|2025-01-10 15:59:17| Recall: 0.8735 ± 0.0000
|2025-01-10 15:59:17| train_time: 447.3959 ± 0.0000
|2025-01-10 15:59:18| Flops: 66105600
|2025-01-10 15:59:18| Params: 63709
|2025-01-10 15:59:18| Inference time: 0.39 ms
|2025-01-10 15:59:18| ********************Experiment Success********************
```

