# Ping Monitor

A simple network monitoring tool written in Python.

The program periodically sends ping requests to a specified IP address and displays the response time and packet loss.

## Features

- Check host availability
- Measure ping in milliseconds
- Detect packet loss
- Display results in the terminal
- Perform periodic network checks

## Technologies

- Python
- `subprocess`
- `re`
- `time`

## How to Run

1. Install Python.
2. Clone or download this repository.
3. Open a terminal in the project directory.
4. Run:

```bash
python ping_monitor.py
```

## Example

```text
Ping: 24 ms
Ping: 21 ms
Ping: 26 ms
Ping: 23 ms
```

## How It Works

The program uses the Python `subprocess` module to execute the system `ping` command.

The output of the command is captured and analyzed using a regular expression. The program extracts the ping response time from the command output.

If no response time is found, the program reports a packet loss.

## Purpose

This project was created to practice Python, working with system commands, processing command output, regular expressions, and basic network monitoring.

## Future Improvements

- Calculate average ping
- Calculate packet loss percentage
- Track minimum and maximum ping
- Save monitoring results to a file
- Add ping history
- Create ping graphs
