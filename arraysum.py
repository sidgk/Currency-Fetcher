def check(my_string):  #my_string is local (namespace is also local) to check
    brackets = ['()', '{}', '[]'] 
    while any(x in my_string for x in brackets):
        print(my_string) 
        for br in brackets: 
            my_string = my_string.replace(br, '') 
    return not my_string 

my_string1='({})'
print(check( my_string1)) # this does not modify my_string of line 9
print(my_string1)
