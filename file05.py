def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    a = 0
    for i in data:
        if i.isalpha():
            a +=1
        if i == '\n':
            a +=1
    n = 0
    for i in data:
        if i.isdigit():
            n +=1
    
    return [a,n]
    
# Read data from file
f = open('txt_file/data05.txt').read()
print(main(f))