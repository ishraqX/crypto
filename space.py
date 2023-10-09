import re
# Read the contents of the uploaded file
with open('thespace.txt', 'r') as file:
    thespace_contents = file.read()
# Displaying the first 1000 characters for a quick overview
print(thespace_contents[:1000])
# Splitting the contents on the $! delimiter
binary_sequences = thespace_contents.split('$!')

# Convert binary strings to ASCII characters
ascii_chars = [chr(int(binary_seq, 2)) for binary_seq in binary_sequences]

# Joining the characters to form the decoded message
decoded_message = ''.join(ascii_chars)
print(decoded_message)

# Searching for a broader pattern that might resemble a flag
potential_flags_broad = re.findall(r"\w+\{\w+\}", decoded_message)
print(potential_flags_broad)
