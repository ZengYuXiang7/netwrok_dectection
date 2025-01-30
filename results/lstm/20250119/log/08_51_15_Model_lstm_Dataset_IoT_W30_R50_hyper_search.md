```python
|2025-01-19 08:51:15| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7d0ffe09c3b0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': lstm, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 50, 'record': True, 'retrain': True, 'rounds': 5,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-19 08:51:15| ********************Experiment Start********************
|2025-01-19 08:53:24| Round=1 BestEpoch=143 Acc=0.8918 F1=0.8296 Precision=0.8329 Recall=0.8280 Training_time=86.0 s 

|2025-01-19 08:56:20| Round=2 BestEpoch=204 Acc=0.8970 F1=0.8423 Precision=0.8476 Recall=0.8398 Training_time=124.2 s 

|2025-01-19 08:59:32| Round=3 BestEpoch=226 Acc=0.8937 F1=0.8276 Precision=0.8361 Recall=0.8238 Training_time=137.1 s 

|2025-01-19 09:02:47| Round=4 BestEpoch=215 Acc=0.8918 F1=0.8335 Precision=0.8355 Recall=0.8340 Training_time=139.6 s 

|2025-01-19 09:05:17| Round=5 BestEpoch=169 Acc=0.8895 F1=0.8237 Precision=0.8342 Recall=0.8174 Training_time=103.0 s 

|2025-01-19 09:05:17| ********************Experiment Results:********************
|2025-01-19 09:05:17| Acc: 0.8927 ± 0.0025
|2025-01-19 09:05:17| F1: 0.8313 ± 0.0063
|2025-01-19 09:05:17| P: 0.8373 ± 0.0053
|2025-01-19 09:05:17| Recall: 0.8286 ± 0.0078
|2025-01-19 09:05:17| train_time: 117.9955 ± 20.5764
|2025-01-19 09:05:17| Flops: 126144000
|2025-01-19 09:05:17| Params: 62521
|2025-01-19 09:05:17| Inference time: 0.07 ms
|2025-01-19 09:05:18| ********************Experiment Success********************
```

