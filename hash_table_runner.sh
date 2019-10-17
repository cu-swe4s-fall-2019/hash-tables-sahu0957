python hash_tables.py \
        --probe_type linear \
        --hash_type rolling \
        --table_size 10000 \
        --key_file nonrandom_words.txt \
        --number_of_keys 10000 | python scatter.py add_time_linear_probe_rolling_nonrandom load_factor add_time
