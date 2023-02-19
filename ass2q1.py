#Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples



def a(z):
    return sorted(z, key=lambda x: x[-1])

z = [(1,9), (2,8), (3,7),(4,6),(5,0)]
a = a(z)
print(a)
