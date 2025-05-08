# The trickiest part of this challenge is to consider the last two stanzas "I've given below", of the song and apply our logic.

# "\n" refers to print the followup characters (e.g: strings, numbers, etc..) in a newline. 

# If you're stuck refer to the "For-Loops_Reference.png"

"""
1 bottle of beer on the wall, 1 bottle of beer.
Take one down and pass it around, no more bottles of beer on the wall.

No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the wall.

"""

for num in range (99,1,-1):
    print(f"{num} bottles of beer on the wall, {num} bottles of beer.\n Take one down and pass it around, {num-1} bottles of beer on the wall.\n") 

if num != 1:
    print(f"1 bottle of beer on the wall, 1 bottle of beer.\n Take one down and pass it around, no more bottles of beer on the wall.\n")
    print("No more bottles of beer on the wall, no more bottles of beer.\n Go to the store and buy some more, 99 bottles of beer on the wall.\n")