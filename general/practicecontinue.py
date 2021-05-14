name="python"
count=(len(name))
i=0
while count >0:
    if(name[i] == 'o'):
        count -=1
        continue
    print(f"{name[i]}",end=' ')
    i += 1
    count -=1