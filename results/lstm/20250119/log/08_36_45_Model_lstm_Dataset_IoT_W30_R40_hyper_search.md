```python
|2025-01-19 08:36:45| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7eeb2b5eb7a0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': lstm, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 40, 'record': True, 'retrain': True, 'rounds': 5,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-19 08:36:45| ********************Experiment Start********************
|2025-01-19 08:39:42| Round=1 BestEpoch=207 Acc=0.8909 F1=0.8219 Precision=0.8314 Recall=0.8167 Training_time=125.6 s 

|2025-01-19 08:43:11| Round=2 BestEpoch=246 Acc=0.8922 F1=0.8348 Precision=0.8519 Recall=0.8292 Training_time=151.2 s 

|2025-01-19 08:45:38| Round=3 BestEpoch=167 Acc=0.8902 F1=0.8261 Precision=0.8361 Recall=0.8239 Training_time=101.2 s 

|2025-01-19 08:48:48| Round=4 BestEpoch=219 Acc=0.8888 F1=0.8319 Precision=0.8385 Recall=0.8308 Training_time=134.4 s 

|2025-01-19 08:51:12| Round=5 BestEpoch=159 Acc=0.8840 F1=0.8203 Precision=0.8342 Recall=0.8122 Training_time=97.5 s 

|2025-01-19 08:51:12| ********************Experiment Results:********************
|2025-01-19 08:51:12| Acc: 0.8892 ± 0.0028
|2025-01-19 08:51:12| F1: 0.8270 ± 0.0056
|2025-01-19 08:51:12| P: 0.8384 ± 0.0071
|2025-01-19 08:51:12| Recall: 0.8226 ± 0.0071
|2025-01-19 08:51:12| train_time: 121.9744 ± 20.2650
|2025-01-19 08:51:12| Flops: 82483200
|2025-01-19 08:51:12| Params: 45221
|2025-01-19 08:51:12| Inference time: 0.07 ms
|2025-01-19 08:51:13| ********************Experiment Success********************
```

