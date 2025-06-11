import serial
import time
import logging

# Configure logging
logging.basicConfig(
    filename="gauge_comm_log.txt",
    filemode="a",
    format="%(asctime)s - %(message)s",
    level=logging.INFO
)

port = 'dev/ttyUSB0'

def main():
    try:
        ser = serial.Serial(
            #port='/tmp/ttyV0',
            port='/dev/ttyUSB0',
            baudrate=9600,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            timeout=1,
            rtscts=True,
            dsrdtr=True)
        print(f"Connected to {ser.port}. Type commands (e.g., #RD). Type 'exit' to quit.")

        while True:
            user_input = input("Command> ").strip()
            if user_input.lower() == "exit":
                break

            # Ensure it ends with carriage return
            if not user_input.endswith('\r'):
                user_input += '\r'

            # Send command
            ser.write(user_input.encode())
            logging.info(f"Sent: {repr(user_input)}")
            
            # Wait briefly and read response
            time.sleep(0.2)
            response = ser.read_until(b'\r').decode().strip()
            print(f"Response: {response}")
            logging.info(f"Received: {response}")

        ser.close()

    except serial.SerialException as e:
        error_msg = f"Serial error on {port}: {e}"
        print(error_msg)
        logging.error(error_msg)

if __name__ == "__main__":
    main()
