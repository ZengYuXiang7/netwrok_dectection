```python
|2025-01-18 14:16:33| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7e0719961e20>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 2, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-18 14:16:33| ********************Experiment Start********************
|2025-01-18 14:31:38| Round=1 BestEpoch= 86 Acc=0.9044 F1=0.8379 Precision=0.8507 Recall=0.8337 Training_time=646.9 s 

|2025-01-18 14:31:38| ********************Experiment Results:********************
|2025-01-18 14:31:38| Acc: 0.9044 ± 0.0000
|2025-01-18 14:31:38| F1: 0.8379 ± 0.0000
|2025-01-18 14:31:38| P: 0.8507 ± 0.0000
|2025-01-18 14:31:38| Recall: 0.8337 ± 0.0000
|2025-01-18 14:31:38| train_time: 646.9046 ± 0.0000
|2025-01-18 14:31:38| Flops: 1285299200
|2025-01-18 14:31:38| Params: 1222525
|2025-01-18 14:31:38| Inference time: 2.15 ms
|2025-01-18 14:31:39| ********************Experiment Success********************
```

