import serial
import time

def respond_to_command(cmd: str) -> str:
    cmd = cmd.strip().upper()

    if cmd == "#RD":
        # Return fake pressure value
        return "* 1.23E-03\r"
    elif cmd == "#RD1":
        return "* 1.10E-03\r"
    elif cmd == "#RD2":
        return "* 2.34E-03\r"
    elif cmd == "#DGS":
        return "* 0DG OFF\r"
    elif cmd == "#IGS":
        return "* 01\r"
    else:
        return "* ? INVALID\r"

def main():
    port = '/tmp/ttyV1'
    baudrate = 9600

    try:
        ser = serial.Serial(port, baudrate=baudrate, timeout=1)
        print(f"Listening on {port}...")

        while True:
            if ser.in_waiting:
                received = ser.read_until(b'\r').decode().strip()
                print(f"Received: {received}")

                response = respond_to_command(received)
                print(f"Sending: {response.strip()}")
                ser.write(response.encode())
            time.sleep(0.1)

    except serial.SerialException as e:
        print(f"Serial error: {e}")

if __name__ == "__main__":
    main()
