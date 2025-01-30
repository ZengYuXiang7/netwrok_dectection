```python
|2025-01-19 15:15:11| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gat, 'heads': 2, 'hyper_search': False,
     'log': <utils.logger.Logger object at 0xf0d0913ab70>, 'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001,
     'model': gnn, 'num_classes': 21, 'optim': AdamW, 'order': 3,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 60,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-19 15:15:11| ********************Experiment Start********************
|2025-01-19 15:15:24| Acc=0.8811 F1=0.8175 Precision=0.8280 Recall=0.8118 time=910.1 s 
|2025-01-19 15:15:24| ********************Experiment Results:********************
|2025-01-19 15:15:24| Acc: 0.8811 ± 0.0000
|2025-01-19 15:15:24| F1: 0.8175 ± 0.0000
|2025-01-19 15:15:24| P: 0.8280 ± 0.0000
|2025-01-19 15:15:24| Recall: 0.8118 ± 0.0000
|2025-01-19 15:15:24| train_time: 910.1100 ± 0.0000
|2025-01-19 15:15:39| Flops: 45388800
|2025-01-19 15:15:39| Params: 59901
|2025-01-19 15:15:39| Inference time: 1.76 ms
|2025-01-19 15:15:39| ********************Experiment Success********************
```

