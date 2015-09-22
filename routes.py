from flask import Flask, render_template
app = Flask(__name__)

import auth

@app.route('/')
def main():
	return render_template('index.html')

@app.route('/login')
def login():
	return facebook.authorize(callback=url_for('oauth_authorized',
		next=request.args.get('next') or request.referrer or None))

if __name__ == "__main__":
    app.run(debug=True)