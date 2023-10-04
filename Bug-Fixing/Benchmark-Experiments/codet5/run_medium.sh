mkdir -p ./saved_models/medium/cache_data
mkdir -p ./saved_models/medium/prediction
mkdir -p ./stats_test/files
python run_gen.py    \
    --do_train \
    --do_eval \
    --do_eval_bleu \
    --do_test  \
    --save_last_checkpoints \
    --always_save_model   \
    --task refine \
    --sub_task medium \
    --model_type codet5 \
    --data_num -1    \
    --num_train_epochs 50 \
    --warmup_steps 1000 \
    --learning_rate 5e-5 \
    --patience 5   \
    --tokenizer_name=Salesforce/codet5-base \
    --tokenizer_path=../../../CodeT5/tokenizer/salesforce   \
    --model_name_or_path=Salesforce/codet5-base \
    --output_dir saved_models/medium/  \
    --summary_dir tensorboard   \
    --data_dir ../data/  \
    --cache_path saved_models/medium/cache_data \
    --res_dir saved_models/medium/prediction \
    --res_fn saved_models/medium/refine_codet5_base.txt   \
    --train_batch_size 4 \
    --eval_batch_size 2 \
    --max_source_length 240 \
    --max_target_length 240 \
    --gradient_accumulation_steps 2 \
    2>&1 | tee saved_models/medium/train.log
