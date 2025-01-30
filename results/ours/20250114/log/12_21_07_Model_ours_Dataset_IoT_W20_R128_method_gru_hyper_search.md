```python
|2025-01-14 12:21:07| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7943c73d3290>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 2, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 2, 'verbose': 10,
}
|2025-01-14 12:21:07| ********************Experiment Start********************
|2025-01-14 12:36:54| Round=1 BestEpoch=165 Acc=0.9216 F1=0.8830 Precision=0.8825 Recall=0.8839 Training_time=720.7 s 

|2025-01-14 12:50:02| Round=2 BestEpoch=129 Acc=0.9238 F1=0.8823 Precision=0.8843 Recall=0.8807 Training_time=574.3 s 

|2025-01-14 12:50:02| ********************Experiment Results:********************
|2025-01-14 12:50:02| Acc: 0.9227 ± 0.0011
|2025-01-14 12:50:02| F1: 0.8827 ± 0.0004
|2025-01-14 12:50:02| P: 0.8834 ± 0.0009
|2025-01-14 12:50:02| Recall: 0.8823 ± 0.0016
|2025-01-14 12:50:02| train_time: 647.4570 ± 73.1957
|2025-01-14 12:50:02| Flops: 4384100352
|2025-01-14 12:50:02| Params: 2047445
|2025-01-14 12:50:02| Inference time: 0.68 ms
|2025-01-14 12:50:03| ********************Experiment Success********************
```

