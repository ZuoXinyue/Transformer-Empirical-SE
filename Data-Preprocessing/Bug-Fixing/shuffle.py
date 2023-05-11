import sys, os, re
import json
import numpy as np
import math
import random

def shuffle_files(records1, records2, save_file_name1, save_file_name2):
    count = len(records1)
    list_indexes = list(range(count))
    print(list_indexes[:5])
    random.shuffle(list_indexes)
    print(list_indexes[:5])

    shuffled_records1 = []
    shuffled_records2 = []
    for sample_index in list_indexes:
        sample_record1 = records1[sample_index]
        sample_record2 = records2[sample_index]
        shuffled_records1.append(sample_record1)
        shuffled_records2.append(sample_record2)

    assert len(shuffled_records1) == count
    assert len(shuffled_records2) == count

    with open(save_file_name1, "w") as f:
        for record in shuffled_records1:
            f.write(record)
    
    with open(save_file_name2, "w") as f:
        for record in shuffled_records2:
            f.write(record)

    print("Shuffled {} records.".format(
        count
    ))

with open("./bugfix.buggy") as buggy:
    records_buggy = [x for x in buggy]
    # print(records_buggy[:5])
with open("./bugfix.fixed") as fixed:
    records_fixed = [x for x in fixed]
shuffle_files(records_buggy, records_fixed, "./bugfix.buggy.shuffled", "./bugfix.fixed.shuffled")