from flask import Flask, request, jsonify
from plyer import notification

app = Flask(__name__)

@app.route('/notify', methods=['POST'])
def send_notification():
    data = request.json
    title = data.get('title', 'Notification')
    message = data.get('message', 'You received a new notification!')

    # Send a desktop notification
    notification.notify(
        title=title,
        message=message,
        app_name="IFTTT Notifier",
        timeout=5
    )

    return jsonify({"status": "Notification sent"}), 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)
