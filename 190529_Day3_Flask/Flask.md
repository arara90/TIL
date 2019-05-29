# Flask

* Python 이용

* 장고에 비해 경량화

* 웹 구조 학습을 위한 단계



1. 플라스크 서버 구동

   >  FLASK_APP=hello.py flask run



2. ```python
   @app.route("/xxx")  ## http://127.0.0.1:5000/xxxx 이렇게 뒤에 붙게될 주소 
   (요청주소)
   ```

   > ```python
   > @app.route("/ara")
   > def whoru():
   >     return "This is Ara!!!!"
   > ```
   >
   > 

3. **Debug 모드로 켜기 ( 실시간 개발 반영 )**

   > **FLASK_DEBUG=1** FLASK_APP=hello.py flask run

4. Flask run 대신에 서버 바로 켜기

   * python hello.py

   > ```
   > if __name__ == '__main__':
   >     app.run(debug=True)
   > ```

   * How? a를 b에서 실행하는 경우에는 main이 아니다. 하지만 a에서 실행하면 main

   > ```
   > ##a.py
   > print("여기는", __name__)
   > if __name__ == '__main__':
   >     print('main 입니다.')
   > ```

   > ```
   > ##b.py
   > import a
   > print('여기는 b')
   > ```

   * 실행결과?

   > $ python a.py
   >
   > \__main__
   > main 입니다.

   > $ python b.py
   > 여기는 a
   > 여기는 b

   * name은 파일의 시작점이라고 할 수 있다. import됐을 경우는 파일명. 시작점인 경우 \__main__

5. @? 데코레이터 , 라우트 함수

   * 함수를 인자로 받는 함수를 실행할때

     ```python
     def hello(func):
         print('hihi')
         func() #bye실행한것과 같음
         print('hihi')
     
     @hello
     def bye():
         print('bye bye')
     
     
     bye()
     
     ##결과
     ##hihi
     ##bye bye
     ##hihi
     ```

     

   * variable routing : 동적 주소 할당 : **@app.route('주소/변수')**

     ```python
     #pass variable routing
     @app.route('/greeting/<string:name>') #<string:name> 이 부분 변화 가능
     def greeting(name):
         return f'반갑습니다 {name}님! '
     
     #주소 : http://127.0.0.1:5000/greeting/ara
     #결과 : 반갑습니다 ara님! 
     ```

   * html 연결 및  변수 받기

     ```python
     @app.route('/html_file')
     def html_file():
        return render_template('index.html')
     
     @app.route('/hi/<string:name>')
     def hi(name):
        return render_template('hi.html', your_name=name)
     
     @app.route('/menulist')
     def menulist():
         menulist = ['Salad', 'Pizza', 'SundaeGukbab', 'F20', 'Gimbab', 'Toast', 'Yogurt', 'Tomatilo']
         return render_template('menulist.html', menu_list=menulist)
     
     ```

     ```html
     <!doctype html>
     <html lang="en">
     <head>
         <meta charset="UTF-8">
         <meta name="viewport"
               content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
         <meta http-equiv="X-UA-Compatible" content="ie=edge">
         <title>Document</title>
     </head>
     <body>
         {% for menu in menu_list %}
         <li>{{ menu }}</li>
         {% endfor %}
     </body>
     </html>
     ```

     