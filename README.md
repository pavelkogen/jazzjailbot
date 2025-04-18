# jazzjailbot
Бот для ловли Джаза в Telegram

<img src="./cat.png" align="left" width="300" height="300">

# Setup

## Prepare Virtual Environment

1. Install Python >= 3.8.5

2. Create Virtual Environment:`python3 -m venv venv`;
   > Instead of "python3" may use "python" or another, check system PATH variable!

3. Activate Virtual Environment:
   - On **Unix or MacOS**, run: `source venv/bin/activate`;
   - On **Windows**, run: `.\venv\Scripts\activate`.

## Prepare Python Libraries
#### File requirements.txt contents list of Python libs to be installed

1. When you are in **(venv)** run: `pip install -r requirements.txt`.

## Update Environment Variables

1. Copy JazzBot/env_example to JazzBot/.env
   - On **Unix or MacOS**, run: `cp JazzBot/env_example JazzBot/.env`;
   - On **Windows**, run: 
     - `cd .\JazzBot\`;
     - `copy env_example .env`;
     - `cd ..`.

2. Open .env file and fill variable values out

## Run Bot

1. When you are in **(venv)** run: `python main.py`.
