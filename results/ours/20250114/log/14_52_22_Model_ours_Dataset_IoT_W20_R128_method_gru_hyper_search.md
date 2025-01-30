```python
|2025-01-14 14:52:22| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7421cd0d3c20>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 10,
}
|2025-01-14 14:52:22| ********************Experiment Start********************
|2025-01-14 15:07:31| Round=1 BestEpoch=114 Acc=0.8466 F1=0.7736 Precision=0.7769 Recall=0.7718 Training_time=662.6 s 

|2025-01-14 15:07:31| ********************Experiment Results:********************
|2025-01-14 15:07:31| Acc: 0.8466 ± 0.0000
|2025-01-14 15:07:31| F1: 0.7736 ± 0.0000
|2025-01-14 15:07:31| P: 0.7769 ± 0.0000
|2025-01-14 15:07:31| Recall: 0.7718 ± 0.0000
|2025-01-14 15:07:31| train_time: 662.5749 ± 0.0000
|2025-01-14 15:07:32| Flops: 4384428032
|2025-01-14 15:07:32| Params: 2042075
|2025-01-14 15:07:32| Inference time: 1.28 ms
|2025-01-14 15:07:33| ********************Experiment Success********************
```

