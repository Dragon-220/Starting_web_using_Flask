from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'hello world'

app.add_url_rule('/',hello_world)

if __name__ == '__main__':
    app.run()