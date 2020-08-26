from flask_restful import Resource, reqparse

from models.user import UserModel

class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type = str,
                        required = True,
                        help = "(Username)This field cannot be blank!"
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="(Password)This field cannot be blank!"
                        )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message': f"The user {data['username']} is already exists!"}, 400 # Before openning the DB!

        user = UserModel (**data) # equivaletn to - UserModel(data['username'], data['password'])
        user.save_to_db()

        return {'nessage': f"User {data['username']} created successfully!"}, 201