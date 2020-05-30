from flask import Flask, render_template
app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
    return render_template('./index.html')

@app.route('/<string:page_name>')
def pages(page_name=None):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def sumbit():
    return 'form submitted'

'''
@app.route('/blog')
def blog():
    return 'These are my thoughts on blog'

@app.route('/blog/2020/dogs')
def blog2():
    return 'These are dogs'

@app.route('/<username>/<int:post_id>')
def blog3(username=None,post_id=None):
    return render_template('./index.html',name=username,id=post_id)


set FLASK_ENV=development
set FLASK_APP=server.py
flask run
'''