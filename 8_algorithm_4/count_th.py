def count_th(word):
    if word.find("th") == -1:#base case -> stop when there is no more 'th' in the string
        return 0
    else:
        check = word.find("th") #find the index of first occurence of 'th'
        new_word = word[check+2:] #Slice the string at index found, add 2 so the 'th' is removed
        return 1 + count_th(new_word) #Return 1 for successful finds and call the function to complete the traversing the string. 
