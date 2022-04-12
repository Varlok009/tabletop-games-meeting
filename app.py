from flask import Flask, request
from flask_restful import Api, Resource
from models import Meeting
from database import Session, migrate


def create_app(create_db=True):
    app = Flask(__name__)

    if create_db:
        migrate()
    return app


app = create_app()
api = Api(app)


class Meetings(Resource):
    def get(self):
        """
        return JSON text of all objects
        """
        with Session() as session:
            meetings = session.query(Meeting).all()
        return {'Meetings':list(x.json() for x in meetings)}

    def post(self):
        data = request.get_json()
        new_meeting = Meeting(
            data['owner_id'],
            data['game_name']
        )
        with Session() as session:
            session.add(new_meeting)
            session.commit()
        return new_meeting.json(), 201


api.add_resource(Meetings,'/meetings/')

app.debug = True
if __name__ == '__main__':
    app.run(host='localhost', port=5002)