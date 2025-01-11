```python
|2025-01-10 00:54:10| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x7977b0003560>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 104,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'seq_method': self, 'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-10 00:54:10| ********************Experiment Start********************
|2025-01-10 00:59:37| Round=1 BestEpoch=139 Acc=0.9042 F1=0.8542 Precision=0.8553 Recall=0.8542 Training_time=230.9 s 

|2025-01-10 00:59:37| ********************Experiment Results:********************
|2025-01-10 00:59:37| Acc: 0.9042 ± 0.0000
|2025-01-10 00:59:37| F1: 0.8542 ± 0.0000
|2025-01-10 00:59:37| P: 0.8553 ± 0.0000
|2025-01-10 00:59:37| Recall: 0.8542 ± 0.0000
|2025-01-10 00:59:37| train_time: 230.9148 ± 0.0000
|2025-01-10 00:59:39| Flops: 91060736
|2025-01-10 00:59:39| Params: 282693
|2025-01-10 00:59:39| Inference time: 0.38 ms
|2025-01-10 00:59:39| ********************Experiment Success********************
```

