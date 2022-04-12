from sqlalchemy import Column, Integer, String, Date, DateTime, JSON
from database import Base

class Meeting(Base):
    __tablename__ = 'meetings'

    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer())
    game_name = Column(String(), index=True)
    # create_date = Column(Date())
    # number_of_players = Column(Integer())
    # meeting_place = Column(String())
    # meeting_date_time = Column(DateTime(timezone=True))
    # description = Column(String())
    # subscribed_players = Column(JSON)
    # confirmed_players = Column(JSON)
    # game_id = Column(Integer, ForeignKey('games.id'), index=True, nullable=True)
    # city_name = Column(String(), index=True)
    # city_id = Column(Integer, ForeignKey('cities.id'), index=True, nullable=True)
    # user = relationship('User', backref='game_meetings', foreign_keys=[owner_id], lazy='joined')
    # users = relationship('MeetingUser', backref='game_meetings', lazy='joined')
    # game = relationship("Game", lazy='subquery')
    # city = relationship("City", lazy='subquery')

    def json(self):
        return {
            'id': self.id,
            'owner_id': self.owner_id,
            'game_name': self.game_name,
            # 'create_date': self.create_date,
            # 'number_of_players': self.number_of_players,
            # 'meeting_place': self.meeting_place,
            # 'meeting_date_time': self.meeting_date_time,
            # 'description': self.description,
            # 'subscribed_players': self.subscribed_players,
            # 'confirmed_players': self.confirmed_players,

        }
