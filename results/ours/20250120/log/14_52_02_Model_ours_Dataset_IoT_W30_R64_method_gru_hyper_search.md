```python
|2025-01-20 14:52:02| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x70fe7e12a480>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 1, 'num_classes': 21, 'num_layers': 3, 'optim': AdamW,
     'path': ./datasets/, 'patience': 50, 'program_test': False, 'rank': 64,
     'record': True, 'retrain': True, 'rounds': 2, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-20 14:52:02| ********************Experiment Start********************
|2025-01-20 15:14:39| Round=1 BestEpoch=199 Acc=0.8062 F1=0.7277 Precision=0.7589 Recall=0.7139 Training_time=1040.1 s 

|2025-01-20 15:56:37| Round=2 BestEpoch=409 Acc=0.9142 F1=0.8641 Precision=0.8707 Recall=0.8594 Training_time=2151.0 s 

|2025-01-20 15:56:37| ********************Experiment Results:********************
|2025-01-20 15:56:37| Acc: 0.8602 ± 0.0540
|2025-01-20 15:56:37| F1: 0.7959 ± 0.0682
|2025-01-20 15:56:37| P: 0.8148 ± 0.0559
|2025-01-20 15:56:37| Recall: 0.7867 ± 0.0727
|2025-01-20 15:56:37| train_time: 1595.5523 ± 555.4611
|2025-01-20 15:56:37| Flops: 1664704512
|2025-01-20 15:56:37| Params: 1396053
|2025-01-20 15:56:37| Inference time: 1.57 ms
|2025-01-20 15:56:38| ********************Experiment Success********************
```

