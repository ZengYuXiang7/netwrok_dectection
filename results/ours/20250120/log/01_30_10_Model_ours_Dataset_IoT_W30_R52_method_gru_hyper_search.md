```python
|2025-01-20 01:30:10| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7ef6d1782240>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 4, 'num_classes': 21, 'num_layers': 1, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 52,
     'record': True, 'retrain': True, 'rounds': 5, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-20 01:30:10| ********************Experiment Start********************
|2025-01-20 01:35:38| Round=1 BestEpoch=105 Acc=0.9237 F1=0.8705 Precision=0.8752 Recall=0.8674 Training_time=238.1 s 

|2025-01-20 01:43:08| Round=2 BestEpoch=154 Acc=0.9219 F1=0.8698 Precision=0.8734 Recall=0.8678 Training_time=351.5 s 

|2025-01-20 01:50:27| Round=3 BestEpoch=150 Acc=0.9234 F1=0.8725 Precision=0.8779 Recall=0.8706 Training_time=341.0 s 

|2025-01-20 01:58:06| Round=4 BestEpoch=158 Acc=0.9206 F1=0.8651 Precision=0.8650 Recall=0.8675 Training_time=359.9 s 

|2025-01-20 02:04:45| Round=5 BestEpoch=133 Acc=0.9161 F1=0.8535 Precision=0.8588 Recall=0.8501 Training_time=303.1 s 

|2025-01-20 02:04:45| ********************Experiment Results:********************
|2025-01-20 02:04:45| Acc: 0.9211 ± 0.0028
|2025-01-20 02:04:45| F1: 0.8663 ± 0.0068
|2025-01-20 02:04:45| P: 0.8701 ± 0.0071
|2025-01-20 02:04:45| Recall: 0.8647 ± 0.0074
|2025-01-20 02:04:45| train_time: 318.7316 ± 44.7655
|2025-01-20 02:04:45| Flops: 375737856
|2025-01-20 02:04:45| Params: 363345
|2025-01-20 02:04:45| Inference time: 0.71 ms
|2025-01-20 02:04:46| ********************Experiment Success********************
```

