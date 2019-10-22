#Given a list with characters of words, reverse the list on space characters
#https://www.youtube.com/watch?v=aotBpjJUqJo&t=945s


def reverse_string(arr):
    #Converts from array to string, splits string on spaces, reverses new list, converts list back to string with spaces, converts string to character list
    #In my opinion too many steps, but it's a one liner
    return list(' '.join(''.join(arr).split()[::-1]))

def reverse_list(arr):
    return arr[::-1]

def reverse_string2(arr):
    #Reverses list and then reverses sub list
    arr = reverse_list(arr)
    start = 0
    for i in range(len(arr) + 1):
        if i == len(arr) or arr[i] == ' ':
            arr[start:i] = reverse_list(arr[start:i])
            start = i + 1
    return arr
print(reverse_string(['p','e','r','f','e','c','t',' ','m','a','k','e','s',' ','p','r','a','c','t','i','c','e']),'\n')
print(reverse_string(['a','b',' ','c',' ','d']),'\n')
print(reverse_string(['a','b']),'\n')
print(reverse_string(['a',' ','b',' ','c']),'\n')

print(reverse_string2(['p','e','r','f','e','c','t',' ','m','a','k','e','s',' ','p','r','a','c','t','i','c','e']),'\n')
print(reverse_string2(['a','b',' ','c',' ','d']),'\n')
print(reverse_string2(['a','b']),'\n')
print(reverse_string2(['a',' ','b',' ','c']),'\n')
