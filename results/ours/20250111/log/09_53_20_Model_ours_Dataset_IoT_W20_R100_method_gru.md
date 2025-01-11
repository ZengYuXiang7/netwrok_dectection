```python
|2025-01-11 09:53:20| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x142e5b48ab40>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 6, 'optim': AdamW, 'path': ./datasets/, 'patience': 30,
     'program_test': False, 'rank': 100, 'record': True, 'retrain': False,
     'rounds': 1, 'seed': 0, 'seq_method': gru, 'time_interval': 10,
     'train_size': 500, 'verbose': 10,
}
|2025-01-11 09:53:20| ********************Experiment Start********************
|2025-01-11 09:57:20| Round=1 BestEpoch= 65 Acc=0.9243 F1=0.8875 Precision=0.8881 Recall=0.8873 Training_time=144.2 s 

|2025-01-11 09:57:20| ********************Experiment Results:********************
|2025-01-11 09:57:20| Acc: 0.9243 ± 0.0000
|2025-01-11 09:57:20| F1: 0.8875 ± 0.0000
|2025-01-11 09:57:20| P: 0.8881 ± 0.0000
|2025-01-11 09:57:20| Recall: 0.8873 ± 0.0000
|2025-01-11 09:57:20| train_time: 144.2326 ± 0.0000
|2025-01-11 09:57:21| Flops: 916924800
|2025-01-11 09:57:21| Params: 584921
|2025-01-11 09:57:21| Inference time: 0.37 ms
|2025-01-11 09:57:21| ********************Experiment Success********************
```

