```python
|2025-01-29 23:40:04| {
     'ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'graph_encoder': gin, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x9cff2327230>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 2, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 64, 'record': True,
     'retrain': False, 'rounds': 10, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-29 23:40:04| ********************Experiment Start********************
|2025-01-29 23:40:53| Round=1 BestEpoch=148 Ac=0.8608 Pr=0.4640 Rc=0.4484 F1=0.4517 Training_time=24.8 s 

|2025-01-29 23:41:45| Round=2 BestEpoch=146 Ac=0.8706 Pr=0.4494 Rc=0.4280 F1=0.4344 Training_time=26.3 s 

|2025-01-29 23:42:20| Round=3 BestEpoch= 88 Ac=0.8544 Pr=0.4925 Rc=0.4454 F1=0.4610 Training_time=16.0 s 

|2025-01-29 23:42:50| Round=4 BestEpoch= 72 Ac=0.8544 Pr=0.4772 Rc=0.4437 F1=0.4560 Training_time=13.1 s 

|2025-01-29 23:43:24| Round=5 BestEpoch= 83 Ac=0.8544 Pr=0.4452 Rc=0.4451 F1=0.4436 Training_time=15.2 s 

|2025-01-29 23:43:48| Round=6 BestEpoch= 51 Ac=0.8576 Pr=0.4788 Rc=0.4452 F1=0.4578 Training_time=9.4 s 

|2025-01-29 23:44:16| Round=7 BestEpoch= 58 Ac=0.8511 Pr=0.4758 Rc=0.4440 F1=0.4553 Training_time=11.5 s 

|2025-01-29 23:44:40| Round=8 BestEpoch= 46 Ac=0.8447 Pr=0.4728 Rc=0.4399 F1=0.4518 Training_time=9.3 s 

|2025-01-29 23:45:24| Round=9 BestEpoch=113 Ac=0.8641 Pr=0.4646 Rc=0.4492 F1=0.4522 Training_time=21.8 s 

|2025-01-29 23:46:11| Round=10 BestEpoch=122 Ac=0.8673 Pr=0.4830 Rc=0.4500 F1=0.4617 Training_time=23.4 s 

|2025-01-29 23:46:11| ********************Experiment Results:********************
|2025-01-29 23:46:11| AC: 0.8579 ± 0.0074
|2025-01-29 23:46:11| PR: 0.4703 ± 0.0140
|2025-01-29 23:46:11| RC: 0.4439 ± 0.0060
|2025-01-29 23:46:11| F1: 0.4525 ± 0.0078
|2025-01-29 23:46:11| train_time: 17.0751 ± 6.1479
|2025-01-29 23:46:11| Flops: 7127040
|2025-01-29 23:46:11| Params: 27474
|2025-01-29 23:46:11| Inference time: 0.26 ms
|2025-01-29 23:46:14| ********************Experiment Success********************
```

