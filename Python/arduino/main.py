import serial
import json
import telebot
from threading import Thread

TELEGRAM_BOT_TOKEN = ""
CHAT_ID = ""

PORT = "COM3"
arduino = serial.Serial(port=PORT, baudrate=9600, timeout=0.1)

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)


class WaterSystem:
    def __init__(self):
        self.water_on = False

    def activate_water(self):
        if not self.water_on:
            arduino.write(b"WATER_ON\n")
            self.water_on = True
            return "Water system activated!"
        return "Water system is already on."

    def deactivate_water(self):
        if self.water_on:
            arduino.write(b"WATER_OFF\n")
            self.water_on = False
            return "Water system deactivated!"
        return "Water system is already off."


water_system = WaterSystem()


def send_alert(sensor_value):
    message = f"Alert! Sensor value is low: {sensor_value}. Consider watering the soil."
    bot.send_message(CHAT_ID, message)


@bot.message_handler(commands=["water"])
def handle_water_command(message):
    response = water_system.activate_water()
    bot.reply_to(message, response)


@bot.message_handler(commands=["stop_water"])
def handle_stop_water_command(message):
    response = water_system.deactivate_water()
    bot.reply_to(message, response)


@bot.message_handler(commands=["solo"])
def display_moisture_command(message):
    data = arduino.readline().decode().strip()
    print(data)
    try:
        sensor_data = json.loads(data)
        sensor_value = sensor_data["sensorValue"]

    except json.JSONDecodeError:
        print("Failed to decode JSON:", data)
        return

    if sensor_value < 80:
        bot.reply_to(
            message,
            f"Alert! Sensor value is low: {sensor_value}. Consider watering the soil.",
        )
        return
    bot.reply_to(message, f"Alert! Sensor value is good: {sensor_value}.")


# Function to continuously read data from Arduino and check sensor value
def monitor_sensor():
    while True:
        try:
            # Read data from Arduino
            data = arduino.readline().decode().strip()
            if data:
                try:
                    # Parse the JSON-like data from Arduino
                    sensor_data = json.loads(data)
                    sensor_value = sensor_data["sensorValue"]

                    # Check if the sensor value is below the threshold
                    # if sensor_value < 80:
                    #     send_alert(sensor_value)

                except json.JSONDecodeError:
                    print("Failed to decode JSON:", data)

        except serial.SerialException as e:
            print(f"Error reading from serial port: {e}")


if __name__ == "__main__":
    print("bot started")
    sensor_thread = Thread(target=monitor_sensor, daemon=True)  # Set daemon to True
    sensor_thread.start()

    try:
        bot.polling()
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")
