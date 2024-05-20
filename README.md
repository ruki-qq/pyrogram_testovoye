# pyrogram_testovoye
Бот-воронка

## Setup
Create environment vars from .env.example in your shell environment.(Postgres vars can also be in .env file.)

Go to **/bot** folder, create venv, run poetry install, run alembic upgrad, load messages and run bot:
```bash
  cd bot
  python -m venv venv
  source venv/bin/activate
  poetry install
  alembic upgrade head
  python load_msgs.py
  python main.py
```

### Docker Compose setup
To run with Docker Compose you must first create **session file** by login to your account with manual setup, then place _.env_ file to **/compose** folder and run:
```bash
  docker compose up
```
_.env_ file example can be located in **/infra**.
