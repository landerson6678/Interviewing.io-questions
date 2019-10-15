#regex programming challenge
#Goal given a string and pattern that can include a specific character,any character, and 0 or more possibilities, determine if string matches regex
#Constraints (not tested on in video): I need to implement a recurssive lookahead so that tricky patterns
#like .*.*n will not return false seeing .* can be 0 or many of any character

#Limitations of python: cannot use for statement because we are manipulating both the index of the string and the index of the regex, this adds a couple of uneeded increment lines


def is_match(character,regex):
    return regex in (character + '.')

def last_index(str,regex):
    if len(regex) > 1 and regex[1] == '*':
        return last_index(str,regex[2:] if 2 < len(regex) else '')
    if len(regex) > 0:
            return last_index(str,regex[1:]) if regex[0] == '.' else str.rfind(regex[0])
    return -1

def regex_match(str,regex):
    i , index = 0 , 0
    while index < len(regex):
        if index + 1 < len(regex) and regex[index + 1] == '*':
            exit = last_index(str,regex[index + 2:] if index + 2 < len(regex) else '')
            while i < len(str) and is_match(str[i],regex[index]) and i != exit:
                i += 1
            index += 2
        elif i >= len(str) or not is_match(str[i],regex[index]):
            return False
        else:
            i += 1
            index += 1
    return i == len(str) and index == len(regex)

#Basic regex tests
print(regex_match('ab','ab')) #True
print(regex_match('aba','ab.')) #True
print(regex_match('aba','a.*')) #True
print(regex_match('aaa','.*a')) #True
print('')
print(regex_match('ab','b')) #False
print(regex_match('ab','ab.')) #False
print(regex_match('aba','a.*b')) #False
print(regex_match('aaa','.aa.')) #False
print('')

#advanced regex tests
print(regex_match('aba','a.*b*')) #True
print(regex_match('testing','te.*.*.*')) #True
print(regex_match('testing','te.*.*ngg*')) #True
