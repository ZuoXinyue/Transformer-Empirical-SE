import sys, os, re
import json
import numpy as np
import math

def generate_files(records, sample_ratio, save_file_name):
    count = len(records)
    sample_count = math.ceil(count * sample_ratio)

    sample_indexes = np.random.choice(
        count,
        sample_count,
        replace=False
    )

    sample_records = []
    for sample_index in sample_indexes:
        sample_record = records[sample_index]
        sample_records.append(sample_record)

    assert len(sample_records) == sample_count

    with open(save_file_name, "w") as f:
        for record in sample_records:
            f.write(json.dumps(record) + "\n")

    print("Sampled {} records from {} original records.".format(
        sample_count,
        count
    ))

with open("./train_alt.jsonl") as f:
    records_train = [json.loads(x) for x in f]
generate_files(records_train, 0.04, "./train_alt_sampled.jsonl")

with open("./valid_alt.jsonl") as f:
    records_valid = [json.loads(x) for x in f]
generate_files(records_valid, 0.025, "./valid_alt_sampled.jsonl")

with open("./test_alt.jsonl") as f:
    records_test = [json.loads(x) for x in f]
generate_files(records_test, 0.06, "./test_alt_sampled.jsonl")

with open("./train_ori.jsonl") as f:
    records_train = [json.loads(x) for x in f]
generate_files(records_train, 0.5, "./train_ori_sampled.jsonl")

with open("./valid_ori.jsonl") as f:
    records_valid = [json.loads(x) for x in f]
generate_files(records_valid, 0.5, "./valid_ori_sampled.jsonl")

with open("./test_ori.jsonl") as f:
    records_test = [json.loads(x) for x in f]
generate_files(records_test, 0.5, "./test_ori_sampled.jsonl")