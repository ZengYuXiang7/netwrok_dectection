```python
|2025-01-19 22:33:47| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x723d15f2ecc0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 2, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': True, 'rounds': 2, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-19 22:33:47| ********************Experiment Start********************
|2025-01-19 22:42:32| Round=1 BestEpoch=102 Acc=0.9289 F1=0.8745 Precision=0.8786 Recall=0.8718 Training_time=385.1 s 

|2025-01-19 22:53:41| Round=2 BestEpoch=137 Acc=0.9272 F1=0.8776 Precision=0.8797 Recall=0.8765 Training_time=520.6 s 

|2025-01-19 22:53:41| ********************Experiment Results:********************
|2025-01-19 22:53:41| Acc: 0.9280 ± 0.0009
|2025-01-19 22:53:41| F1: 0.8760 ± 0.0015
|2025-01-19 22:53:41| P: 0.8791 ± 0.0006
|2025-01-19 22:53:41| Recall: 0.8742 ± 0.0023
|2025-01-19 22:53:41| train_time: 452.8442 ± 67.7296
|2025-01-19 22:53:41| Flops: 685766400
|2025-01-19 22:53:41| Params: 595821
|2025-01-19 22:53:41| Inference time: 1.24 ms
|2025-01-19 22:53:41| ********************Experiment Success********************
```

