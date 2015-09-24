from flask import Flask, render_template
from flask.ext.login import LoginManager, UserMixin, current_user, login_user, logout_user

app = Flask(__name__)

import db

login_manager = LoginManager()
login_manager.init_app(app)

'''class UserNotFoundError(Exception):
	pass

class User(UserMixin):
	
	def __init__(self, id):
		if not id in self.
'''

@app.route('/')
def main():
	return render_template('index.html')

@app.rout('/signup_check', methods=['POST']):


if __name__ == "__main__":
    app.run(debug=True)