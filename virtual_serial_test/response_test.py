import serial
import time

def main():
    port = '/dev/ttyUSB0'
    baudrate = 9600

    try:
        ser = serial.Serial(port, baudrate=baudrate, timeout=1)
        print(f"Listening on {port}...")

        while True:
            if ser.in_waiting:
                received = ser.read_until(b'\r').decode().strip()
                print(f"Received: {received}")


                # response = respond_to_command(received)
                # print(f"Sending: {response.strip()}")
                # ser.write(response.encode())
            time.sleep(0.1)

    except serial.SerialException as e:
        print(f"Serial error: {e}")

if __name__ == "__main__":
    main()