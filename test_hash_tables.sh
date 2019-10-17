test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest

. ssshtest

rm -f add_test.png
rm -f search_test.png

# Make a list of nonrandom (patterned) words
bash nonrandom_wordcreator.sh

# Test to make sure nonrandom words will generate no error code
run hash_tables_nonrandom_words python hash_tables.py \
	--probe_type linear \
	--hash_type ascii \
	--table_size 1000 \
	--key_file nonrandom_words.txt \
	--number_of_keys 1000

assert_exit_code 0

# Test to make sure that scatter.py will read stdin from hash_tables.py
# And create a plot, with no exit code
run hash_tables_nonrandom_words_graphing python hash_tables.py \
	--probe_type linear \
	--hash_type ascii \
	--table_size 1000 \
	--key_file nonrandom_words.txt \
	--number_of_keys 1000 | \
	grep add_time | python scatter.py "add_test.png" "load_factor" "time"

assert_exit_code 0

# Test to make sure search function can feed into scatter.py
run hash_tables_nonrandom_words_graphing python hash_tables.py \
	--probe_type linear \
	--hash_type ascii \
	--table_size 1000 \
	--key_file nonrandom_words.txt \
	--number_of_keys 1000 | \
	grep search | python scatter.py "search_test.png" "time" "value"

assert_exit_code 0

python random_wordcreator.py > random_words.txt
# Test to make sure random words of a random length between 1 and 30 will
# Not result in an error code
run hash_tables_random_words_graphing python hash_tables.py \
	--probe_type linear \
	--hash_type ascii \
	--table_size 1000 \
	--key_file random_words.txt \
	--number_of_keys 1000 | \
	grep add_time | python scatter.py "add_test.png" "time" "value"

# If there is no print message, we know the plot was created successfully
assert_exit_code 0

# Test to make sure random words of a random length between 1 and 30 will
# Not result in an error code
run hash_tables_random_words_rolling_graphing python hash_tables.py \
	--probe_type linear \
	--hash_type rolling \
	--table_size 1000 \
	--key_file random_words.txt \
	--number_of_keys 1000 | \
	grep add_time | python scatter.py "add_test.png" "time" "value"
# If there is no error message, we know the plot was created successfully
assert_exit_code 0

# If we feed scatter.py non_number entries, it should raise an error

run scatter_error_testing echo "foo bar tar" | python scatter.py "error" "time" "test"

# ssshtest is having issues calling error codes from python, so I check them through bash
assert_equal $(echo $?) 1

# If it is empty, we should exit without making a file
run scatter_error_testing echo "" | python scatter.py "error" "time" "test"

# ssshtest is having issues calling error codes from python, so I check them through bash
assert_equal $(echo $?) 1


# Test whether Chained Hash option will run with both ascii and rolling
# Hash strategies
run hash_tables_random_words_rolling_graphing python hash_tables.py \
        --probe_type chained \
        --hash_type rolling \
        --table_size 1000 \
        --key_file random_words.txt \
        --number_of_keys 1000 | \
        grep add_time | python scatter.py "add_test.png" "time" "value"

assert_exit_code 0

run hash_tables_random_words_rolling_graphing python hash_tables.py \
        --probe_type chained \
        --hash_type ascii \
        --table_size 1000 \
        --key_file random_words.txt \
        --number_of_keys 1000 | \
        grep add_time | python scatter.py "add_test.png" "time" "value"

assert_exit_code 0
