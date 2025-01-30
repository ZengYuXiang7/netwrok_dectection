```python
|2025-01-19 09:05:20| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x76b0e8379c40>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': lstm, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 60, 'record': True, 'retrain': True, 'rounds': 5,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-19 09:05:20| ********************Experiment Start********************
|2025-01-19 09:07:53| Round=1 BestEpoch=174 Acc=0.8939 F1=0.8308 Precision=0.8357 Recall=0.8281 Training_time=105.5 s 

|2025-01-19 09:10:43| Round=2 BestEpoch=194 Acc=0.8934 F1=0.8348 Precision=0.8415 Recall=0.8312 Training_time=119.4 s 

|2025-01-19 09:13:10| Round=3 BestEpoch=164 Acc=0.8870 F1=0.8192 Precision=0.8254 Recall=0.8179 Training_time=100.4 s 

|2025-01-19 09:15:35| Round=4 BestEpoch=162 Acc=0.8871 F1=0.8238 Precision=0.8257 Recall=0.8237 Training_time=99.3 s 

|2025-01-19 09:17:47| Round=5 BestEpoch=138 Acc=0.8895 F1=0.8312 Precision=0.8434 Recall=0.8226 Training_time=85.4 s 

|2025-01-19 09:17:47| ********************Experiment Results:********************
|2025-01-19 09:17:47| Acc: 0.8902 ± 0.0030
|2025-01-19 09:17:47| F1: 0.8280 ± 0.0057
|2025-01-19 09:17:47| P: 0.8343 ± 0.0076
|2025-01-19 09:17:47| Recall: 0.8247 ± 0.0046
|2025-01-19 09:17:47| train_time: 102.0212 ± 10.9492
|2025-01-19 09:17:47| Flops: 179020800
|2025-01-19 09:17:47| Params: 82221
|2025-01-19 09:17:47| Inference time: 0.08 ms
|2025-01-19 09:17:49| ********************Experiment Success********************
```

