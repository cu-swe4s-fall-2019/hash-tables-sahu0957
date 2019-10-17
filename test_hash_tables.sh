test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest

. ssshtest

rm -f add_test.png

bash nonrandom_wordcreator.sh


run hash_tables_nonrandom_words python hash_tables.py \
	--probe_type linear \
	--hash_type ascii \
	--table_size 1000 \
	--key_file nonrandom_words.txt \
	--number_of_keys 1000

assert_exit_code 0


bash nonrandom_wordcreator.sh
run hash_tables_nonrandom_words_graphing python hash_tables.py \
	--probe_type linear \
	--hash_type ascii \
	--table_size 10000 \
	--key_file nonrandom_words.txt \
	--number_of_keys 10000 | \
	python scatter.py "add_test.png" "load_factor" "time"

assert_exit_code 0
