import serial

# Change this to your HC-05 COM port (Check Device Manager for Windows)
bluetooth_port = "COM8"  # Replace with actual port, e.g., COM5 (Windows) or /dev/ttyUSB0 (Linux/macOS)
baud_rate = 9600  # Default baud rate for HC-05

try:
    # Open serial connection to HC-05
    bt_serial = serial.Serial(bluetooth_port, baud_rate, timeout=1)
    print(f"Connected to {bluetooth_port}")

    while True:
        # Read data from Bluetooth
        data = bt_serial.readline().decode("utf-8").strip()
        if data:
            print(f"Received: {data}")  # Print received message

except serial.SerialException as e:
    print(f"Error: {e}")

except KeyboardInterrupt:
    print("\nDisconnected from Bluetooth.")

finally:
    if 'bt_serial' in locals() and bt_serial.is_open:
        bt_serial.close()