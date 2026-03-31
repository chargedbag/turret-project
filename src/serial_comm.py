import serial
import time

class SerialComm:
    def __init__(self, port, baud):
        self.ser = serial.Serial(port, baud, timeout=1)
        time.sleep(2)

    def send(self, pan, tilt):
        command = f"{int(pan)},{int(tilt)}\n"
        self.ser.write(command.encode())

    def close(self):
        self.ser.close()
