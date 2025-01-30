```python
|2025-01-19 23:49:56| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7c5f287cb620>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 1, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 32, 'record': True,
     'retrain': True, 'rounds': 5, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-19 23:49:56| ********************Experiment Start********************
|2025-01-20 00:01:14| Round=1 BestEpoch=250 Acc=0.9197 F1=0.8634 Precision=0.8738 Recall=0.8597 Training_time=567.9 s 

|2025-01-20 00:08:22| Round=2 BestEpoch=147 Acc=0.9200 F1=0.8684 Precision=0.8796 Recall=0.8648 Training_time=332.6 s 

|2025-01-20 00:16:38| Round=3 BestEpoch=172 Acc=0.9216 F1=0.8670 Precision=0.8810 Recall=0.8651 Training_time=395.8 s 

