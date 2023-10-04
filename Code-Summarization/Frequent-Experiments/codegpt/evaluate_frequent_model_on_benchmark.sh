lang=java #programming language
python run.py \
        --do_test \
        --model_type gpt2 \
        --model_name_or_path microsoft/CodeGPT-small-java-adaptedGPT2 \
        --load_model_path ./saved_models/$lang/checkpoint-last/pytorch_model.bin \
        --train_filename ../dataset_codesum/$lang/train.jsonl \
        --dev_filename ../dataset_codesum/$lang/valid.jsonl \
        --test_filename ../dataset_ori/$lang/test.jsonl \
        --output_dir ./saved_models/$lang/ \
        --max_source_length 256 \
        --max_target_length 128 \
        --beam_size 11 \
        --train_batch_size 8 \
        --eval_batch_size 8 \
        --learning_rate 5e-5 \
        --num_train_epochs 10 \
        # 2>&1 | tee ./saved_models/$lang/test.log
