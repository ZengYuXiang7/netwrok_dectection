```python
|2025-01-18 14:31:41| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x76af4ca13f50>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 2, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 2, 'verbose': 1,
}
|2025-01-18 14:31:41| ********************Experiment Start********************
|2025-01-18 14:46:48| Round=1 BestEpoch= 86 Acc=0.9007 F1=0.8412 Precision=0.8434 Recall=0.8412 Training_time=648.2 s 

|2025-01-18 14:46:48| ********************Experiment Results:********************
|2025-01-18 14:46:48| Acc: 0.9007 ± 0.0000
|2025-01-18 14:46:48| F1: 0.8412 ± 0.0000
|2025-01-18 14:46:48| P: 0.8434 ± 0.0000
|2025-01-18 14:46:48| Recall: 0.8412 ± 0.0000
|2025-01-18 14:46:48| train_time: 648.1958 ± 0.0000
|2025-01-18 14:46:48| Flops: 1513843200
|2025-01-18 14:46:48| Params: 1247525
|2025-01-18 14:46:48| Inference time: 2.22 ms
|2025-01-18 14:46:48| ********************Experiment Success********************
```

