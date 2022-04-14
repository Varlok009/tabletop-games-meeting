from flask import session
from database import Session
from requests import get, post



# get('http://localhost:5002/meetings/')


post('http://localhost:5002/meetings/', {
    'owner_id': 4,
    'game_name': 'pisos33',
})