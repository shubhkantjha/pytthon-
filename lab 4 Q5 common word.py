#common word
s1=input("enter first letter")
s2=input("enter second letter")
min_length = min(len(s1), len(s2))
for i in range(min_length):
    if s1[i] == s2[i]:
        print(s1[i])
    else:
        print("no common word")
        break;
