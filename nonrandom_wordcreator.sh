rm -f nonrandom_words.txt

for i in {1..1000}; do
	echo "sample$i" >> nonrandom_words.txt
done

