#1.open()
f = open('mulcam.txt', 'w')
for i in range(10):
    f.write('Hello, Mulcam\n')

with open('mulcam.txt', 'w') as f :
    f.writelines(['1\n', '2\n', '3\n'])

# \n : 개행문자
# \t : tab
# \\ : 역슬래쉬
# \' : 따옴표
# \" : 쌍따옴표