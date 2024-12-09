<h1>Weather Update with Telegram and PostgreSQL</h1>
<h3>Overview</h3>
The Weather Update project is a simple application that allows users to fetch real-time weather updates for a specific city, send the updates to a Telegram group, and store the data in a PostgreSQL database. The project integrates the OpenWeatherMap API and Telegram Bot API to streamline the process of sharing and storing weather information.
<br>

<h3>Features<h3>
<h4>1) Real-Time Weather Fetching:</h4>
Fetches live weather data using the OpenWeatherMap API.

<h4>2) Telegram Integration:</h4>
Sends the fetched weather update as a message to a specific Telegram group or chat.

<h4>3) Data Storage in PostgreSQL:</h4>
Stores the weather update messages in a PostgreSQL database with timestamps for future reference.

<h4>4) Manual Trigger:</h4>
The process (fetching weather data, sending to Telegram, and saving to the database) is triggered manually by accessing a FastAPI endpoint.


<h3>Technologies Used</h3>
1) Backend: Python, FastAPI<br>
2) Database: PostgreSQL<br>
3) APIs:<br>
        1) OpenWeatherMap API for fetching weather data<br>
        2) Telegram Bot API for sending messages<br>
Other Tools: Requests library, psycopg2 for PostgreSQL integration<br>
