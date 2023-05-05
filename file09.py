def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    a = []
    for i in data:
        if i.isdigit():
            a.append(int(i)) 
    return min(a)
# Read data from file
f = open('txt_file/data09.txt').read()
print(main(f))
