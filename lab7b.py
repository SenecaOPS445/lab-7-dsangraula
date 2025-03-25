#!/usr/bin/env python3
class Time:
    def __init__(self, hour, minute, second):
        if not all(isinstance(i, int) for i in [hour, minute, second]):
            raise ValueError("Hour, minute, and second must be integers")
        
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(time):
    return f"{time.hour:02}:{time.minute:02}:{time.second:02}"


def change_time(time, seconds):
    """Modify the time object by adding or subtracting seconds."""
    time.second += seconds

    # Handle positive carryover
    while time.second >= 60:
        time.second -= 60
        time.minute += 1
    while time.minute >= 60:
        time.minute -= 60
        time.hour += 1

    # Handle negative seconds
    while time.second < 0:
        time.second += 60
        time.minute -= 1
    while time.minute < 0:
        time.minute += 60
        time.hour -= 1

    return None
