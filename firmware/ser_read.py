import serial
f = open("out.bin", "wb")
s = serial.Serial("/dev/ttyUSB0", 57600, timeout=15)
s.reset_input_buffer()
print("Try starting it now")
x = s.read(4096)
f.write(x)
f.close()
s.close()

