```python
|2025-01-10 16:12:05| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x7351bb832db0>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 100,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-10 16:12:05| ********************Experiment Start********************
|2025-01-10 16:17:46| Round=1 BestEpoch=129 Acc=0.9201 F1=0.8787 Precision=0.8777 Recall=0.8804 Training_time=239.1 s 

|2025-01-10 16:17:46| ********************Experiment Results:********************
|2025-01-10 16:17:46| Acc: 0.9201 ± 0.0000
|2025-01-10 16:17:46| F1: 0.8787 ± 0.0000
|2025-01-10 16:17:46| P: 0.8777 ± 0.0000
|2025-01-10 16:17:46| Recall: 0.8804 ± 0.0000
|2025-01-10 16:17:46| train_time: 239.0516 ± 0.0000
|2025-01-10 16:17:47| Flops: 398268800
|2025-01-10 16:17:47| Params: 383621
|2025-01-10 16:17:47| Inference time: 0.39 ms
|2025-01-10 16:17:47| ********************Experiment Success********************
```

