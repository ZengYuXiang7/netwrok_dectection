```python
|2025-01-11 07:35:40| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'graph_encoder': gin, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x72a147905370>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 6, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'verbose': 10,
}
|2025-01-11 07:35:40| ********************Experiment Start********************
|2025-01-11 08:07:39| Round=1 BestEpoch=336 Acc=0.8241 F1=0.7498 Precision=0.7700 Recall=0.7371 Training_time=1506.3 s 

|2025-01-11 08:07:39| ********************Experiment Results:********************
|2025-01-11 08:07:39| Acc: 0.8241 ± 0.0000
|2025-01-11 08:07:39| F1: 0.7498 ± 0.0000
|2025-01-11 08:07:39| P: 0.7700 ± 0.0000
|2025-01-11 08:07:39| Recall: 0.7371 ± 0.0000
|2025-01-11 08:07:39| train_time: 1506.2758 ± 0.0000
|2025-01-11 08:08:04| Flops: 25231360
|2025-01-11 08:08:04| Params: 70805
|2025-01-11 08:08:04| Inference time: 0.29 ms
|2025-01-11 08:08:04| ********************Experiment Success********************
```

