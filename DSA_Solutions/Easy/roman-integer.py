# we loop through each element in our string
# If current value is smaller than the next one
# we subtract it from our result else we add it
def romanToInt(x):
    result = 0
    romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for i in range(len(x)):
        if i < len(x)-1 and romans[x[i]] < romans[x[i+1]]:
            result -= romans[x[i]]
        else:
            result += romans[x[i]]
    print(result)


romanToInt("MCDLII")
romanToInt("III")
romanToInt("LVI")
