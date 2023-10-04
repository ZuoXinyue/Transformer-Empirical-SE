data_dir=../data_alter
mkdir -p ./saved_models/
mkdir -p ./stats_test/files
python run.py \
        --do_train \
        --do_eval \
        --do_test \
        --model_type roberta \
        --model_name_or_path microsoft/codebert-base \
        --train_filename $data_dir/train.bugfix.buggy,$data_dir/train.bugfix.fixed \
        --dev_filename $data_dir/valid.bugfix.buggy,$data_dir/valid.bugfix.fixed \
        --test_filename $data_dir/test.bugfix.buggy,$data_dir/test.bugfix.fixed \
        --output_dir ./saved_models/ \
        --max_source_length 256 \
        --max_target_length 256 \
        --beam_size 5 \
        --train_batch_size 44 \
        --eval_batch_size 44 \
        --learning_rate 5e-5 \
        --num_train_epochs 30 \
        2>&1 | tee ./saved_models/train.log