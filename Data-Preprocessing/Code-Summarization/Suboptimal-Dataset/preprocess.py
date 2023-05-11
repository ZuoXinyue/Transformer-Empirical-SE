import functools
import os
import tensorflow.compat.v1 as tf
import tensorflow_datasets as tfds
import pandas as pd
import json

nq_tsv_path_comment = {
    "train": "./training.tsv",
    "validation": "./eval.tsv",
    "test": "./test.tsv"
}

def read_tsv_file(split):
    file_path = nq_tsv_path_comment[split]
    data=pd.read_csv(file_path, sep='\t', header=None)
    print(data.shape)
    data.columns = ["code", "doc_string"]
    print(data.iloc[0])
    print(data.iloc[0]["code"])
    return data

train_df = read_tsv_file("train")
valid_df = read_tsv_file("validation")
test_df = read_tsv_file("test")

def output_jsonl(df, output_path):
    with open(output_path, 'a+', encoding='utf-8') as f:
        for index, row in df.iterrows():
            # print(row)
            code = row["code"]
            doc_string = row["doc_string"]
            code_tokens = code.split()
            doc_string_tokens = doc_string.split()
            json_string = {"code": code, "docstring": doc_string, "code_tokens": code_tokens, "docstring_tokens": doc_string_tokens}
            json_record = json.dumps(json_string, ensure_ascii=False)
            f.write(json_record + '\n')

output_jsonl(train_df, "./train.jsonl")
output_jsonl(valid_df, "./valid.jsonl")
output_jsonl(test_df, "./test.jsonl")