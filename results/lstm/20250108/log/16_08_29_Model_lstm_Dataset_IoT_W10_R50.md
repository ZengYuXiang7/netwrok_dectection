```python
|2025-01-08 16:08:29| {
     'Ablation': 0, 'bs': 256, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 200, 'eval_set': True, 'experiment': False, 'log': <utils.logger.Logger object at 0x720329233fe0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': lstm,
     'num_classes': 6, 'optim': AdamW, 'path': ./datasets/, 'patience': 30,
     'program_test': False, 'rank': 50, 'record': True, 'retrain': False,
     'rounds': 1, 'seed': 0, 'time_interval': 10, 'train_size': 500,
     'verbose': 0,
}
|2025-01-08 16:08:29| ********************Experiment Start********************
|2025-01-08 16:19:29| Round=1 BestEpoch=196 Acc=0.5940 F1=0.5134 Precision=0.5845 Recall=0.4966 Training_time=524.9 s 

|2025-01-08 16:19:29| ********************Experiment Results:********************
|2025-01-08 16:19:29| Acc: 0.5940 ± 0.0000
|2025-01-08 16:19:29| F1: 0.5134 ± 0.0000
|2025-01-08 16:19:29| P: 0.5845 ± 0.0000
|2025-01-08 16:19:29| Recall: 0.4966 ± 0.0000
|2025-01-08 16:19:29| train_time: 524.8520 ± 0.0000
|2025-01-08 16:19:33| Flops: 75942400
|2025-01-08 16:19:33| Params: 295871
|2025-01-08 16:19:33| Inference time: 0.08 ms
|2025-01-08 16:19:33| ********************Experiment Success********************
```

```python
|2025-01-08 16:19:33| {
     'Ablation': 0, 'bs': 256, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 200, 'eval_set': True, 'experiment': False, 'log': <utils.logger.Logger object at 0x7202b83a3ec0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': lstm,
     'num_classes': 6, 'optim': AdamW, 'path': ./datasets/, 'patience': 30,
     'program_test': False, 'rank': 80, 'record': True, 'retrain': False,
     'rounds': 1, 'seed': 0, 'time_interval': 10, 'train_size': 500,
     'verbose': 0,
}
|2025-01-08 16:19:33| ********************Experiment Start********************
|2025-01-08 16:30:43| Round=1 BestEpoch=161 Acc=0.6390 F1=0.5694 Precision=0.6331 Recall=0.5504 Training_time=455.8 s 

|2025-01-08 16:30:43| ********************Experiment Results:********************
|2025-01-08 16:30:43| Acc: 0.6390 ± 0.0000
|2025-01-08 16:30:43| F1: 0.5694 ± 0.0000
|2025-01-08 16:30:43| P: 0.6331 ± 0.0000
|2025-01-08 16:30:43| Recall: 0.5504 ± 0.0000
|2025-01-08 16:30:43| train_time: 455.8027 ± 0.0000
|2025-01-08 16:30:56| Flops: 128880640
|2025-01-08 16:30:56| Params: 502181
|2025-01-08 16:30:56| Inference time: 0.09 ms
|2025-01-08 16:30:59| ********************Experiment Success********************
```

```python
|2025-01-08 16:30:59| {
     'Ablation': 0, 'bs': 256, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 200, 'eval_set': True, 'experiment': False, 'log': <utils.logger.Logger object at 0x7202b7928ce0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': lstm,
     'num_classes': 6, 'optim': AdamW, 'path': ./datasets/, 'patience': 30,
     'program_test': False, 'rank': 100, 'record': True, 'retrain': False,
     'rounds': 1, 'seed': 0, 'time_interval': 10, 'train_size': 500,
     'verbose': 0,
}
|2025-01-08 16:30:59| ********************Experiment Start********************
|2025-01-08 16:46:19| Round=1 BestEpoch=173 Acc=0.6503 F1=0.5847 Precision=0.6373 Recall=0.5722 Training_time=675.2 s 

|2025-01-08 16:46:19| ********************Experiment Results:********************
|2025-01-08 16:46:19| Acc: 0.6503 ± 0.0000
|2025-01-08 16:46:19| F1: 0.5847 ± 0.0000
|2025-01-08 16:46:19| P: 0.6373 ± 0.0000
|2025-01-08 16:46:19| Recall: 0.5722 ± 0.0000
|2025-01-08 16:46:19| train_time: 675.1685 ± 0.0000
|2025-01-08 16:46:23| Flops: 167244800
|2025-01-08 16:46:23| Params: 651721
|2025-01-08 16:46:23| Inference time: 0.10 ms
|2025-01-08 16:46:23| ********************Experiment Success********************
```

```python
|2025-01-08 16:46:23| {
     'Ablation': 0, 'bs': 256, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 200, 'eval_set': True, 'experiment': False, 'log': <utils.logger.Logger object at 0x7202b7929700>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': cnn,
     'num_classes': 6, 'optim': AdamW, 'path': ./datasets/, 'patience': 30,
     'program_test': False, 'rank': 50, 'record': True, 'retrain': False,
     'rounds': 1, 'seed': 0, 'time_interval': 10, 'train_size': 500,
     'verbose': 0,
}
|2025-01-08 16:46:23| ********************Experiment Start********************
|2025-01-08 17:29:56| Round=1 BestEpoch=189 Acc=0.5730 F1=0.4735 Precision=0.5487 Recall=0.4689 Training_time=2261.1 s 

|2025-01-08 17:29:56| ********************Experiment Results:********************
|2025-01-08 17:29:56| Acc: 0.5730 ± 0.0000
|2025-01-08 17:29:56| F1: 0.4735 ± 0.0000
|2025-01-08 17:29:56| P: 0.5487 ± 0.0000
|2025-01-08 17:29:56| Recall: 0.4689 ± 0.0000
|2025-01-08 17:29:56| train_time: 2261.1326 ± 0.0000
|2025-01-08 17:30:00| Flops: 2737433600
|2025-01-08 17:30:00| Params: 9021
|2025-01-08 17:30:00| Inference time: 0.09 ms
|2025-01-08 17:30:00| ********************Experiment Success********************
```

```python
|2025-01-08 17:30:00| {
     'Ablation': 0, 'bs': 256, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 200, 'eval_set': True, 'experiment': False, 'log': <utils.logger.Logger object at 0x72014e788620>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': cnn,
     'num_classes': 6, 'optim': AdamW, 'path': ./datasets/, 'patience': 30,
     'program_test': False, 'rank': 80, 'record': True, 'retrain': False,
     'rounds': 1, 'seed': 0, 'time_interval': 10, 'train_size': 500,
     'verbose': 0,
}
|2025-01-08 17:30:00| ********************Experiment Start********************
|2025-01-08 18:14:09| Round=1 BestEpoch=195 Acc=0.6215 F1=0.5417 Precision=0.6163 Recall=0.5277 Training_time=2386.5 s 

|2025-01-08 18:14:09| ********************Experiment Results:********************
|2025-01-08 18:14:09| Acc: 0.6215 ± 0.0000
|2025-01-08 18:14:09| F1: 0.5417 ± 0.0000
|2025-01-08 18:14:09| P: 0.6163 ± 0.0000
|2025-01-08 18:14:09| Recall: 0.5277 ± 0.0000
|2025-01-08 18:14:09| train_time: 2386.4548 ± 0.0000
|2025-01-08 18:14:13| Flops: 6812917760
|2025-01-08 18:14:13| Params: 21621
|2025-01-08 18:14:13| Inference time: 0.10 ms
|2025-01-08 18:14:13| ********************Experiment Success********************
```

```python
|2025-01-08 18:14:13| {
     'Ablation': 0, 'bs': 256, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 200, 'eval_set': True, 'experiment': False, 'log': <utils.logger.Logger object at 0x7202b557ca40>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': cnn,
     'num_classes': 6, 'optim': AdamW, 'path': ./datasets/, 'patience': 30,
     'program_test': False, 'rank': 100, 'record': True, 'retrain': False,
     'rounds': 1, 'seed': 0, 'time_interval': 10, 'train_size': 500,
     'verbose': 0,
}
|2025-01-08 18:14:13| ********************Experiment Start********************
|2025-01-08 19:07:04| Round=1 BestEpoch=199 Acc=0.6361 F1=0.5641 Precision=0.6661 Recall=0.5355 Training_time=2921.2 s 

|2025-01-08 19:07:04| ********************Experiment Results:********************
|2025-01-08 19:07:04| Acc: 0.6361 ± 0.0000
|2025-01-08 19:07:04| F1: 0.5641 ± 0.0000
|2025-01-08 19:07:04| P: 0.6661 ± 0.0000
|2025-01-08 19:07:04| Recall: 0.5355 ± 0.0000
|2025-01-08 19:07:04| train_time: 2921.1983 ± 0.0000
|2025-01-08 19:07:08| Flops: 10543667200
|2025-01-08 19:07:08| Params: 33021
|2025-01-08 19:07:08| Inference time: 0.10 ms
|2025-01-08 19:07:08| ********************Experiment Success********************
```

