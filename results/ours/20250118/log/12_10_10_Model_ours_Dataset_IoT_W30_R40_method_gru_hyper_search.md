```python
|2025-01-18 12:10:10| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x77b170246cc0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 2, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 40, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-18 12:10:10| ********************Experiment Start********************
|2025-01-18 12:16:11| Round=1 BestEpoch=170 Acc=0.9049 F1=0.8426 Precision=0.8533 Recall=0.8379 Training_time=280.4 s 

|2025-01-18 12:16:11| ********************Experiment Results:********************
|2025-01-18 12:16:11| Acc: 0.9049 ± 0.0000
|2025-01-18 12:16:11| F1: 0.8426 ± 0.0000
|2025-01-18 12:16:11| P: 0.8533 ± 0.0000
|2025-01-18 12:16:11| Recall: 0.8379 ± 0.0000
|2025-01-18 12:16:11| train_time: 280.4377 ± 0.0000
|2025-01-18 12:16:11| Flops: 442988800
|2025-01-18 12:16:11| Params: 162989
|2025-01-18 12:16:11| Inference time: 0.42 ms
|2025-01-18 12:16:12| ********************Experiment Success********************
```

