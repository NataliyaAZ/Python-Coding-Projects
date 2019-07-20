def remove_repeatedletters(string):
    new_string = ''
    for char in string:
        if not(char in new_string):
            new_string = new_string + char
    return (new_string)

string_result = remove_repeatedletters('drtyupfgtrrtytuuuebbttmdff')
print (string_result)