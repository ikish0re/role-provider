import bot
from flask import Flask, request


app = Flask(__name__)

@app.route("/api/discord", methods=["POST"])
def post_discord_id():
    data = request.get_json()
    print(data["id"])
    status = bot.run_discord_bot(data["id"], data["job"])
    if(status == "Ok"):
        return status["message"], status["code"]
    else:
        return status, 404

if __name__ == "__main__":
    app.run(debug=True)