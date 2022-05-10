# -*- coding: utf-8 -*- 
"""
Created on Tue Feb 15 20:23:47 2022

@author: kcruz29
"""
#Kevin Cruz
#CS 113
#2/15/22
#Project 1


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def c_encrypt(msg, number):
    
    '''
    This function takes two parameters / arguments, which is a string, and 
    integer. If the first parameter / argument is all lowercase, all uppercase,
    or a mixture of both, the string will be all uppercase in the end. Based on
    the integer given in the second argument / parameter, thats how much the
    string's value will shift from either the left or right depending if the 
    number is positive or negative     
    '''
    
    newstring = ""
    
    for letter in msg:
        
        #Everytime the for loop repeats the characters in msg go into letter one
        #by one
        
        new_index = (alphabet.find(letter.upper()))
        
        #new_index finds the index number of each character in letter within
        #msg. This also capitalizes the letters
        
        if new_index != -1:
            
            #The if statement is used to make sure it only changes letters
            #within the argument. Anything that gives a value of -1 such as an
            #exlamation mark will be ignored
            
            index = new_index + number
            
            #index takes the index number from new_index and adds that with the 
            #second argument.
            
            newstring = newstring + (alphabet[index % 26])
            
            #newstring in the beginning has no content, but as the for loop
            #continues to loop, it adds the characters in letter using its index
            #number to find its location in the alphabet.
            
        
        else:
            newstring = newstring + letter
            #used to just add anything else that is not a letter such as "!, ?, 
            # :, etc"
    return newstring

def c_decrypt(msg, number):
    
    '''
    This function takes two parameters / arguments, which is a string, and 
    integer. If the first parameter / argument is all lowercase, all uppercase,
    or a mixture of both, the string will be all uppercase in the end. Based on
    the integer given in the second argument / parameter, thats how much the
    string's value will shift from either the left or right depending if the 
    number is positive or negative     
    '''
    
    newstring = ""
    
    for letter in msg:
        
        #Everytime the for loop repeats the characters in msg go into letter one
        #by one
        
        new_index = (alphabet.find(letter.upper()))
        
        #new_index finds the index number of each character in letter within
        #msg. This also capitalizes the letters
        
        if new_index != -1:
            
            #The if statement is used to make sure it only changes letters
            #within the argument. Anything that gives a value of -1 such as an
            #exlamation mark will be ignored
            
            index = new_index - number
            
            #index takes the index number from new_index and subtracts that 
            #with the second argument.
            
            newstring = newstring + (alphabet[index % 26])
            
            #newstring in the beginning has no content, but as the for loop
            #continues to loop, it adds the characters in letter using its index
            #number to find its location in the alphabet.
        else:
            newstring = newstring + letter
            #used to just add anything else that is not a letter such as "!, ?, 
            # :, etc"
    return newstring

def vig_encrypt(orig_str, encr_str):
    
    '''
    Index number from first argument is changed based on the index number in
    the second argument. Both arguments index numbers are added or subtracted 
    to return a new string
    '''
    
    newstring = ""
    
    increment = 0
    
    #increment is used to go through each letter in orig_str
    
    encr_str_wrap = 0
    
    #encr_str_wrap is used to wrap around encr_str when the for loop goes past 
    #it's range.
    
    for letter in orig_str:
        
        #The for loop will take each letter from orig_str everytime it loops
        #again.
        
        index = alphabet.find(letter.upper())
        
        #index is used to find the index number of letters passed in the for
        #loop 
        
        if index != -1:
            
            #The if statement is used to make sure it only changes letters
            #within the argument. Anything that gives a value of -1 such as an
            #exclamation mark will be ignored
            
            encr_letter = encr_str[encr_str_wrap]
            
            #Goes through each letter in encr_string, which gives the letter of
            #index
            
            new_index = alphabet.find(encr_letter)
            
            #Finds the index number from encr_letter
            
            index = index + new_index
            
            #Finds letters in the first argument and adds that index with new 
            #index
            
            newstring = newstring + (alphabet[index % 26])
            
            #Finds the letter of the index number from index and adds each
            #letter that goes through the for loop
            
            increment = increment + 1
            
            #This is used to add to increments to continue the for loop until 
            #every letter in orig_str is passed into the for loop
            
            encr_str_wrap = increment % len(encr_str)
            
            #Wrap function to go back to the beginning of encr_str whenever it
            #goes past it's range
            
        else:
            
            newstring = newstring + letter
            
            #used to just add anything else that is not a letter such as "!, ?, 
            # :, etc"
            
    return newstring

def vig_decrypt(orig_str, encr_str):
    
    '''
    Index number from first argument is changed based on the index number in
    the second argument. Both arguments index numbers are added or subtracted 
    to return a new string
    '''
    
    newstring = ""
    
    increment = 0
    
    #increment is used to go through each letter in orig_str
    
    encr_str_wrap = 0
    
    #encr_str_wrap is used to wrap around encr_str when the for loop goes past 
    #it's range.
    
    for letter in orig_str:
        
        #The for loop will take each letter from orig_str everytime it loops
        #again.
        
        index = alphabet.find(letter.upper())
        
        #index is used to find the index number of letters passed in the for
        #loop 
        
        if index != -1:
            
            #The if statement is used to make sure it only changes letters
            #within the argument. Anything that gives a value of -1 such as an
            #exlamation mark will be ignored
            
            encr_letter = encr_str[encr_str_wrap]
            
            #Goes through each letter in encr_string, which gives the letter of
            #index
            
            new_index = alphabet.find(encr_letter)
            
            #Finds the index number from encr_letter
            
            index = index - new_index
            
            #Finds letters in the first argument and subtracts that index with new 
            #index
            
            newstring = newstring + (alphabet[index % 26])
            
            #Finds the letter of the index number from index and adds each
            #letter that goes through the for loop
            
            increment = increment + 1
            
            #This is used to add to increments to continue the for loop until 
            #every letter in orig_str is passed into the for loop
            
            encr_str_wrap = increment % len(encr_str)
            
            #Wrap function to go back to the beginning of encr_str whenever it
            #goes past it's range
            
        else:
            
            newstring = newstring + letter
            
            #used to just add anything else that is not a letter such as "!, ?, 
            # :, etc"
            
    return newstring
            
            