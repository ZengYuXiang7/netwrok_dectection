```python
|2025-01-28 19:42:41| {
     'ablation': 3, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7c276b70f140>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 4, 'num_classes': 21, 'num_layers': 2, 'optim': AdamW,
     'path': ./datasets/, 'patience': 50, 'program_test': False, 'rank': 64,
     'record': True, 'retrain': True, 'rounds': 2, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-28 19:42:41| ********************Experiment Start********************
|2025-01-28 19:51:15| Round=1 BestEpoch=310 Ac=0.9082 Pr=0.8653 Rc=0.8404 F1=0.8425 Training_time=391.4 s 

|2025-01-28 19:56:04| Round=2 BestEpoch=151 Ac=0.8875 Pr=0.8417 Rc=0.8126 F1=0.8188 Training_time=191.3 s 

|2025-01-28 19:56:04| ********************Experiment Results:********************
|2025-01-28 19:56:04| AC: 0.8978 ± 0.0104
|2025-01-28 19:56:04| PR: 0.8535 ± 0.0118
|2025-01-28 19:56:04| RC: 0.8265 ± 0.0139
|2025-01-28 19:56:04| F1: 0.8307 ± 0.0119
|2025-01-28 19:56:04| train_time: 291.3387 ± 100.0312
|2025-01-28 19:56:04| Flops: 113745920
|2025-01-28 19:56:04| Params: 117525
|2025-01-28 19:56:04| Inference time: 0.41 ms
|2025-01-28 19:56:04| ********************Experiment Success********************
```

