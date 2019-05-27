a = '123'
new_q = f'{a}'


f'%s %s' % ('one', 'two')

#pyformat
'{} {}'.format('one', 'two')

#f-string
a,b = 'one', 'two'
f'{a} {b}'

#example
name = '홍길동'
eng_name = "Hong Gil dong"

print('안녕하세요, {1} 입니다. My name is {0}'.format(name, eng_name))
print(f'안녕하세요, {name}입니다.')



