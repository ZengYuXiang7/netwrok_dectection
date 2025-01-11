```python
|2025-01-09 17:55:17| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 40,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x7afbf7425f70>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': lstm, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 50,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 17:55:17| ********************Experiment Start********************
|2025-01-09 17:58:47| Round=1 BestEpoch=230 Acc=0.8447 F1=0.7657 Precision=0.7743 Recall=0.7601 Training_time=142.2 s 

|2025-01-09 17:58:47| ********************Experiment Results:********************
|2025-01-09 17:58:47| Acc: 0.8447 ± 0.0000
|2025-01-09 17:58:47| F1: 0.7657 ± 0.0000
|2025-01-09 17:58:47| P: 0.7743 ± 0.0000
|2025-01-09 17:58:47| Recall: 0.7601 ± 0.0000
|2025-01-09 17:58:47| train_time: 142.1582 ± 0.0000
|2025-01-09 17:58:47| Flops: 168192000
|2025-01-09 17:58:47| Params: 73021
|2025-01-09 17:58:47| Inference time: 0.09 ms
|2025-01-09 17:58:48| ********************Experiment Success********************
```

