# 193. Valid Phone Numbers

# Read from the file file.txt and output all valid phone numbers to stdout.
grep -E '^(\([0-9]{3}\) [0-9]{3}-[0-9]{4}|[0-9]{3}-[0-9]{3}-[0-9]{4})$' file.txt

# Notes:
# -E use extended regex
# ^ match entire line
# $ terminate after this point exactly
# \ treat following char e.g. ( as a character, not as a special command

# First format: \([0-9]{3}\) [0-9]{3}-[0-9]{4}
    # \( , 3 occurrences of a digit, \) , 3 occurrences of a digit, - , 4 occurrences of a digit
# Second format: [0-9]{3}-[0-9]{3}-[0-9]{4}
    # 3 occurrences of a digit, - , 3 occurrences of a digit, - , 4  occurrences of a digit
