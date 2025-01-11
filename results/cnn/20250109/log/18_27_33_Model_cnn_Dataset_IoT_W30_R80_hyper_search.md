```python
|2025-01-09 18:27:33| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 30,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x7dcb46df88f0>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': cnn, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 80,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 18:27:33| ********************Experiment Start********************
|2025-01-09 18:35:11| Round=1 BestEpoch=417 Acc=0.8856 F1=0.8169 Precision=0.8318 Recall=0.8122 Training_time=335.1 s 

|2025-01-09 18:35:11| ********************Experiment Results:********************
|2025-01-09 18:35:11| Acc: 0.8856 ± 0.0000
|2025-01-09 18:35:11| F1: 0.8169 ± 0.0000
|2025-01-09 18:35:11| P: 0.8318 ± 0.0000
|2025-01-09 18:35:11| Recall: 0.8122 ± 0.0000
|2025-01-09 18:35:11| train_time: 335.1290 ± 0.0000
|2025-01-09 18:35:12| Flops: 77639680
|2025-01-09 18:35:12| Params: 21621
|2025-01-09 18:35:12| Inference time: 0.09 ms
|2025-01-09 18:35:12| ********************Experiment Success********************
```

