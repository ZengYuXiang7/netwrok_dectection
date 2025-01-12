```python
|2025-01-08 20:47:20| {
     'Ablation': 0, 'bs': 256, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 200, 'eval_set': True, 'experiment': False, 'log': <utils.logger.Logger object at 0xf82930f1220>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 6, 'optim': AdamW, 'path': ./datasets/, 'patience': 30,
     'program_test': False, 'rank': 50, 'record': True, 'retrain': False,
     'rounds': 1, 'seed': 0, 'time_interval': 10, 'train_size': 500,
     'verbose': 0,
}
|2025-01-08 20:47:20| ********************Experiment Start********************
|2025-01-08 20:49:14| Round=1 BestEpoch=  1 Acc=0.0425 F1=0.0039 Precision=0.0020 Recall=0.0476 Training_time=3.0 s 

|2025-01-08 20:49:14| ********************Experiment Results:********************
|2025-01-08 20:49:14| Acc: 0.0425 ± 0.0000
|2025-01-08 20:49:14| F1: 0.0039 ± 0.0000
|2025-01-08 20:49:14| P: 0.0020 ± 0.0000
|2025-01-08 20:49:14| Recall: 0.0476 ± 0.0000
|2025-01-08 20:49:14| train_time: 2.9571 ± 0.0000
|2025-01-08 20:49:19| Flops: 97638400
|2025-01-08 20:49:19| Params: 381025
|2025-01-08 20:49:19| Inference time: 0.32 ms
|2025-01-08 20:49:20| ********************Experiment Success********************
```
