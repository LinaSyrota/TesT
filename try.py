import re
with open('test_file.txt', 'r') as file:
    text = file.read()
    words = re.split('[,:; ]+', text)
    num_words = len(words)
    print(num_words)

