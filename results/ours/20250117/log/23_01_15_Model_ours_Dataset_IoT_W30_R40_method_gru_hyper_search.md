```python
|2025-01-17 23:01:15| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x77d74218da00>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 1, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 40, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-17 23:01:15| ********************Experiment Start********************
|2025-01-17 23:10:25| Round=1 BestEpoch=140 Acc=0.8965 F1=0.8324 Precision=0.8394 Recall=0.8294 Training_time=427.0 s 

|2025-01-17 23:10:25| ********************Experiment Results:********************
|2025-01-17 23:10:25| Acc: 0.8965 ± 0.0000
|2025-01-17 23:10:25| F1: 0.8324 ± 0.0000
|2025-01-17 23:10:25| P: 0.8394 ± 0.0000
|2025-01-17 23:10:25| Recall: 0.8294 ± 0.0000
|2025-01-17 23:10:25| train_time: 426.9598 ± 0.0000
|2025-01-17 23:10:26| Flops: 406247680
|2025-01-17 23:10:26| Params: 327669
|2025-01-17 23:10:26| Inference time: 0.87 ms
|2025-01-17 23:10:26| ********************Experiment Success********************
```

