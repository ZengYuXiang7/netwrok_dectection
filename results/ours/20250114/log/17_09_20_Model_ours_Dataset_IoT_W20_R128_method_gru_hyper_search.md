```python
|2025-01-14 17:09:20| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7a9bdbb32000>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 10,
}
|2025-01-14 17:09:20| ********************Experiment Start********************
|2025-01-14 17:17:41| Round=1 BestEpoch= 73 Acc=0.9133 F1=0.8730 Precision=0.8725 Recall=0.8753 Training_time=319.3 s 

|2025-01-14 17:17:41| ********************Experiment Results:********************
|2025-01-14 17:17:41| Acc: 0.9133 ± 0.0000
|2025-01-14 17:17:41| F1: 0.8730 ± 0.0000
|2025-01-14 17:17:41| P: 0.8725 ± 0.0000
|2025-01-14 17:17:41| Recall: 0.8753 ± 0.0000
|2025-01-14 17:17:41| train_time: 319.2714 ± 0.0000
|2025-01-14 17:17:42| Flops: 4383444992
|2025-01-14 17:17:42| Params: 2042069
|2025-01-14 17:17:42| Inference time: 0.65 ms
|2025-01-14 17:17:42| ********************Experiment Success********************
```

