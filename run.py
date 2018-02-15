# run.py

import os
from os.path import join, dirname

from dotenv import load_dotenv

from app import create_app

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

config_name = os.getenv('FLASK_CONFIG')
print(config_name)
app = create_app(config_name)

if __name__ == '__main__':
    app.run()