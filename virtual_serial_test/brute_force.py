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

baudrates = [19200, 9600, 4800, 2400, 1200, 600, 300, 150, 75]
bytesizes = [serial.SEVENBITS, serial.EIGHTBITS]
parities = [serial.PARITY_NONE, serial.PARITY_EVEN, serial.PARITY_ODD]
stopbits_lst = [serial.STOPBITS_ONE, serial.STOPBITS_TWO]

port = 'dev/ttyUSB0'

def main():
    try:
        for baudrate in baudrates:
            for bytesize in bytesizes:
                for parity in parities:
                    for stopbits in stopbits_lst:
                        ser = serial.Serial(
                            #port='/tmp/ttyV0',
                            port='/dev/ttyUSB0',
                            baudrate=baudrate,
                            bytesize=bytesize,
                            parity=parity,
                            stopbits=stopbits,
                            timeout=2)
                        print(f"{baudrate}, {bytesize}, {parity}, {stopbits}")
                        logging.info(f"{baudrate}, {bytesize}, {parity}, {stopbits}")
                        user_input = "#DS\r"

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
