class RobotData():
    def __init__(self, enabled: bool, pressure: float):
        self.enabled = enabled
        self.pressure = pressure

    @classmethod
    def fromDict(self, robot_data):
        return RobotData(robot_data["enabled"], robot_data["pressure"])

    def toDict(self):
        return {
            "enabled": self.enabled,
            "pressure": self.pressure,
        }

    def __eq__(self, other): 
        if not isinstance(other, RobotData):
            # don't attempt to compare against unrelated types
            return NotImplemented
        
        return self.enabled == other.enabled and \
            self.pressure == other.pressure
