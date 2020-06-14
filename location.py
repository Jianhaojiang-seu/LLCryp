# const latitude_coefficient = 5.4
# const longitude_coefficient = 6

class Location:
    latitude = ["", 0]  # [direction, value]
    longitude = ["", 0]   # [direction, value]

    def __init__(self, latitude = None, longitude = None, tolerance = None):
        if latitude:
            self.latitude = self.toDegreeDecimalMinutes(latitude, 1)
        if longitude:
            self.longitude  = self.toDegreeDecimalMinutes(longitude, 2)

    def transformed_location(self):
        """Gives transformed location to be used in key construction process
        """
        transformed_location = [None, None]
        # TODO: implement it
        return transformed_location

    def toDegreeDecimalMinutes(self, location_value, location_type):
        """Convert location values
        """
        result_location = ["", 0.0]
        if location_value < 0 and location_type == 1:
            location_sign = "S"
            location_value = location_value * -1
        elif location_value < 0 and location_type == 2:
            location_sign = "W"
            location_value = location_value * -1
        elif location_value > 0 and location_type == 1:
            location_sign = "N"
        elif location_value > 0 and location_type == 2:
            location_sign = "E"
        result_location[0] = location_sign
        result_location[1] = location_value
        # TODO: convert result_location to degrees & minutes
        return result_location