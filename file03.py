def main(data:str):
    """
    The data is from the file. Return the numbers as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    lst = []
    for i in data:
        if i.isdigit():
            lst.append(i)
    return lst
# Read data from file
f=open('txt_file/data03.txt').read()
print(main(f))