rm -f nonrandom_words.txt

for i in {1..10000}; do
	echo "sample$i" >> nonrandom_words.txt
done

