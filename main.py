from flask import Flask, request, session, redirect, url_for, render_template
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required


login_manager = LoginManager()
app = Flask(__name__)

login_manager.init_app(app)

# class Human:
#     # инициализация
#     def __init__(self, height=165, weight=76):
#         # property
#         self.height = height
#         self.weight = weight
#
#     def get_height_weight(self):
#         return f"Your height is {self.height} and your weight is {self.weight}"
#
#
# man = Human()
# print(man.height, man.weight, man.get_height_weight())
#
#
# class Rider(Human):
#     pass
#
#
# rider = Rider()
# print(rider)
# Set the secret key to some random bytes. Keep this really secret!
# Set the secret key to some random bytes. Keep this really secret!

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

class User(UserMixin):
    pass

users = {'admin': {'password': 'admin'}}


@login_manager.user_loader
def load_user(user_id):
    user = User()
    user.id = user_id
    return user


@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}<br><a href="/logout">Logout</a>'
    return 'You are not logged in<br><a href="/login">Login</a>'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and password == users[username]['password']:
            user = User()
            user.id = username
            login_user(user)
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Incorrect username or password')

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    logout_user()
    return redirect(url_for('index'))


@app.route('/profile')
@login_required
def profile():
    return f'Hello, {current_user.id}!'


if __name__ == '__main__':
    app.run(host="localhost", port="8000", debug=True)