# coding : utf-8
# Author : yuxiang Zeng
import os
import ast
import argparse
from pprint import pprint, pformat
import yaml



def get_config(Config='TestConfig'):
    import argparse
    from utils.config import load_config, update_config_from_args
    parser = argparse.ArgumentParser()
    parser.add_argument('--config_path', type=str, default='exper_config.py')
    parser.add_argument('--exp_name', type=str, default=Config)
    args, unknown_args = parser.parse_known_args()
    args = load_config(args.config_path, args.exp_name)
    args = update_config_from_args(args, unknown_args)
    return args



def load_config(file_path, class_name):
    import importlib.util
    import sys
    spec = importlib.util.spec_from_file_location("module.name", file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules["module.name"] = module
    spec.loader.exec_module(module)
    config = getattr(module, class_name)()
    return config


def update_config_from_args(config, args):
    from dataclasses import fields
    it = iter(args)
    for arg in it:
        if arg.startswith("--"):
            if "=" in arg:
                key, value = arg[2:].split("=")
            else:
                key = arg[2:]
                value = next(it)

            # Try to find the field in the config dataclass
            field_type = next((f.type for f in fields(config) if f.name == key), str)
            if field_type == bool:
                value = value.lower() in ['true', '1', 'yes']
            else:
                value = field_type(value)
            setattr(config, key, value)
    return config