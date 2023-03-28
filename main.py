file1 = open('file_1.txt').read()
file2 = open('file_2.txt').read()
Same = open('same.txt', 'w')
Diff = open('diff.txt', 'w')

def same(text1, text2):
    arr_same = []
    for line1 in text1:
        for line2 in text2:
            if line1 == line2:
                arr_same.append(line1)
                #Same.write(line1)
    
    return arr_same
                
def diff(text1, text2):
    arr_diff = []
    
    for line1 in text1:
        same = False
        for line2 in text2:
            if line1 == line2:
                same = True
        
        if not same:
            arr_diff.append(line1)
    
    return arr_diff
    #Diff.close()

def output(file, arr):
    for el in arr:
        file.write(el)   
    file.close()
    
arr1 = same(file1, file2)
arr2 = diff(file1, file2)

output(Same, arr1)
output(Diff, arr2)