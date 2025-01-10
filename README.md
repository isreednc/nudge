# Nudge 

A simple terminal-based timer that helps users stay on track by reminding them of tasks at regular intervals. The timer repeats until the user decides to quit, making it a handy tool for those who tend to get carried away with their work.

## Features

- Set a timer for a specified duration.
- Repeat the timer until the user quits.
- Simple and easy-to-use interface.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/isreednc/nudge.git
   ```

2. Navigate to the project directory:
   ```bash
   cd REPO_NAME
   ```

3. Install dependencies (pygame)
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the program with the following command line arguments:
```bash
python nudge.py <time_in_seconds> [label] [repeats]
```

- <time_in_seconds>: The duration for the timer in seconds (required).
- [label]: A label for the timer (optional).
- [repeats]: The number of times to repeat the timer (optional). If not specified, the timer will repeat indefinitely.

You can exit the timer program at any time by:

- Pressing Ctrl + C in the terminal.
- Typing quit in the command line.



