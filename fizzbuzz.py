import pytest

#ToDo:
# call fizzbuzz | passed
# return number passed to fizzbuzz | passed
# return fizz if number is divisable by 3 | passed
# return buzz if number is divisable by 5 | passed
# return fizzbuzz if number is divisable by both 3 and 5 | passed
# provide room for easily extending rules should be able to make numbers
#   divisable by 4 return augh easily for example | passed though subjective
# call function that calls fizzbuzz on any range on numbers
#   :assumed return value should be list | failed


def fizzbuzz(value: int) -> int | str:
    """creates variable word and returns the following based on conditions
        returns fizz if value is evenly divisable by 3
        returns buzz if value is evenly divisable by 5
        returns fizz buzz if value is evenly disable by both 3 and 5
    has room to easily be extended with more rules.
    """
    
    # wasn't specified that 0 returns fizz or buzz so I made sure it
    # wouldn't
    if value == 0:
        return 0
        

    word = ''

    fizz = value % 3 == 0
    if fizz:
        word += "fizz"
    
    buzz = value % 5 == 0
    if buzz:
        word += "buzz"
    

    if word:
        return word
    else:
        return value


def fizzbuzz_range(start: int, end: int) -> list: 
    """calls fizzbuzz on range of numbers and builds list from results
    ranges work like range functions. starts at start and ends at end 
    value -1"""

    return [fizzbuzz(x) for x in range(start,end)]

