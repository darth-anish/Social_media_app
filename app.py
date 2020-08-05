from flask import Flask, render_template, request
from models import create_posts, see_posts

app = Flask(__name__, template_folder = 'templates')

@app.route('/', methods=['GET'])
def index():
    post_var = see_posts()
    return render_template('index.html', post_var = post_var)



@app.route('/posts', methods=['POST', 'GET'])
def posts():
    if request.method == 'GET':
        pass

    if request.method == 'POST':
        name = request.form.get('name')
        status = request.form.get('post')
        create_posts(name, status)

    return render_template('posts.html')

if __name__ == '__main__':
    app.run(debug=True)
