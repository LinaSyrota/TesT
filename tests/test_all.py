import pytest
from main import diff

@pytest.fixture()
def createFiles():
    file1 = open('file_1.txt').read()
    file2 = open('file_2.txt').read()
    Same = open('same.txt', 'w')
    Diff = open('diff.txt', 'w')
    
    return file1, file2, Same, Diff


def test_diff(createFiles):
    files = createFiles
    
    for line1 in files[0]:
        same = False
        for line2 in files[1]:
            if line1 == line2:
                same = True
        
        if not same:
            diff_line = line1
    
    assert diff_line == '3'