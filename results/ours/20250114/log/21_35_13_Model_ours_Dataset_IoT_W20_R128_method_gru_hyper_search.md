```python
|2025-01-14 21:35:13| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x76884ac62cc0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 10,
}
|2025-01-14 21:35:13| ********************Experiment Start********************
|2025-01-14 21:53:18| Round=1 BestEpoch=119 Acc=0.9195 F1=0.8776 Precision=0.8772 Recall=0.8783 Training_time=809.2 s 

|2025-01-14 21:53:18| ********************Experiment Results:********************
|2025-01-14 21:53:18| Acc: 0.9195 ± 0.0000
|2025-01-14 21:53:18| F1: 0.8776 ± 0.0000
|2025-01-14 21:53:18| P: 0.8772 ± 0.0000
|2025-01-14 21:53:18| Recall: 0.8783 ± 0.0000
|2025-01-14 21:53:18| train_time: 809.1930 ± 0.0000
|2025-01-14 21:53:19| Flops: 8762822656
|2025-01-14 21:53:19| Params: 4052949
|2025-01-14 21:53:19| Inference time: 1.07 ms
|2025-01-14 21:53:20| ********************Experiment Success********************
```

