# Location class to hold latitude and longitude
class Location:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

class ObstructionDetector:
    def __init__(self):
        self._speed = None
        self._location_a = None
        self._location_b = None
    
    def set_speed(self, speed):
        if speed <= 0:
            raise ValueError("Positive value")
        self._speed = speed
    
    def set_locations(self, location_a, location_b):
        if not isinstance(location_a, Location) or not isinstance(location_b, Location):
            raise ValueError("Instances of the Location class")
        self._location_a = location_a
        self._location_b = location_b
    
    # Calculate the expected time it should take to travel
    def calculate_expected_time(self):
        if not self._speed or not self._location_a or not self._location_b:
            raise ValueError("Set speed and locations")
        
        distance = self.calculate_distance()
        expected_time = distance / self._speed
        return expected_time
    

    def calculate_distance(self):
        if not self._location_a or not self._location_b:
            raise ValueError("Locations is needed")
        
        distance = ((self._location_b.latitude - self._location_a.latitude)**2 +
                    (self._location_b.longitude - self._location_a.longitude)**2) ** 0.5
        return distance
    
    # check for obstacle
    def is_impenetrable_obstruction(self, expected_time, actual_time):
        expected_time_to_reach = expected_time + 60
        """Adding 60 minutes to the expected time it will take to get from point a to point b"""
        return actual_time > expected_time_to_reach

if __name__ == "__main__":
    try:
        # Logging to keep track of what's going on
        import logging
        logging.basicConfig(level=logging.INFO)
        
        location_a = Location(53.5872, -2.4138)
        location_b = Location(53.474, -2.2388)
        
        # set up our obstruction detector
        obstruction_detector = ObstructionDetector()
        
        # Set speed, locations, and actual travel time
        obstruction_detector.set_speed(5)
        obstruction_detector.set_locations(location_a, location_b)
        actual_time = 78
        
        # Calculate the expected time and check if there's a tough rock in our way
        expected_time = obstruction_detector.calculate_expected_time()
        if obstruction_detector.is_impenetrable_obstruction(expected_time, actual_time):
            logging.info("There is Obstruction.")
        else:
            logging.info("No Obstruction")
    
    except ValueError as e:
        logging.error(f"An error occurred: {e}")
