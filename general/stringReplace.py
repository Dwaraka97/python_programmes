def strReplace():
    st = 'india is a democratic country,india has second highest population in the world,india is traditional country'
    string = st[5:]
    str1 = st[0:6]
    string = str.replace('india', 'indian', 1)
    st = str1 + string
    print(st)


strReplace()
