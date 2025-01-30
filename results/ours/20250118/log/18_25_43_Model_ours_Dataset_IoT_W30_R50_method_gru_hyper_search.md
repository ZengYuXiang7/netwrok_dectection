```python
|2025-01-18 18:25:43| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x71794931d8e0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-18 18:25:43| ********************Experiment Start********************
|2025-01-18 18:28:53| Round=1 BestEpoch= 51 Acc=0.9019 F1=0.8419 Precision=0.8531 Recall=0.8371 Training_time=111.2 s 

|2025-01-18 18:28:53| ********************Experiment Results:********************
|2025-01-18 18:28:53| Acc: 0.9019 ± 0.0000
|2025-01-18 18:28:53| F1: 0.8419 ± 0.0000
|2025-01-18 18:28:53| P: 0.8531 ± 0.0000
|2025-01-18 18:28:53| Recall: 0.8371 ± 0.0000
|2025-01-18 18:28:53| train_time: 111.2420 ± 0.0000
|2025-01-18 18:28:54| Flops: 1024204800
|2025-01-18 18:28:54| Params: 339825
|2025-01-18 18:28:54| Inference time: 0.56 ms
|2025-01-18 18:28:54| ********************Experiment Success********************
```

