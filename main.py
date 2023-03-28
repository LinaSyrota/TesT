file1 = open('file_1.txt').read()
file2 = open('file_2.txt').read()
Same = open('same.txt', 'w')

def same(text1, text2):
    same = list()
    for line1 in text1:
        for line2 in text2:
            if line1 == line2:
                Same.write(line1)
                
same(file1, file2)