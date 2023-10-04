import sys, os, re
import json
import numpy as np
import random
import math

def generate_files(records, dest_num, save_file_name):
    count = len(records)

    full_indices = []

    for i in range(dest_num//count):
        sample_indexes = np.random.choice(
            count,
            count,
            replace=False
        )
        full_indices.extend(sample_indexes)
    
    sample_indexes = np.random.choice(
        count,
        dest_num - count*(dest_num//count),
        replace=False
    )
    full_indices.extend(sample_indexes)

    random.shuffle(full_indices)

    sample_records = []
    for sample_index in full_indices:
        sample_record = records[sample_index]
        sample_records.append(sample_record)
    print(len(sample_records), dest_num)
    assert len(sample_records) == dest_num

    with open(save_file_name, "w") as f:
        for record in sample_records:
            f.write(json.dumps(record) + "\n")

    print("Sampled {} records from {} original records.".format(
        dest_num,
        count
    ))

with open("./train_ori.jsonl") as f:
    records_train = [json.loads(x) for x in f]
generate_files(records_train, 1953940, "./train_ori_sampled.jsonl")

with open("./valid_ori.jsonl") as f:
    records_valid = [json.loads(x) for x in f]
generate_files(records_valid, 104273, "./valid_ori_sampled.jsonl")

with open("./test_ori.jsonl") as f:
    records_test = [json.loads(x) for x in f]
generate_files(records_test, 90908, "./test_ori_sampled.jsonl")