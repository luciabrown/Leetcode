# 192. Word Frequency

# Read from the file words.txt and output the word frequency list to stdout.
tr -cs '[:alnum:]' '[\n*]' < words.txt | sort | uniq -c | sort -nr | awk '{print $2, $1}'

# Notes:
# tr -cs '[:alnum:]' '[\n*]' replace non alphanumerics with a newline in words.txt
# sort words alphabetically
# uniq -c count repeated words
# sort -nr sort by frequency
# awk '{print $2, $1}' flip the parameters of uniq -c such that the word appears first then the frequency
