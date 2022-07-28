from flask import Flask,request

app=Flask(__name__)

@app.route('/hello')
def hello():
    age=request.args['age']
    print(request.args)
    return '<h1>Hello,%s</h1>'%age

