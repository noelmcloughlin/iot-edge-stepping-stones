
class MyBoard():
    """ Basic Electronic Board class for 
        - SenseHat
        - BME680

        The argument 'board' is instance of your board's python library.
     """

    def __init__(self, name='sense_hat'):
        """ Initialize the Board """

        self.name = name
        if self.name == 'sense_hat':
            try:
                from sense_hat import SenseHat
            except:
                print("\nCannot import the sensehat module")
                exit(1)
            self.board = SenseHat()

        elif name == 'bme680':
            try:
                self.board = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
            except IOError:
                try:
                    self.board = bme680.BME680(bme680.I2C_ADDR_SECONDARY)
                except:
                    print("\nCannot detect %s over I2C" % name)
                    exit(1)
            self.board.set_humidity_oversample(bme680.OS_2X)
            self.set_pressure_oversample(bme680.OS_4X)
            self.set_temperature_oversample(bme680.OS_8X)
            self.set_filter(bme680.FILTER_SIZE_3)
        self.name = name

    def read(self, sensor):
        if sensor == 'temperature':
            return self.read_temperature()
        elif sensor == 'humidity':
            return self.read_humidity()
        elif sensor == 'pressure':
            return self.read_pressure
        else:
            return None

    def read_temperature(self):
        if self.name == 'sense_hat':
            return {'t': round(self.board.get_temperature(),2),}
        elif self.name == 'bme680':
            return {'t': round(self.board.data.temperature,2),}

    def read_humidity(self):
        if self.name == 'sense_hat':
            return {'h': self.board.get_humidity(),}
        elif self.name == 'bme680':
            return {'h': self.board.data.humidity,}

    def read_pressure(self):
        if self.name == 'sense_hat':
            return {'p': self.board.get_pressure(),}
        elif self.name == 'bme680':
            return {'p': self.board.data.pressure,}
