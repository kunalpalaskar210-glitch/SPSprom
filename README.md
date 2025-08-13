# SPSpro

**---------Stone Paper Scissors Game---------** 
A simple Flask web app where you play Stone, Paper, Scissors against the computer. Scores are saved in a CSV file, and you can reset them anytime.

   **-------- Features--------**
  1.Play Stone, Paper, Scissors against the computer.
  2.Automatic winner calculation.
  3.Scoreboard showing past results from a CSV file.
  4.Reset button to clear all scores.
  5.Simple and colorful responsive design.

   **-------- Gameplay Rules--------**

  Stone beats Scissors
  Paper beats Stone
  Scissors beats Paper
  Same choices = Draw

  **----project file structure----**
      │
      ├── app.py                # Flask main application
      ├── scores.csv            # CSV file storing scores
      ├── templates/
      │   └── index.html         # Game HTML template
      ├── static/
      │   └── style.css          # Game styling
      └── README.txt             # This file

  **-------Preview screenshot-------**

To view screenshot (ctrl+click) on link below

<img width="1920" height="1080" alt="preview" src="https://github.com/user-attachments/assets/de4ba597-7b4f-4fcc-89da-282a4ab5f938" />


   **------pakages used------**
      **--External--**
   1.Flask : Web framework to run your Stone–Paper–Scissors game in the browser.
      **--Built-in--**
   2.CSV file : Read and write game results to scores.csv file.
   3.Random : Pick a random move for the computer (Stone, Paper, Scissors).



   **----- CSV File Format----**
The scores.csv file stores data in the following format:
EX:
| Player   | Computer | Result        |
| -------- | -------- | ------------- |
| Stone    | Paper    | Computer Wins |
| Scissors | Paper    | Player Wins   |
| Paper    | Paper    | Draw          |


