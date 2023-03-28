import re

#file = open('test_file.txt').read()
 
def words(text):
    # text = file.read()
    words = re.split('[,:; ]+', text)
    num_words = len(words)
    print(num_words)

def sentence(text):
    sentences = re.split('[.!?]+', text)
    num_s = len(sentences)
    print(num_s)
    
file = open('test_file.txt').read()
words(file)
sentence(file)