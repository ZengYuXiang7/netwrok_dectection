```python
|2025-01-29 20:37:31| {
     'ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': ustctfc, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x14f186676930>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 4, 'num_classes': 21, 'num_layers': 2, 'optim': AdamW,
     'path': ./datasets/, 'patience': 50, 'program_test': False, 'rank': 52,
     'record': True, 'retrain': False, 'rounds': 2, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-29 20:37:31| ********************Experiment Start********************
|2025-01-29 20:38:47| Round=1 BestEpoch= 38 Ac=0.8600 Pr=0.7553 Rc=0.7786 F1=0.7622 Training_time=5.7 s 

|2025-01-29 20:38:47| Ac=0.8400 Pr=0.7638 Rc=0.5910 F1=0.6387 time=9.0 s 
|2025-01-29 20:38:47| ********************Experiment Results:********************
|2025-01-29 20:38:47| AC: 0.8500 ± 0.0100
|2025-01-29 20:38:47| PR: 0.7595 ± 0.0043
|2025-01-29 20:38:47| RC: 0.6848 ± 0.0938
|2025-01-29 20:38:47| F1: 0.7005 ± 0.0618
|2025-01-29 20:38:47| train_time: 7.3583 ± 1.6532
|2025-01-29 20:38:47| Flops: 493881856
|2025-01-29 20:38:47| Params: 429589
|2025-01-29 20:38:47| Inference time: 0.87 ms
|2025-01-29 20:38:47| ********************Experiment Success********************
```

