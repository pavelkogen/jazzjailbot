# jazzjailbot 
<img src="./cat.png" width="100" height="100">

Бот для ловли Джаза в Telegram 

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

## Linux Service

1. On **Linux** server copy file `jazzjail.service` file to `/etc/systemd/system/` on your Linux server;
   - Run:
     - `systemctl daemon-reload`;
     - `systemctl enable jazzjail.service`;
     - `systemctl start jazzjail.service`.

2 . File `jazzjail.service` contains default settings for ec2 server.
