def main(s):
    """
    A str of several words is given. All letters are lowercase. Make sure that the first letter of each word is capitalized.
    Args:
        s: str
    Returns:
        str: answer
    """
    if s.lower():
        return s.capitalize()
    else:
        return s.lower() 
print(main('dedaK'))
