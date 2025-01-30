```python
|2025-01-29 22:28:12| {
     'ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'graph_encoder': gcn, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xb9bebaaae40>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 64, 'record': True,
     'retrain': False, 'rounds': 5, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-29 22:28:12| ********************Experiment Start********************
|2025-01-29 22:28:53| Round=1 BestEpoch= 85 Ac=0.8738 Pr=0.4806 Rc=0.4530 F1=0.4628 Training_time=17.0 s 

|2025-01-29 22:29:25| Round=2 BestEpoch= 66 Ac=0.8641 Pr=0.4909 Rc=0.4738 F1=0.4783 Training_time=14.5 s 

|2025-01-29 22:30:08| Round=3 BestEpoch=103 Ac=0.8738 Pr=0.4637 Rc=0.4769 F1=0.4687 Training_time=22.5 s 

|2025-01-29 22:30:38| Round=4 BestEpoch= 59 Ac=0.8706 Pr=0.4535 Rc=0.4522 F1=0.4518 Training_time=12.9 s 

|2025-01-29 22:31:08| Round=5 BestEpoch= 63 Ac=0.8576 Pr=0.4562 Rc=0.4704 F1=0.4623 Training_time=13.5 s 

|2025-01-29 22:31:08| ********************Experiment Results:********************
|2025-01-29 22:31:08| AC: 0.8680 ± 0.0063
|2025-01-29 22:31:08| PR: 0.4690 ± 0.0145
|2025-01-29 22:31:08| RC: 0.4653 ± 0.0105
|2025-01-29 22:31:08| F1: 0.4648 ± 0.0087
|2025-01-29 22:31:08| train_time: 16.0957 ± 3.4997
|2025-01-29 22:31:09| Flops: 2539520
|2025-01-29 22:31:09| Params: 23570
|2025-01-29 22:31:09| Inference time: 1.16 ms
|2025-01-29 22:31:10| ********************Experiment Success********************
```

