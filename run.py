from flask import Flask
from flask_restful import Api
from extensions import db


from auth.resources.login_resource import LoginResource
from auth.resources.signup_resource import SignupResource
from orm.one_to_many_resource import OneToManyResource

app = Flask(__name__)
api = Api(app, prefix='/v1')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://snc:csit@localhost/csit-snc'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(SignupResource, '/auth/signup')
api.add_resource(LoginResource, '/auth/login')
api.add_resource(OneToManyResource, '/one-to-many')

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
