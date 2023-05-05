def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    x1=data.split('\n')
    x2=[]
    for i in x1:
        
        x2.append(len(i))
    return max(x2) 

print(main(open('txt_file/data10.txt').read()))