#PIG Latin Problem
#if a word starts with a vovel add 'ay' at the end.
#if a word doesnt start with a vovel add the first letter to the end and add 'ay' after


def pigLatin(word):
    
    firstWord = word[0]
    
    #vovel check
    if firstWord in 'aeiou':
        pigWord = word + 'ay'
    else:
        pigWord = word[1:] + firstWord + 'ay'
    
    return pigWord


result = pigLatin(input("Enter the word :"))
print(result)