from flask.ext.login import LoginManager, UserMixin, current_user, login_user, logout_user

login_manager = LoginManager()
login_manager.init_app(app)