import os
import requests
import asyncio
from bs4 import BeautifulSoup
from telegram.ext import ApplicationBuilder

BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHANNEL_ID = os.environ.get('CHANNEL_ID')

# Jan 5 2026 Relaunch

# Create the Application and pass it your bot's token.
async def send_daily_message(app):
    url = "https://www.gismeteo.kz/weather-astana-5164/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    soup = BeautifulSoup(requests.get(url, headers=headers).text, 'html.parser')
    weather_div = soup.find('div', class_='weather-feel')
    temp_tag = weather_div.find('temperature-value')

    # Get the value attribute
    temperature = temp_tag['value']
    print(temperature)  # Print the extracted temperature value

    await app.bot.send_message(chat_id=CHANNEL_ID, text=f"Today in Astana, it feels like {temperature}°C")

async def run_app():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Start the application (polling won't be strictly necessary if only scheduling)
    await app.initialize()
    await app.start()
    
    await send_daily_message(app)  # Await the async function

    await app.stop()

if __name__ == '__main__':
    asyncio.run(run_app())  # Use asyncio.run() to run the async function