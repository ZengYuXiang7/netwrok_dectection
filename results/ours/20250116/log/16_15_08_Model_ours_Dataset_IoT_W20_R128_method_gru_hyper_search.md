```python
|2025-01-16 16:15:08| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x71b61de90050>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-16 16:15:08| ********************Experiment Start********************
|2025-01-16 16:38:32| Round=1 BestEpoch=113 Acc=0.9221 F1=0.8836 Precision=0.8821 Recall=0.8853 Training_time=1054.9 s 

|2025-01-16 16:38:32| ********************Experiment Results:********************
|2025-01-16 16:38:32| Acc: 0.9221 ± 0.0000
|2025-01-16 16:38:32| F1: 0.8836 ± 0.0000
|2025-01-16 16:38:32| P: 0.8821 ± 0.0000
|2025-01-16 16:38:32| Recall: 0.8853 ± 0.0000
|2025-01-16 16:38:32| train_time: 1054.9293 ± 0.0000
|2025-01-16 16:38:33| Flops: 7671828480
|2025-01-16 16:38:33| Params: 5684565
|2025-01-16 16:38:33| Inference time: 1.50 ms
|2025-01-16 16:38:34| ********************Experiment Success********************
```

