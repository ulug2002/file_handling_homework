def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """

# Read data from file
    list=[]
    for i in data:
        if i.isdigit():

         list.append(int(i))
    return list
    
f=open('txt_file/data01.txt').read()
print(main(f))