import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {} #This is an empty dictionary. We will add key-value pairs to this dictionary with the help of the following lines of code (The for-loop and its code block).

for character in message: #The loop will run for the number of single characters (Each letter & each space between the words are characters) in the string assigned to 'message'.
                          #That means the loop will run for 73 times.
                          #In each iteration of the loop, 'character' will be set to the current character of the string for the running iteration.
                          #That means the loop will start with 'I' and end with '.'(period). 'I' is the current character of the first iteration and '.' is the current character of the last iteration of the for-loop.

    count.setdefault(character, 0) #If the character assigned to 'character' is not in the 'count' dictionary, then the character will be added to the dictionary as a key with its value being set to 0.
    count[character] = count[character] + 1 #The value of the key (character added as key) of 'count' in the running iteration of the loop is incremented by one.
                                            #As a result of a key's value being incremented, we can track how many times a particular character in the string was iterated.
                                            #^It's because the existing value of the existing key will be incremented by 1 for the number of times the particular character is iterated.
                                            #The accuracy of exactly how many times a value should be incremented is ensured because already existing keys in the dictionary aren't updated with new values by set.default(), as it does so only if the key is missing in the dictionary. 

pprint.pprint(count) #Prints out the dictionary with all the key-value pairs added.
             #The key and its value in each key-value pair represent a specific character from the string assigned to 'message' and the number of times it's found in the string, respectively.
