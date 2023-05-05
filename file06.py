def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    a = data.split('\n')
    n = []
    for i in a:

        n.append(len(i))
    return n
# Read data from file
f = open('txt_file/data06.txt').read()
print(main(f))