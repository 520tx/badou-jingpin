#-*-coding:utf-8-*-
'''
Author: Shiyao Ma
Date: 2023-09-24 14:52:54
LastEditors: Shiyao Ma
LastEditTime: 2023-09-24 15:18:52
Copyright (c) 2023 by Shiyao Ma, All Rights Reserved. 
'''
"""
配置参数信息
"""

Config = {
    "model_path": "model_output",
    "schema_path": "data/schema.json",
    "train_data_path": "data/train.txt",
    "valid_data_path": "data/test.txt",
    "vocab_path":"data/chars.txt",
    "max_length": 100,
    "hidden_size": 256,
    "num_layers": 2,
    "epoch": 20,
    "batch_size": 16,
    "optimizer": "adam",
    "learning_rate": 1e-4,
    "use_crf": False,
    "class_num": 9,
    "bert_path": r"/home/mashiyao/.cache/huggingface/hub/models--bert-base-chinese/snapshots/8d2a91f91cc38c96bb8b4556ba70c392f8d5ee55/"
}