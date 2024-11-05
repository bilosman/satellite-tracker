from visualizations.ground_track import *
from visualizations.polar_cord import *
import sys

import sys

def select_option(options, prompt):
    """Display options and prompt user to select one."""
    sys.stdout.write(prompt + "\n")
    for idx, option in enumerate(options, 1):
        sys.stdout.write(f"{idx}. {option}\n")
    sys.stdout.write("Enter the number of your choice: ")
    print('\n')
    
    try:
        choice = int(sys.stdin.readline().strip()) - 1
        if 0 <= choice < len(options):
            return options[choice]
        else:
            sys.stdout.write("Invalid selection. Please choose a valid number.\n")
            return select_option(options, prompt)
    except ValueError:
        sys.stdout.write("Invalid input. Please enter a number.\n")
        return select_option(options, prompt)

def main():
    visualization_types = ["Ground Track Visualization", "Polar Coordinate Visualization"]
    visualization_choice = select_option(visualization_types, "Select Visualization Type:")

    satellites = [
        "ISS (ZARYA)", "CSS (TIANHE)", "ISS (NAUKA)", "FREGAT DEB",
        "CSS (WENTIAN)", "CSS (MENGTIAN)", "TIANZHOU-7", "1998-067WL",
        "SZ-17 MODULE", "PROGRESS-MS 27", "CYGNUS NG-21", "PROGRESS-MS 28",
        "BINAR-4", "COSMOGIRLSAT", "SAKURA", "BINAR-2", "BINAR-3",
        "1998-067WY", "SOYUZ-MS 26", "CREW DRAGON 9", "CYSAT-1", "DORA",
        "SHENZHOU-19 (SZ-19)", "2024-194B", "2024-194C", "2024-194D"
    ]

    observers = {
        "Port Hedland": ('20.3123 S', '118.64498 E'), 
        "New York": ('40.7128 N', '74.0060 W'),
        "Tokyo": ('35.6895 N', '139.6917 E'), 
        "Sydney": ('33.8688 S', '151.2093 E'),
        "London": ('51.5074 N', '0.1278 W'),
        "Berlin": ('52.5200 N', '13.4050 E'),
        "Paris": ('48.8566 N', '2.3522 E'),
        "Los Angeles": ('34.0522 N', '118.2437 W'),
        "Moscow": ('55.7558 N', '37.6173 E'),
        "Dubai": ('25.276987 N', '55.296249 E'),
        "Beijing": ('39.9042 N', '116.4074 E'),
        "Delhi": ('28.6139 N', '77.2090 E'),
        "São Paulo": ('23.5505 S', '46.6333 W'),
        "Cairo": ('30.0444 N', '31.2357 E'),
        "Johannesburg": ('26.2041 S', '28.0473 E'),
        "Singapore": ('1.3521 N', '103.8198 E'),
        "Hong Kong": ('22.3193 N', '114.1694 E'),
        "Toronto": ('43.651070 N', '79.347015 W'),
        "Buenos Aires": ('34.6037 S', '58.3816 W'),
        "Mexico City": ('19.4326 N', '99.1332 W')
    }

    time_zones = [
        "UTC", 
        "US/Eastern", "US/Central", "US/Mountain", "US/Pacific", 
        "Europe/London", "Europe/Berlin", 
        "Asia/Tokyo", "Australia/Sydney", "Asia/Kolkata"
    ]


    observers_names = list(observers.keys())
    satellite_choice = select_option(satellites, "Select Satellite:")

    if visualization_choice == "Ground Track Visualization":
        time_zone_choice = select_option(time_zones, "Select Time Zone:")
        observer_choice = select_option(observers_names, "Select Observer Location:")
        
        sys.stdout.write(f"Selected: {visualization_choice} -> {satellite_choice} -> {observer_choice}\n")
        visualize_ground_track(satellite_choice, time_zone_choice, observers[observer_choice][0], observers[observer_choice][1])

    elif visualization_choice == "Polar Coordinate Visualization":
        time_zone_choice = select_option(time_zones, "Select Time Zone:")
        observer_choice = select_option(observers_names, "Select Observer Location:")

        sys.stdout.write(f"Selected: {visualization_choice} -> {satellite_choice} -> {time_zone_choice} -> {observer_choice}\n")
        visualize_polar_coordinates(time_zone_choice, satellite_choice, observers[observer_choice][0], observers[observer_choice][1])


if __name__ == "__main__":
    main()
