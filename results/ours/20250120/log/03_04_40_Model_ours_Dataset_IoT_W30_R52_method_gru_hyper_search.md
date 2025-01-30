```python
|2025-01-20 03:04:40| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7ae1c25d3c80>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 2, 'num_classes': 21, 'num_layers': 2, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 52,
     'record': True, 'retrain': True, 'rounds': 5, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-20 03:04:40| ********************Experiment Start********************
|2025-01-20 03:12:24| Round=1 BestEpoch= 88 Acc=0.9182 F1=0.8628 Precision=0.8663 Recall=0.8605 Training_time=328.3 s 

|2025-01-20 03:22:13| Round=2 BestEpoch=119 Acc=0.8970 F1=0.8429 Precision=0.8509 Recall=0.8389 Training_time=447.3 s 

|2025-01-20 03:34:38| Round=3 BestEpoch=159 Acc=0.9096 F1=0.8514 Precision=0.8593 Recall=0.8519 Training_time=595.9 s 

|2025-01-20 03:45:01| Round=4 BestEpoch=128 Acc=0.9087 F1=0.8579 Precision=0.8654 Recall=0.8556 Training_time=480.1 s 

|2025-01-20 03:56:25| Round=5 BestEpoch=143 Acc=0.9163 F1=0.8602 Precision=0.8688 Recall=0.8544 Training_time=537.3 s 

|2025-01-20 03:56:25| ********************Experiment Results:********************
|2025-01-20 03:56:25| Acc: 0.9099 ± 0.0075
|2025-01-20 03:56:25| F1: 0.8550 ± 0.0071
|2025-01-20 03:56:25| P: 0.8622 ± 0.0064
|2025-01-20 03:56:25| Recall: 0.8523 ± 0.0072
|2025-01-20 03:56:25| train_time: 477.7920 ± 90.2943
|2025-01-20 03:56:26| Flops: 740752896
|2025-01-20 03:56:26| Params: 643989
|2025-01-20 03:56:26| Inference time: 1.15 ms
|2025-01-20 03:56:27| ********************Experiment Success********************
```

