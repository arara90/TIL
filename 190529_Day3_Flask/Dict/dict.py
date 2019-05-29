lunch = {'중국집': '02-1'
         , '양식': '02-2'
         , '냉면집': '02-3'
         }

#2.추가
lunch['분식집'] = '054-'

lunch = {
    '한식집' : {
        '고갯마루' : '02-4',
        '순남시래기': '031-'
    }
}

lunch['한식집']
#print(lunch['한식집']['고갯마루'])

#추가. dict 내부 자료형
# key = str, integer,float,boolean
# value = 모든 자료형

# 4.딕셔너리 반복문 활용
lunch = {'중국집': '02-1'
         , '양식': '02-2'
         , '냉면집': '02-3'
         }

for k in lunch :
    print(k, lunch[k])
    print(type(k))

print('#########key##########')
for k in lunch.keys():
    print(k, lunch[k])
    print(type(k))
print('##########value#########')
for v in lunch.values():
    print(v)
    print(type(v))
print('##########items#########')
for k,v in lunch.items():
    print(k,v)
    print(type(k),type(v))

