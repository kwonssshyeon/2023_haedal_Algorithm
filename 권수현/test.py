l = ["A", "B", "C"]
r = []
for i in range(1, 1 << len(l)):
    tmp = ""
    for j in range(len(l)):
        
        if (i & 1 << j) != 0:
            tmp += l[j]
    r.append(tmp)
print(r)