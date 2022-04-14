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
        print('ok')
        print(request.form)
        print(request.form['game_name'])
        print(request.form['owner_id'])
        new_meeting = Meeting(    
            owner_id = request.form['owner_id'],
            game_name = request.form['game_name']
        )
        with Session() as session:
            session.add(new_meeting)
            session.commit()
            return {'Meeting':new_meeting.json()}, 201


class GameMeeting(Resource):
    def get(self, game_name):
        """
        return JSON text of one objects
        """
        with Session() as session:
            meeting = session.query(Meeting).filter(Meeting.game_name==game_name).one()
        return {'Meeting': meeting.json()}


api.add_resource(Meetings,'/meetings/')
api.add_resource(GameMeeting,'/meeting/<string:game_name>')

app.debug = True
if __name__ == '__main__':
    app.run(host='localhost', port=5002)