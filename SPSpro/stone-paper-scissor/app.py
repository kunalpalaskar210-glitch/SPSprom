from flask import Flask, render_template, request, redirect, url_for
import csv
import os
import random

app = Flask(__name__)

CSV_FILE = "scores.csv"

# Initialize CSV file if not exists
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Player", "Computer", "Result"])  # Header row

def read_scores():
    scores = []
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                scores.append(row)
    return scores

def append_score(player, computer, result):
    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([player, computer, result])

def reset_scores():
    with open(CSV_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Player", "Computer", "Result"])

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    player_choice = ""
    computer_choice = ""
    scores = read_scores()

    if request.method == "POST":
        if "reset" in request.form:
            reset_scores()
            return redirect(url_for("index"))

        player_choice = request.form["choice"]
        computer_choice = random.choice(["Stone", "Paper", "Scissors"])

        # Determine result
        if player_choice == computer_choice:
            result = "Draw"
        elif (player_choice == "Stone" and computer_choice == "Scissors") or \
             (player_choice == "Paper" and computer_choice == "Stone") or \
             (player_choice == "Scissors" and computer_choice == "Paper"):
            result = "Player Wins"
        else:
            result = "Computer Wins"

        append_score(player_choice, computer_choice, result)
        scores = read_scores()

    return render_template("index.html", result=result, player_choice=player_choice,
                           computer_choice=computer_choice, scores=scores)

if __name__ == "__main__":
    app.run(debug=True)
