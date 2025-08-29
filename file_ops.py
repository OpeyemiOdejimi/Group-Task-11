# helper module

import csv 
from pathlib import Path 

def save_participant(path, participant_dict):
    if path.exists():
        with open(path, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(participant_dict.values())
    else:
        with open(path, "w", newline="", encoding="utf-8") as f:
            f.write("Name, Age, Phone, Track\n")
            writer = csv.writer(f)
            writer.writerow(participant_dict.values())