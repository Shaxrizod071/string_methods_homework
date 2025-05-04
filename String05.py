import string
def main(s):
    """
    A str of several words is given. Return the variable capitalized.
    Args:
        s: str
    Returns:
        str: answer
    """
    jkl=string.ascii_letters 
    a=''
    for i in s:
       if i in jkl:
           a+=i
    return a.capitalize()
print(main('hgigKGKG'))

