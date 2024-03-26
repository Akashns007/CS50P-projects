d={}
while(True):
    try:
        item = input().upper()
    except EOFError:
        print()
        break
    if item  in d:
        d[item]=d[item]+1
    else:
        d[item]=1
for item in sorted(d):
    print(d.get(item),item)