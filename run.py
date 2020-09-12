from flask import Flask
from flask_restful import Api

from auth.resources.user_profile_resource import UserProfile
from extensions import db, jwt

from auth.resources.login_resource import LoginResource
from auth.resources.signup_resource import SignupResource

app = Flask(__name__)
api = Api(app, prefix='/v1')
app.config.from_object('config.default')
app.config.from_envvar('CONFIGURATION_FILE')


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(SignupResource, '/auth/signup')
api.add_resource(LoginResource, '/auth/login')
api.add_resource(UserProfile, '/users/<user_id>/me')

if __name__ == '__main__':
    db.init_app(app)
    jwt.init_app(app)
    app.run(debug=True)
