import machine
from L76GNSS import L76GNSS
from pycoproc_1 import Pycoproc

class GPSManager:
    def __init__(self):
        self.py = Pycoproc(Pycoproc.PYTRACK)
        self.l76 = L76GNSS(self.py, timeout=30)
        
    def getposition(self, timeout=30):
        counter = 0
        coord = self.l76.coordinates()
        while(counter<timeout):
            counter = counter+1
            coord = self.l76.coordinates()
            if not (coord[0] == None or coord[1] == None):
                return coord
        return coord