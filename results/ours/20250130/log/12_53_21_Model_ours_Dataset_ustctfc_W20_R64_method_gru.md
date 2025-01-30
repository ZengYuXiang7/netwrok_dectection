```python
|2025-01-30 12:53:21| {
     'ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': ustctfc, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x13ec74e92e40>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 4, 'num_classes': 21, 'num_layers': 2, 'optim': AdamW,
     'path': ./datasets/, 'patience': 60, 'program_test': False, 'rank': 64,
     'record': True, 'retrain': False, 'rounds': 5, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-30 12:53:21| ********************Experiment Start********************
|2025-01-30 12:58:04| Round=1 BestEpoch=  4 Ac=0.9952 Pr=0.5760 Rc=0.5774 F1=0.5694 Training_time=9.5 s 

|2025-01-30 13:02:10| Round=2 BestEpoch= 38 Ac=0.9955 Pr=0.5539 Rc=0.5804 F1=0.5627 Training_time=88.1 s 

|2025-01-30 13:04:49| Round=3 BestEpoch=  3 Ac=0.9945 Pr=0.5694 Rc=0.5072 F1=0.5171 Training_time=6.9 s 

|2025-01-30 13:09:33| Round=4 BestEpoch= 56 Ac=0.9933 Pr=0.5333 Rc=0.5655 F1=0.5431 Training_time=130.0 s 

|2025-01-30 13:12:04| Round=5 BestEpoch=  4 Ac=0.9944 Pr=0.5760 Rc=0.5365 F1=0.5328 Training_time=8.7 s 

|2025-01-30 13:12:04| ********************Experiment Results:********************
|2025-01-30 13:12:04| AC: 0.9946 ± 0.0008
|2025-01-30 13:12:04| PR: 0.5617 ± 0.0163
|2025-01-30 13:12:04| RC: 0.5534 ± 0.0278
|2025-01-30 13:12:04| F1: 0.5450 ± 0.0192
|2025-01-30 13:12:04| train_time: 48.6403 ± 51.0852
|2025-01-30 13:12:04| Flops: 743464960
|2025-01-30 13:12:04| Params: 648139
|2025-01-30 13:12:04| Inference time: 0.88 ms
|2025-01-30 13:12:05| ********************Experiment Success********************
```

