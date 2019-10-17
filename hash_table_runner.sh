python hash_tables.py \
        --probe_type linear \
        --hash_type rolling \
        --table_size 10000 \
        --key_file nonrandom_words.txt \
        --number_of_keys 10000 | \
	grep hash_and_slot | \
	python scatter.py collisions_rolling_nonrandom word_number hash_value
