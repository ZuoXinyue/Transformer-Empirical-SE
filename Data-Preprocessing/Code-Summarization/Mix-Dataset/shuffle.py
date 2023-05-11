import sys, os, re
import json
import numpy as np
import math
import random

def shuffle_files(records, save_file_name):
    count = len(records)
    list_indexes = list(range(count))
    print(list_indexes[:5])
    random.shuffle(list_indexes)
    print(list_indexes[:5])

    shuffled_records = []
    for sample_index in list_indexes:
        sample_record = records[sample_index]
        shuffled_records.append(sample_record)

    assert len(shuffled_records) == count

    with open(save_file_name, "w") as f:
        for record in shuffled_records:
            f.write(json.dumps(record) + "\n")

    print("Shuffled {} records.".format(
        count
    ))

with open("./train_merged.jsonl") as f:
    records_train = [json.loads(x) for x in f]
shuffle_files(records_train, "./train.jsonl")

with open("./valid_merged.jsonl") as f:
    records_valid = [json.loads(x) for x in f]
shuffle_files(records_valid, "./valid.jsonl")

with open("./test_merged.jsonl") as f:
    records_test = [json.loads(x) for x in f]
shuffle_files(records_test, "./test.jsonl")