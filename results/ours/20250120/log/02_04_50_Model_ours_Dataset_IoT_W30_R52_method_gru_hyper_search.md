```python
|2025-01-20 02:04:50| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7f455cd496a0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 1, 'num_classes': 21, 'num_layers': 2, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 52,
     'record': True, 'retrain': True, 'rounds': 5, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-20 02:04:50| ********************Experiment Start********************
|2025-01-20 02:16:44| Round=1 BestEpoch=151 Acc=0.9264 F1=0.8748 Precision=0.8819 Recall=0.8696 Training_time=566.4 s 

|2025-01-20 02:28:59| Round=2 BestEpoch=156 Acc=0.9263 F1=0.8797 Precision=0.8834 Recall=0.8768 Training_time=586.2 s 

|2025-01-20 02:43:07| Round=3 BestEpoch=184 Acc=0.9187 F1=0.8638 Precision=0.8700 Recall=0.8600 Training_time=692.7 s 

|2025-01-20 02:53:26| Round=4 BestEpoch=126 Acc=0.9238 F1=0.8742 Precision=0.8749 Recall=0.8748 Training_time=474.3 s 

|2025-01-20 03:04:37| Round=5 BestEpoch=139 Acc=0.9199 F1=0.8594 Precision=0.8690 Recall=0.8519 Training_time=524.1 s 

|2025-01-20 03:04:37| ********************Experiment Results:********************
|2025-01-20 03:04:37| Acc: 0.9230 ± 0.0032
|2025-01-20 03:04:37| F1: 0.8704 ± 0.0076
|2025-01-20 03:04:37| P: 0.8759 ± 0.0059
|2025-01-20 03:04:37| Recall: 0.8666 ± 0.0094
|2025-01-20 03:04:37| train_time: 568.7265 ± 72.9139
|2025-01-20 03:04:37| Flops: 740752896
|2025-01-20 03:04:37| Params: 643989
|2025-01-20 03:04:37| Inference time: 1.17 ms
|2025-01-20 03:04:38| ********************Experiment Success********************
```

