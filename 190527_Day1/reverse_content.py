#1. read file
with open('mulcam.txt', 'r') as f:
    lines = f.readlines()
    print(lines)
#2. reverse
lines.reverse()

#3. write file
with open('mulcam.txt', 'w') as f:
    f.writelines(lines)

