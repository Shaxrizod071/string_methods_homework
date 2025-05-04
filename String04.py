
def main(s):
    """
    A variable of type str is given. make sure all letters are lowercase.
    Args:
        s: str
    Returns:
        bool: answer
    """
   
    if s in s.lower():
        return True
    return False
print(main('fififwf'))
