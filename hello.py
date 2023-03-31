from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/handle_data', methods=['POST'])
def handle_data():
    projectpath = request.form['projectFilepath']
    # your code
    print(projectpath)
    return "Thank you"
    # return a response


@app.route('/user')
def user():
    return render_template('input.html')


@app.route('/userinput', methods=['POST']) 
def userinput():
    username = request.form['username']
    print(username)
    return f"Your username is {username}"

if __name__ == '__main__':
    app.run(debug=True)

