```python
|2025-01-19 10:14:38| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gcn, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7ba43e4e61e0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 40, 'record': True,
     'retrain': True, 'rounds': 5, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-19 10:14:38| ********************Experiment Start********************
|2025-01-19 10:27:21| Round=1 BestEpoch=169 Acc=0.8409 F1=0.7588 Precision=0.7685 Recall=0.7551 Training_time=545.4 s 

|2025-01-19 10:53:12| Round=2 BestEpoch=343 Acc=0.8622 F1=0.7883 Precision=0.7947 Recall=0.7854 Training_time=1210.3 s 

|2025-01-19 11:10:00| Round=3 BestEpoch=216 Acc=0.8568 F1=0.7850 Precision=0.8003 Recall=0.7789 Training_time=752.8 s 

|2025-01-19 11:21:07| Round=4 BestEpoch=132 Acc=0.8435 F1=0.7643 Precision=0.7768 Recall=0.7583 Training_time=460.8 s 

|2025-01-19 11:46:16| Round=5 BestEpoch=337 Acc=0.8594 F1=0.7819 Precision=0.7874 Recall=0.7796 Training_time=1186.9 s 

|2025-01-19 11:46:16| ********************Experiment Results:********************
|2025-01-19 11:46:16| Acc: 0.8526 ± 0.0087
|2025-01-19 11:46:16| F1: 0.7757 ± 0.0118
|2025-01-19 11:46:16| P: 0.7856 ± 0.0116
|2025-01-19 11:46:16| Recall: 0.7715 ± 0.0123
|2025-01-19 11:46:16| train_time: 831.2432 ± 314.7352
|2025-01-19 11:46:32| Flops: 2611200
|2025-01-19 11:46:32| Params: 25541
|2025-01-19 11:46:32| Inference time: 1.33 ms
|2025-01-19 11:46:33| ********************Experiment Success********************
```

