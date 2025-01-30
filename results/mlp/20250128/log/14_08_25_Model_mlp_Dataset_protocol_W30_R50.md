```python
|2025-01-28 14:08:25| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': protocol, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x128410d6a3c0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': mlp, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 50, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-28 14:08:25| ********************Experiment Start********************
|2025-01-28 14:14:33| Round=1 BestEpoch=101 Ac=0.5187 Pr=0.4611 Rc=0.3971 F1=0.4069 Training_time=12.4 s 

|2025-01-28 14:14:46| Round=2 BestEpoch= 27 Ac=0.4533 Pr=0.4153 Rc=0.3438 F1=0.3448 Training_time=3.3 s 

|2025-01-28 14:14:46| ********************Experiment Results:********************
|2025-01-28 14:14:46| AC: 0.4860 ± 0.0327
|2025-01-28 14:14:46| PR: 0.4382 ± 0.0229
|2025-01-28 14:14:46| RC: 0.3704 ± 0.0266
|2025-01-28 14:14:46| F1: 0.3759 ± 0.0310
|2025-01-28 14:14:46| train_time: 7.8811 ± 4.5492
|2025-01-28 14:14:46| Flops: 749824
|2025-01-28 14:14:46| Params: 5731
|2025-01-28 14:14:46| Inference time: 0.06 ms
|2025-01-28 14:14:47| ********************Experiment Success********************
```

