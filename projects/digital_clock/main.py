import time
from datetime import datetime
import pytz

# List of time zones to display
TIME_ZONES = {
    'EST': 'America/New_York',
    'CST': 'America/Chicago',
    'PST': 'America/Los_Angeles',
    'UTC': 'UTC',
    'IST': 'Asia/Kolkata',
    'JST': 'Asia/Tokyo'
}

def get_time_in_timezones():
    """Fetch the current time in different time zones."""
    current_times = {}
    for timezone, tz in TIME_ZONES.items():
        tz_info = pytz.timezone(tz)
        current_times[timezone] = datetime.now(tz_info).strftime('%Y-%m-%d %I:%M:%S %p')
    return current_times

def display_time(current_times):
    """Display the time in a user-friendly format."""
    print("\nCurrent Time in Different Time Zones:")
    for zone, time_str in current_times.items():
        print(f"{zone}: {time_str}")

if __name__ == "__main__":
    try:
        while True:
            current_times = get_time_in_timezones()
            display_time(current_times)
            time.sleep(1)  # Delay for 1 second
            print("\033[H\033[J", end="")  # Clear console (works in most console environments)
    except KeyboardInterrupt:
        print("\nClock stopped.")