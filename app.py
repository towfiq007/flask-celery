from flask import *  
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


# @socketio.on('client_event', namespace='/test')
@socketio.on('client_event')
def handle_my_custom_event(data_from_client):
    print('client_event')
    print(data_from_client)
    emit('alert_events', 'Alert from server')


@socketio.on('alert_events')
def handle_my_custom_event(data_from_client):
    print(data_from_client)
    emit('alert_events', 'Alert from server')
    print('emitted alert_events')

@app.route('/')  
def index():  
      return render_template('index.html')  

if __name__ == '__main__':
    socketio.run(app)
    # app.run(debug=True)



