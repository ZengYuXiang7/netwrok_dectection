```python
|2025-01-29 23:24:03| {
     'ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'graph_encoder': gcn, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xed7843cf320>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 64, 'record': True,
     'retrain': False, 'rounds': 10, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-29 23:24:03| ********************Experiment Start********************
|2025-01-29 23:24:41| Round=1 BestEpoch= 85 Ac=0.8738 Pr=0.4806 Rc=0.4530 F1=0.4628 Training_time=18.6 s 

|2025-01-29 23:25:16| Round=2 BestEpoch= 66 Ac=0.8641 Pr=0.4909 Rc=0.4738 F1=0.4783 Training_time=15.7 s 

|2025-01-29 23:26:04| Round=3 BestEpoch=103 Ac=0.8738 Pr=0.4637 Rc=0.4769 F1=0.4687 Training_time=24.8 s 

|2025-01-29 23:26:36| Round=4 BestEpoch= 59 Ac=0.8706 Pr=0.4535 Rc=0.4522 F1=0.4518 Training_time=14.1 s 

|2025-01-29 23:27:09| Round=5 BestEpoch= 63 Ac=0.8576 Pr=0.4562 Rc=0.4704 F1=0.4623 Training_time=15.1 s 

|2025-01-29 23:27:43| Round=6 BestEpoch= 63 Ac=0.8770 Pr=0.4562 Rc=0.4542 F1=0.4540 Training_time=15.0 s 

|2025-01-29 23:28:38| Round=7 BestEpoch=126 Ac=0.8673 Pr=0.4938 Rc=0.4736 F1=0.4788 Training_time=30.0 s 

|2025-01-29 23:29:18| Round=8 BestEpoch= 81 Ac=0.8091 Pr=0.4237 Rc=0.4300 F1=0.4262 Training_time=19.4 s 

|2025-01-29 23:29:49| Round=9 BestEpoch= 54 Ac=0.8608 Pr=0.4504 Rc=0.4481 F1=0.4480 Training_time=12.9 s 

|2025-01-29 23:30:59| Round=10 BestEpoch=165 Ac=0.8738 Pr=0.4714 Rc=0.4537 F1=0.4576 Training_time=39.3 s 

|2025-01-29 23:30:59| ********************Experiment Results:********************
|2025-01-29 23:30:59| AC: 0.8628 ± 0.0189
|2025-01-29 23:30:59| PR: 0.4640 ± 0.0200
|2025-01-29 23:30:59| RC: 0.4586 ± 0.0140
|2025-01-29 23:30:59| F1: 0.4589 ± 0.0147
|2025-01-29 23:30:59| train_time: 20.4831 ± 8.0559
|2025-01-29 23:31:00| Flops: 2539520
|2025-01-29 23:31:00| Params: 23570
|2025-01-29 23:31:00| Inference time: 1.28 ms
|2025-01-29 23:31:02| ********************Experiment Success********************
```

