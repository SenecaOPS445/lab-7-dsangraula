#!/usr/bin/env python3
# Student ID: dsangraula
class Time:
    """Simple object type for time of the day.
    data attributes: hour, minute, second
    """
    def __init__(self,hour=12,minute=0,second=0):
        """constructor for time object""" 
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    """Add two time objects and return the sum with proper carryover."""
    sum = Time(0, 0, 0)
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second

    # Carry over seconds
    if sum.second >= 60:
        sum.minute += sum.second // 60
        sum.second %= 60

    # Carry over minutes
    if sum.minute >= 60:
        sum.hour += sum.minute // 60
        sum.minute %= 60

    # Ensure hour stays within 24-hour format (optional, depending on requirement)
    sum.hour %= 24

    return sum
