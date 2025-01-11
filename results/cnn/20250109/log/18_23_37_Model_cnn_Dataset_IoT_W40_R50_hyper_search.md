```python
|2025-01-09 18:23:37| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 40,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x77eb589dc7a0>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': cnn, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 50,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 18:23:37| ********************Experiment Start********************
|2025-01-09 18:27:25| Round=1 BestEpoch=242 Acc=0.8291 F1=0.7135 Precision=0.7757 Recall=0.7019 Training_time=154.0 s 

|2025-01-09 18:27:25| ********************Experiment Results:********************
|2025-01-09 18:27:25| Acc: 0.8291 ± 0.0000
|2025-01-09 18:27:25| F1: 0.7135 ± 0.0000
|2025-01-09 18:27:25| P: 0.7757 ± 0.0000
|2025-01-09 18:27:25| Recall: 0.7019 ± 0.0000
|2025-01-09 18:27:25| train_time: 154.0424 ± 0.0000
|2025-01-09 18:27:26| Flops: 41612800
|2025-01-09 18:27:26| Params: 9021
|2025-01-09 18:27:26| Inference time: 0.10 ms
|2025-01-09 18:27:26| ********************Experiment Success********************
```

