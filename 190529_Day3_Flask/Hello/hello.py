from flask import Flask, render_template
import random
#시작점인지 검증하기 위해 Flask에서 내부적으로 구현해놓은 부분
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/ara")
def ara():
    return "This is Ara!!!!"


#pass variable routing
@app.route('/greeting/<string:name>') #<string:name> 이 부분 변화 가능
def greeting(name):
    return f'반갑습니다 {name}님! '

#주소 : http://127.0.0.1:5000/greeting/ara
#결과 : 반갑습니다 ara님!


@app.route('/cube/<int:num>')
def cube(num):
   res = num ** 3
   return f'{res}'     # ==str(res)


#<int:people>
import random as rand

@app.route('/lunch/<int:num>')
def lunch(num):
   lunch = ['Salad', 'Pizza', 'SundaeGukbab', 'F20', 'Gimbab','Toast','Yogurt','Tomatilo']
   res = random.sample(lunch, num)
   return str(res)

@app.route('/html')
def html():
    html_string = """
    <h1> This is H1 tag </h1>
    <h2> This is H2 tag </h2>
    <p> This is p tag </p>
"""
    return html_string

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



if __name__ == '__main__':
    app.run(debug=True)
