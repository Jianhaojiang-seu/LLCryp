latitude_coefficient = 5.4
longitude_coefficient = 6

class Location:
    latitude = ["", None]  # [direction {N, S, E, W}, value]
    longitude = ["", None]   # [direction {N, S, E, W}, value]
    tolerance = None

    def __init__(self, latitude = None, longitude = None, tolerance = None):
        if latitude:
            self.latitude = self.toDegreeDecimalMinutes(latitude, 1)
        if longitude:
            self.longitude  = self.toDegreeDecimalMinutes(longitude, 2)
        if tolerance:
            self.tolerance = tolerance 

    def getTransformedLocation(self):
        """ Main driver function.
            Gives transformed location to be used in key construction process
        """
        transformed_location =  [self.transformLocation(self.longitude[0], self.longitude[1]), self.transformLocation(self.latitude[0], self.latitude[1])]
        return transformed_location

    def getAdjacentQuadrants(self):
        return self.createAdjacentQuadrants(self.transformLocation(self.longitude[0], self.longitude[1]), self.transformLocation(self.latitude[0], self.latitude[1]))

    def transformLocation(self, location_dir, location_value):
        location_value = location_value * 10000
        if location_dir == "N" or location_dir == "S":
            return round(self.includeLocationSign(location_dir, location_value / (self.tolerance * latitude_coefficient)), 2)
        else: 
            return round(self.includeLocationSign(location_dir, location_value / (self.tolerance * longitude_coefficient)), 2)

    def includeLocationSign(self, location_dir, location_value):
        if (location_dir == "N" or location_dir == "W"):
            return location_value
        else:
            return -1 * location_value


    def createAdjacentQuadrants(self, latitude_val, longitude_val):
        adjacentQuadrants = []  # list containing all the possible quadrants
        directions = [1, -1, 0]
        for x in directions:
            for y in directions:
                adjacentQuadrants.append([latitude_val + x, longitude_val + y])
        return adjacentQuadrants

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