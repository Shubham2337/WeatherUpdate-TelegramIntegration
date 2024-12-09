import requests
import psycopg2
from fastapi import FastAPI
from telegram import Bot
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)


DATABASE_URL = "postgresql://postgres:admin%40123@localhost:5432/weather_db"
TELEGRAM_TOKEN = "8081312859:AAGUn71RgUiIjyoekgs0XFG8A75xffzE2RI"
TELEGRAM_CHAT_ID = "-1002382031337"  
API_KEY = "d6dad889673868dfe97c7f0968a3775a"
CITY = "Pune"

# Initialize the bot
bot = Bot(token=TELEGRAM_TOKEN)


def fetch_weather_data():
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()

        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        message = f"Weather update for {CITY}: Temperature: {temperature}°C, Condition: {weather_description}"
        return message
    except requests.RequestException as e:
        logging.error(f"Failed to fetch weather data: {e}")
        return None


def save_weather_data_to_db(weather_message: str):
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS weather_updates (
                id SERIAL PRIMARY KEY,
                message TEXT NOT NULL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        cursor.execute('INSERT INTO weather_updates (message) VALUES (%s)', (weather_message,))
        conn.commit()
        cursor.close()
        conn.close()
        logging.info("Weather data saved to database successfully.")
    except Exception as e:
        logging.error(f"Failed to save weather data to database: {e}")


async def send_weather_to_telegram():
    weather_message = fetch_weather_data()
    if weather_message:
        try:
            await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=weather_message)
            logging.info("Weather update sent to Telegram group successfully.")
            save_weather_data_to_db(weather_message)
        except Exception as e:
            logging.error(f"Failed to send message to Telegram: {e}")
    else:
        logging.error("Weather message is empty. Skipping Telegram message.")


@app.get("/")
async def read_root():
    await send_weather_to_telegram()
    return {"message": "Weather update sent to the Telegram group."}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
