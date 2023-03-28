file1 = open('file_1.txt').read()
file2 = open('file_2.txt').read()
Same = open('same.txt', 'w')
Diff = open('diff.txt', 'w')

def same(text1, text2):
    for line1 in text1:
        for line2 in text2:
            if line1 == line2:
                Same.write(line1)
    
    Same.close()
                
def diff(text1, text2):
    for line1 in text1:
        same = False
        for line2 in text2:
            if line1 == line2:
                same = True
        
        if not same:
            Diff.write(line1)
    
    Diff.close()

same(file1, file2)
diff(file1, file2)