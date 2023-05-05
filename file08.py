def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    a = []
    for i in data:
        if i.isdigit():
            a.append(int(i))
    return max(a)
# Read data from file
f = open('data08.txt').read()
print(main(f))