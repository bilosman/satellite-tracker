import ephem
import matplotlib.pyplot as plt
from datetime import datetime
from skyfield.api import utc, load, Topos
import pytz

# Defining the TLE Data - Information from the International Space Station
stations_url = 'http://celestrak.com/NORAD/elements/stations.txt'
satellites = load.tle(stations_url)

def visualize_ground_track(satellite_name: str , time_zone: str, observer_lat: str, observer_long: str):
    satellite = satellites[satellite_name]

    # Defining the Time Range that we want to pay attention to the satellite
    time_scale = load.timescale()
    timezone = pytz.timezone(time_zone)
    current_date = datetime.now(timezone)
    time_range = time_scale.utc(current_date.year, 
                                current_date.month, 
                                current_date.day, 
                                current_date.hour, 
                                minute=range(60 * 2)) # 2 hours

    altitudes = []
    azimuths = []
    for t in time_range:
    # Calculate satellite position at each time step
        observer = Topos(latitude=observer_lat, longitude=observer_long)
        orbit = (satellite - observer).at(t) # Observer relative to the space station for every t
        altitude, azimuth, distance = orbit.altaz()

        altitudes.append(altitude.degrees)
        azimuths.append(azimuth.degrees)

    # Plotting the Satellite Path
    plt.figure(figsize=(10,5))
    plt.plot(azimuths, altitudes, marker='o', linestyle='-')
    plt.title(f"Satellite Path - {satellite_name}")
    plt.xlabel("Azimuth (degrees)")
    plt.ylabel("Altitude (degrees)")
    plt.grid(True)
    plt.show()

# Test code
if __name__ == "__main__":
    # Example values to test independently
    visualize_ground_track(
        time_zone_name="UTC",
        satellite_name="ISS (ZARYA)",
        observer_lat="20.3123 S",
        observer_long="118.64498 E"
    )
