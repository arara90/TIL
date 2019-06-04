# Django Template Language

1. **반복문**

```html
<!--   for문이 몇 번 돌았는지?     -->
    {% for menu in menus %}
        <p> {{ forloop.counter }}, {{ menu }} </p>
    {% endfor%}
```

```
1, 족발 

2, 삼겹살 

3, 냉면 

4, 치맥 

5, 피자 

6, 양고기 

7, 다이어트!!!! 
```

2. **empty_list**

```
{% for user in empty_list %}
        <!--   for문이 몇 번 돌았는지?     -->
        <p>  {{ user }} </p>
    {% empty %}
        <p>현재 가입한 유저가 없습니다.</p>
    {% endfor%}
```

```
현재 가입한 유저가 없습니다.
```

3.**조건문**

```html
 <h1>2. 조건문</h1>
    {% if '피자' in menus %}
    <p<>피자는 파파존스!</p>
    {% endif%}

    <hr>

    {% for menu in menus %}
        <!--   for문이 몇 번 돌았는지?     -->
        <p> {{ forloop.counter }}번째 도는 중 ... </p>
        {% if forloop.first %}
            <p> 피자 + 파파존스</p>
        {%else%}
            <p> {{ menu }} </p>
        {%endif%}
    {% endfor%}
```

4. **Language Filter**

   ```html
       <h3>3. language filter 활용</h3>
       {% for message in messages %}
           {% if message|length > 5 %}
               <p>{{ message }}, {{ message|length }} => 글씨가 너무 길어요!</p>
           {% else %}
               <p>{{ message }}, {{ message|length }} </p>
           {% endif %}
       {% endfor %}
   ```

   ```
   apple, 5 
   
   banana, 6 => 글씨가 너무 길어요!
   
   mango, 5 
   ```

5. **lorem ipsum**

   ```html
   <h3>4. lorem ipsum</h3>
       {% lorem %} <br>
           <hr>
       {% lorem 3 %} <br>
           <hr>
       {% lorem 3 w %} <br>
           <hr>
       {% lorem 4 w random %} <br>
           <hr>
       {% lorem 2 p random %}
   ```

   ```
   Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. 
   ------
   Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Inventore veritatis praesentium voluptatum nemo sequi reprehenderit voluptate cumque voluptatibus quasi quaerat, fuga repudiandae atque ipsam nostrum eos hic deleniti culpa nesciunt, facilis alias numquam libero quaerat, architecto quisquam ipsa ullam sint debitis? Ratione culpa beatae ullam cumque facere eaque adipisci modi nostrum qui accusantium, voluptatum nulla iste consectetur voluptates similique. Fugit incidunt commodi odio dolorum ducimus dolore voluptatibus officiis a modi exercitationem, fugit earum fuga similique excepturi, ratione sapiente deleniti culpa, nihil ipsum facilis facere recusandae itaque veritatis quibusdam, illo cum repudiandae eligendi distinctio? Autem cumque optio voluptatem temporibus assumenda distinctio vel quae minima laboriosam quasi, alias reiciendis itaque corporis distinctio quidem, velit quia atque magnam sit beatae asperiores. Provident ab dicta libero amet optio exercitationem? 
   ------
   lorem ipsum dolor 
   ------
   perferendis quis minus vero 
   ------
   Corrupti velit excepturi praesentium porro laboriosam beatae iusto ab, optio dicta explicabo temporibus vero saepe.
   
   Dolores commodi beatae autem iusto dignissimos magnam eius magni rerum et, ipsam dignissimos praesentium quidem pariatur nam facilis?
   ```

6. **글자수 제한**

   ```html
   <h3>5. 글자수 제한 (truncate) </h3>
       <p> {{ my_sentence|truncatewords:3 }} </p>
       <p> {{ my_sentence|truncatechars:3 }} </p>
       <p> {{ my_sentence|truncatechars:10 }} </p>
   ```

   ```
   Life is short, … 
   Li… 
   Life is s… 
   ```

7.  **글자 관련 필터 (truncate)**

   ```html
   <p> {{ 'abc'|length }} </p>
       <p> {{ 'ABC'|lower }} </p>
       <p> {{ my_sentence|title }} </p>
       <p> {{ menus|random }} </p>
   ```

   ```
   3 
   abc 
   Life Is Short, You Need Python 
   치맥 
   ```

8. **연산** 

```
{{ 4|add:6 }} 
```

```
10 
```



9. **날짜 표현**

```html
    <p> 1) {{ datatimenow }} </p>
    <p> 2) {% now 'DATETIME_FORMAT' %} </p>
    <p> 3) {% now 'SHORT_DATETIME_FORMAT' %} </p>

    <p> 4) {% now 'DATE_FORMAT' %} </p>
    <p> 5) {% now 'SHORT_DATE_FORMAT' %} </p>
    <p> 6) {% now 'Y년 m월 d일 (D)' %} </p>
    <p> 7) {% now 'Y' as current_year %} Copyright {{ current_year }} </p>
    <p> 8) {{ datatimenow | date:'SHORT_DATE_FORMAT'}} </p>
```

```
1) 2019년 6월 3일 2:42 오후 
2) 2019년 6월 3일 2:42 오후 
3) 2019-6-3 14:42 
4) 2019년 6월 3일 
5) 2019-6-3. 
6) 2019년 06월 03일 (월요일) 
7) Copyright 2019 
8) 2019-6-3. 
```

+ python의 날짜 표현 : <https://minus31.github.io/2018/07/28/python-date/>

  

10. **기타**

```html
    <h3> 9. 기타 </h3>
    <!-- google.com 링크 -->
	{{ 'google.com'|urlize }}
	
```

