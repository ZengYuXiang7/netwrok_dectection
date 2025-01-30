```python
|2025-01-18 15:26:16| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7a9377508590>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 2, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 6, 'verbose': 1,
}
|2025-01-18 15:26:16| ********************Experiment Start********************
|2025-01-18 15:36:06| Round=1 BestEpoch= 60 Acc=0.9016 F1=0.8359 Precision=0.8446 Recall=0.8307 Training_time=378.3 s 

|2025-01-18 15:36:06| ********************Experiment Results:********************
|2025-01-18 15:36:06| Acc: 0.9016 ± 0.0000
|2025-01-18 15:36:06| F1: 0.8359 ± 0.0000
|2025-01-18 15:36:06| P: 0.8446 ± 0.0000
|2025-01-18 15:36:06| Recall: 0.8307 ± 0.0000
|2025-01-18 15:36:06| train_time: 378.2574 ± 0.0000
|2025-01-18 15:36:06| Flops: 1238630400
|2025-01-18 15:36:06| Params: 1036675
|2025-01-18 15:36:06| Inference time: 1.80 ms
|2025-01-18 15:36:07| ********************Experiment Success********************
```

