python hash_tables.py \
        --probe_type linear \
        --hash_type rolling \
        --table_size 10000 \
        --key_file random_words.txt \
        --number_of_keys 10000 | \
	grep search | \
	python scatter.py search_time_linear_hash_rolling_random load_factor search_time
