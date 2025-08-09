from flask import Flask, render_template, request, jsonify
import random
import csv

app = Flask(__name__)

CSV_FILE = 'game_data.csv'

def read_stats():
    try:
        with open(CSV_FILE, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                return {
                    'wins': int(row['wins']),
                    'losses': int(row['losses']),
                    'ties': int(row['ties'])
                }
    except Exception as e:
        print("Error reading CSV:", e)
        return {'wins': 0, 'losses': 0, 'ties': 0}

def write_stats(stats):
    try:
        with open(CSV_FILE, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['wins', 'losses', 'ties'])
            writer.writeheader()
            writer.writerow(stats)
    except Exception as e:
        print("Error writing CSV:", e)

def determine_winner(player, computer):
    if player == computer:
        return 'Tie'
    elif (player == 'Rock' and computer == 'Scissors') or \
         (player == 'Paper' and computer == 'Rock') or \
         (player == 'Scissors' and computer == 'Paper'):
        return 'Win'
    else:
        return 'Lose'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/play", methods=["POST"])
def play():
    data = request.get_json()
    player_choice = data["choice"]
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    result = determine_winner(player_choice, computer_choice)

    stats = read_stats()
    if result == "Win":
        stats["wins"] += 1
    elif result == "Lose":
        stats["losses"] += 1
    else:
        stats["ties"] += 1

    write_stats(stats)

    return jsonify({
        "player": player_choice,
        "computer": computer_choice,
        "result": result,
        "stats": stats
    })

    @app.route("/reset", methods=["POST"])
    def reset():
        stats = {'wins': 0, 'losses': 0, 'ties': 0}
        write_stats(stats)
        return jsonify({"message": "Game stats reset!", "stats": stats})



if __name__ == "__main__":
    app.run(debug=True)
