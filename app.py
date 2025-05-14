from flask import Flask, render_template, request, jsonify
from appointment_bot import AppointmentBot
import socket

app = Flask(__name__)
bot = AppointmentBot()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    response, should_exit = bot.process_input(user_message)
    return jsonify({
        'response': response,
        'should_exit': should_exit
    })

def find_available_port(start_port=8000, max_port=8100):
    """Find an available port in the given range"""
    for port in range(start_port, max_port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('127.0.0.1', port))
                return port
        except OSError:
            continue
    raise RuntimeError('No available ports found')

if __name__ == '__main__':
    try:
        port = find_available_port()
        print(f"\nStarting server on port {port}")
        print(f"Open your browser and go to: http://127.0.0.1:{port}\n")
        app.run(host='127.0.0.1', port=port, debug=True)
    except Exception as e:
        print(f"Error starting server: {e}")
        print("Please try running the application again or use a different port.") 