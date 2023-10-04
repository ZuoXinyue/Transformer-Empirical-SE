lang=java #programming language
mkdir -p ./saved_models/$lang/
mkdir -p ./stats_test/files
python run.py \
        --do_train \
        --do_eval \
        --do_test \
        --model_type gpt2 \
        --model_name_or_path microsoft/CodeGPT-small-java-adaptedGPT2 \
        --train_filename ../dataset_mix/$lang/train.jsonl \
        --dev_filename ../dataset_mix/$lang/valid.jsonl \
        --test_filename ../dataset_mix/$lang/test.jsonl \
        --output_dir ./saved_models/$lang \
        --max_source_length 256 \
        --max_target_length 128 \
        --beam_size 10 \
        --train_batch_size 4 \
        --eval_batch_size 4 \
        --learning_rate 5e-5 \
        --num_train_epochs 10 \
        2>&1 | tee ./saved_models/$lang/train.log