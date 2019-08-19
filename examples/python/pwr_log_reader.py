f = open('pwr.log', 'r')
lines = f.readlines()
f.close()

for i in range(len(lines)):
    if "BURNUP   K-INF" in lines[i]:
        break
    
print(i)
