import uasyncio
from ioUtil import MotorUtil

mainMotor = MotorUtil([12, 13, 14, 15])
lmainMotor = MotorUtil([9, 8, 7, 6])

#while 1: print("1")

print("start")
uasyncio.run(mainMotor.move(11))
print("end")

