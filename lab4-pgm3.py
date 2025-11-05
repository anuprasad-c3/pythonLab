def compare(s1,s2,n):
    return s1[:n] == s2[:2]
s1 = input("Enter first string :")
s2 = input("Enter second string :")
n = int(input("Enter number of characters to compare :"))
print("Reslt :",compare(s1,s2,n))
