from flask import Flask,url_for
import click
app=Flask(__name__)
#从flask包导入Flask类
#实例化这个类，就得到程序实例app

#注册路由
@app.route('/')
def index():
    return '<h1>Hello Flask!</h1>'

#为视图绑定多个路由
@app.route('/hi')
@app.route('/hello')
def say_hello():
    return '<h1>Hello Flask!!!</h1>'

#动态URL
@app.route('/greet/<name>')
@app.route('/greet',defaults={'name':'Programmer'})
def greet(name):
    return '<h1>Hello,%s!</h1>' % name

#创建自定义命令
@app.cli.command()
def hello():
    # click.echo('Hello,Human!')
    print('Hello,Human!!')
