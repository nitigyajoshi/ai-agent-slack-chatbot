# main.py
import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv
from agent import get_agent_response  # you’ll create this function in agent.py

# Load environment variables
load_dotenv()

# Slack app tokens
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")

# Initialize Slack app
app = App(token=SLACK_BOT_TOKEN)

# Listen for messages in direct messages
# ✅ Listen to direct messages (optional)
@app.message(".*")
def handle_direct_messages(message, say):
    user_message = message['text']
    response = get_agent_response(user_message)
    say(response)

# ✅ Listen for when bot is mentioned in channels
@app.event("app_mention")
def handle_app_mention_events(body, say):
    user_message = body['event']['text']
    response = get_agent_response(user_message)
    say(response)

# ✅ Run the app with Socket Mode
if __name__ == "__main__":
    print("⚡️ Bolt app is running!")
    SocketModeHandler(app, SLACK_APP_TOKEN).start()
