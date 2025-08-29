# Group Task 11 – Contacat Saver
## Project Overview
You are running a short tech workshop and need a simple program to collect participant details: name, age, phone, and track. 
These details should be saved into a CSV file so organizers can follow up later.

* **It allows users to:**
* **Add participant details (name, age, phone, track)**
* **Store them in a CSV file (participants.csv)**
* **View stored participant records in a formatted display**
The project demonstrates Python fundamentals such as file handling, CSV operations, input validation, and modular code structure.

## Features
* Validates user inputs (e.g., age must be numeric, phone number must be 11 digits).
* Stores participant data in a persistent CSV file.
* Reads and displays participant details neatly.
* Modularized code structure (main.py and fileops.py).


### Project Structure
```
Group-Task-11/
│── main.py          # Handles program flow & user interaction
│── file_ops.py      # Functions for saving and loading participants
│── __init__.py      # Module initializer (empty)
│── participant_pkg/ # Folder where participants.csv is stored
```

### Group Members & Contributions
1 **Majaro Hassan**
- Implemented main.py
- Designed the program flow (menu options, input validation, participant registration loop).

2 **Opeyemi Odejimi**
- Co-implemented file_ops.py
- Worked on saving participant data to CSV.


3 **Adegboyega Fatai**
- Co-implemented file_ops.py
- Developed the logic for loading/displaying participant details from CSV.

  
4 **Mr Oba**
- Created __init__.py file for module initialization.

---
## License
This project is for educational purposes as part of the AI Engineering Training Group Task.
