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
    
    arr = diff(files[0], files[1])
    
    assert arr[0] == '3'
    