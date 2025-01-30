```python
|2025-01-28 19:22:11| {
     'ablation': 2, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7b764d093500>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 4, 'num_classes': 21, 'num_layers': 2, 'optim': AdamW,
     'path': ./datasets/, 'patience': 50, 'program_test': False, 'rank': 64,
     'record': True, 'retrain': True, 'rounds': 2, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-28 19:22:11| ********************Experiment Start********************
|2025-01-28 19:25:22| Round=1 BestEpoch= 61 Ac=0.9234 Pr=0.8650 Rc=0.8605 F1=0.8624 Training_time=94.3 s 

|2025-01-28 19:31:28| Round=2 BestEpoch=158 Ac=0.9257 Pr=0.8769 Rc=0.8706 F1=0.8733 Training_time=250.3 s 

|2025-01-28 19:31:28| ********************Experiment Results:********************
|2025-01-28 19:31:28| AC: 0.9245 ± 0.0012
|2025-01-28 19:31:28| PR: 0.8710 ± 0.0060
|2025-01-28 19:31:28| RC: 0.8656 ± 0.0051
|2025-01-28 19:31:28| F1: 0.8678 ± 0.0055
|2025-01-28 19:31:28| train_time: 172.3162 ± 77.9711
|2025-01-28 19:31:28| Flops: 1115217920
|2025-01-28 19:31:28| Params: 407061
|2025-01-28 19:31:28| Inference time: 0.35 ms
|2025-01-28 19:31:29| ********************Experiment Success********************
```

