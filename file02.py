def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    a =0
    for i in data:
        if i.isalpha():
            a+=1
        if i=='\n':
            a+=1
    return a
f=open('txt_file/data02.txt').read()
# Read data from file
print(main(f))

