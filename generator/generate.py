import csv
import random
import os
import sys

NUM_ROWS = 50


COLUMNS = ["PLAYER_NAME", "AGE", "POSITION", "GOALS+ASSIST"]

def generate_row():

    return {
        "PLAYER_NAME": random.choice([
            "Lamine Yamal",
            "Lionel Messi",
            "Matvey Safonv",
            "Pedri",
            "Mpappe",
            "Harry Kane",
            "Erling Haaland",
            "Alexander Golovin",
            "Vitinha",
            "Declan Rice"
            "Virgil Van dijk",
        ]),
        "AGE": random.randint(18, 38),
        "POSITION": random.choice(["Goalkeeper", "Defender", "Midfielder", "Forward"]),
        "GOALS+ASSIST": random.randint(0, 70),
    }

OUTPUT_DIR = sys.argv[1] if len(sys.argv) > 1 else "/data"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "data.csv")

os.makedirs(OUTPUT_DIR, exist_ok=True)

rows = [generate_row() for _ in range(NUM_ROWS)]

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=COLUMNS)
    writer.writeheader()
    writer.writerows(rows)

