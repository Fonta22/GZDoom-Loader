from pypresence import Presence
import time
import sys
import psutil
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

client_id = os.environ.get("APP_ID")
game = sys.argv[1]

if game == 'DOOM2':
    game = 'Doom II'
else:
    game = game.capitalize()

def checkProcess(processName):
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return False

RPC = Presence(client_id)

print(f'Загрузка {game}...')

RPC.connect()

RPC.update(
    details=f'Playing {game}',
    # state='ich bin tutorial',
    large_image='circle_gzdoom',
    large_text='GZDoom',
    start=time.time()
)

print(f'Running presence: {game}')

while True:
    if not checkProcess('gzdoom.exe'):
        print('')
        exit()