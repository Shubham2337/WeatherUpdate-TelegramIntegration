<h2>Weather Update with Telegram and PostgreSQL</h2>
Overview
The Weather Update project is a simple application that allows users to fetch real-time weather updates for a specific city, send the updates to a Telegram group, and store the data in a PostgreSQL database. The project integrates the OpenWeatherMap API and Telegram Bot API to streamline the process of sharing and storing weather information.

Features
Real-Time Weather Fetching:

Fetches live weather data using the OpenWeatherMap API.
Telegram Integration:

Sends the fetched weather update as a message to a specific Telegram group or chat.
Data Storage in PostgreSQL:

Stores the weather update messages in a PostgreSQL database with timestamps for future reference.
Manual Trigger:

The process (fetching weather data, sending to Telegram, and saving to the database) is triggered manually by accessing a FastAPI endpoint.
Technologies Used
Backend: Python, FastAPI
Database: PostgreSQL
APIs:
OpenWeatherMap API for fetching weather data
Telegram Bot API for sending messages
Other Tools: Requests library, psycopg2 for PostgreSQL integration
