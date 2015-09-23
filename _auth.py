from flask_oauth import OAuth

oauth = OAuth()
fb_app_id = 1720905058133337
fb_app_secret = "50ba8c6da2dd383352131cd4b5fc4cf1"

facebook = oauth.remote_app('facebook',
		base_url='localhost:5000',
		request_token_url=None,
		access_token_url='/oauth/access_token',
		authorize_url='https://www.facebook.com/dialog/oauth',
		consumer_key=fb_app_id,
		consumer_secret=fb_app_secret,
		request_token_params={'scope': 'email'}
	)