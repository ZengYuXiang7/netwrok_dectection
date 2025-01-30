```python
|2025-01-19 09:38:22| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7a76c2b72b70>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': cnn, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 50, 'record': True, 'retrain': True, 'rounds': 5,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-19 09:38:22| ********************Experiment Start********************
|2025-01-19 09:40:44| Round=1 BestEpoch=157 Acc=0.8590 F1=0.7800 Precision=0.8122 Recall=0.7856 Training_time=93.4 s 

|2025-01-19 09:44:30| Round=2 BestEpoch=266 Acc=0.8796 F1=0.8143 Precision=0.8487 Recall=0.8109 Training_time=160.4 s 

|2025-01-19 09:47:10| Round=3 BestEpoch=182 Acc=0.8447 F1=0.7487 Precision=0.8271 Recall=0.7348 Training_time=108.6 s 

|2025-01-19 09:49:35| Round=4 BestEpoch=158 Acc=0.8585 F1=0.7926 Precision=0.8186 Recall=0.7855 Training_time=95.1 s 

|2025-01-19 09:54:18| Round=5 BestEpoch=336 Acc=0.8791 F1=0.8076 Precision=0.8390 Recall=0.7975 Training_time=203.9 s 

|2025-01-19 09:54:18| ********************Experiment Results:********************
|2025-01-19 09:54:18| Acc: 0.8642 ± 0.0134
|2025-01-19 09:54:18| F1: 0.7886 ± 0.0233
|2025-01-19 09:54:18| P: 0.8291 ± 0.0133
|2025-01-19 09:54:18| Recall: 0.7829 ± 0.0258
|2025-01-19 09:54:18| train_time: 132.2783 ± 43.3157
|2025-01-19 09:54:18| Flops: 31244800
|2025-01-19 09:54:18| Params: 9021
|2025-01-19 09:54:18| Inference time: 0.09 ms
|2025-01-19 09:54:19| ********************Experiment Success********************
```

