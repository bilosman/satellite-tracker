from skyfield import api
import pytz
from pytz import timezone
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

def visualize_polar_coordinates(time_zone_name: str, satellite_name: str, observer_lat: str, observer_long: str):
    time_zone = timezone(time_zone_name)

    station_data = api.load.tle('https://celestrak.com/NORAD/elements/stations.txt')
    satellite = station_data[satellite_name]

    minutes = range(60 * 24 * 2)
    time_scale = api.load.timescale()
    time_zone_for_date = pytz.timezone(time_zone_name)
    current_date = datetime.now(time_zone_for_date)
    time_range = time_scale.utc(current_date.year, 
                                current_date.month, 
                                current_date.day, 
                                current_date.hour, 
                                minutes)


    time_range = time_scale.utc(2024, 3, 21, 2, minutes)
    observer = api.Topos(latitude=observer_lat, longitude=observer_long)
    orbit = (satellite - observer).at(time_range)
    altitude, azimuth, distance = orbit.altaz()
    #print(f"Altitudes: {altitude}")
    #print(f"Azimuth: {azimuth}")
    #print(f"Distance: {distance}")

    visible_pass = altitude.degrees > 0
    indicies, = visible_pass.nonzero()
    boundaries, = np.diff(visible_pass).nonzero()

    boundaries = boundaries if len(boundaries) % 2 == 0 else boundaries[0: -1]
    passes = boundaries.reshape(len(boundaries) // 2, 2)
    #print(passes)


    pass_to_observe = 0
    specific_pass = passes[pass_to_observe]
    rise, set = specific_pass
    print(f'Satellite Rises at {time_range[0].astimezone(time_zone)}')
    print(f'Satellite Sets at {time_range[1].astimezone(time_zone)}')

    ax = plt.subplot(111, projection='polar')
    plt.title(f"{satellite_name} Pass Polar Chart")
    ax.set_rlim([0, 100])
    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1)

    azimuth_angle = azimuth.radians
    altitude_radius = 90 - altitude.degrees
    ax.plot(azimuth_angle[rise:set], altitude_radius[rise:set], 'bo--')

    for k in range(rise, set):
        text = time_range[k].astimezone(time_zone).strftime('%H:%M')
        ax.text(azimuth_angle[k], altitude_radius[k], text, ha='right', va='bottom')
    plt.show()


# Test code
if __name__ == "__main__":
    visualize_polar_coordinates(
        time_zone_name="UTC",
        satellite_name="ISS (ZARYA)",
        observer_lat="20.3123 S",
        observer_long="118.64498 E"
    )
