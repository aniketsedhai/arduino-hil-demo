import sys
import time
import serial

port = sys.argv[1]
print(f"Opening serial connection to {port}...")

with serial.Serial(port, 115200, timeout=3) as ser:
    ser.dtr = True
    time.sleep(2.0)
    ser.reset_input_buffer()

    print("Sending: PING")
    ser.write(b"PING\n")

    response = ser.readline().decode("utf-8", errors="ignore").strip()
    print(f"Received: {response}")

    if response != "PONG":
        print(f"HiL Test FAILED: Expected 'PONG', got '{response}'")
        sys.exit(1)

    print("HiL Test PASSED! Hardware responded correctly.")
