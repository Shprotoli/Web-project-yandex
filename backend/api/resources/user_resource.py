from flask_restful import Resource, reqparse
from backend.db.models.user import User
from backend.db.repositories.user_repository import UserRepository

parser = reqparse.RequestParser()
parser.add_argument('username', type=str, required=True, help='Username is required')
parser.add_argument('password', type=str, required=True, help='Password is required')
parser.add_argument('email', type=str, required=False)

class UserListResource(Resource):
    def get(self):
        users = User.query.all()
        return [user.to_dict() for user in users], 200

    def post(self):
        args = parser.parse_args()
        user = User(username=args['username'], password=args['password'])
        # optional email handling can be added
        UserRepository.create(user)
        return user.to_dict(), 201

class UserResource(Resource):
    def get(self, user_id: int):
        user = UserRepository.get_by_id(user_id)
        if not user:
            return {'message': 'User not found'}, 404
        return user.to_dict(), 200

    def put(self, user_id: int):
        user = UserRepository.get_by_id(user_id)
        if not user:
            return {'message': 'User not found'}, 404
        args = parser.parse_args()
        user.username = args['username']
        user.password = args['password']
        # commit changes
        from backend.other.extensions import db
        db.session.commit()
        return user.to_dict(), 200

    def delete(self, user_id: int):
        user = UserRepository.get_by_id(user_id)
        if not user:
            return {'message': 'User not found'}, 404
        from backend.other.extensions import db
        db.session.delete(user)
        db.session.commit()
        return {'message': 'Deleted'}, 204
