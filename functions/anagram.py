def anagram(s1, s2):
    print(sorted(s1))
    if sorted(s1)==sorted(s2):
        return "Anagram"
    else:
        return "Not Anagram"


s1 = input("Enter first name: ")
s2 = input("Enter second name: ")
print(anagram(s1, s2))
