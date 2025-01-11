```python
|2025-01-09 21:43:11| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': False, 'log': <utils.logger.Logger object at 0x8ca2b6afc80>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 50,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 21:43:11| ********************Experiment Start********************
|2025-01-09 21:43:13| Acc=0.8237 F1=0.7664 Precision=0.7754 Recall=0.7684 time=270.9 s 
|2025-01-09 21:43:13| ********************Experiment Results:********************
|2025-01-09 21:43:13| Acc: 0.8237 ± 0.0000
|2025-01-09 21:43:13| F1: 0.7664 ± 0.0000
|2025-01-09 21:43:13| P: 0.7754 ± 0.0000
|2025-01-09 21:43:13| Recall: 0.7684 ± 0.0000
|2025-01-09 21:43:13| train_time: 270.9483 ± 0.0000
|2025-01-09 21:43:14| Flops: 128841600
|2025-01-09 21:43:14| Params: 107971
|2025-01-09 21:43:14| Inference time: 0.45 ms
|2025-01-09 21:43:14| ********************Experiment Success********************
```

