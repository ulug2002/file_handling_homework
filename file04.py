def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    lst = []
    for i in data:
        if i.isalpha():
            lst.append(i)
        if i =='\n':
            lst.append('\n')
    return lst
# Read data from file
f=open('txt_file/data04.txt').read()
print(main(f))