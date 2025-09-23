# Let's take the first word and its length
# we compare it with the rest elements. Whenever they dont match
# we subtract 1 from length and update first = first[0:length]
# if our length == 0, we return "" because no common prefix is found
def longestCommonPrefix(array):
    if len(array):
        return ""
    first = array[0]
    length = len(first)
    for i in array[1:]:
        while first != i[0:length]:
            length -= 1
            if length == 0:
                return ""
            first = first[0:length]
    return first


print(longestCommonPrefix(['flower', 'flight']))
print(longestCommonPrefix(['apple', 'ape', 'apricot']))
