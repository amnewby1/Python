def frequency_map(coll):
    frequencies = {}
    for digit in coll:
        frequencies[digit] = frequencies.get(digit, 0)+1
    return frequencies

def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    return frequency_map(str(num1))==frequency_map(str(num2))
    