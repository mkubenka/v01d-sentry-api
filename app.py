from flask import Flask
from flask import make_response
from flask import abort
from flask import jsonify
from raven.contrib.flask import Sentry

import events

app = Flask(__name__)
app.config.from_object('config')

sentry = Sentry(app)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/')
def home():
    raise Exception

@app.route('/api/v1/events', methods = ['GET'])
def get_events():
    return jsonify({'events': events.events})

@app.route('/api/v1/events/<int:event_id>', methods = ['GET'])
def get_event(event_id):
    event = filter(lambda e: e['id'] == event_id, events.events)
    if len(event) == 0:
        abort(404)
    return jsonify({'event': event[0]})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
