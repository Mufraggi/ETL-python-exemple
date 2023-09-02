import json

import pika as pika

from src.receivers.pokemon_api_receivers import callback_pokemon_api_call, queue_api_sync
from src.receivers.pokemon_sync_production import callback_pokemon_sync_production, queue_sync_production

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost', port=5672))
channel = connection.channel()

channel.queue_declare(queue=queue_api_sync)
channel.queue_declare(queue=queue_sync_production)

channel.basic_consume(queue=queue_api_sync, on_message_callback=callback_pokemon_api_call, auto_ack=True)
channel.basic_consume(queue=queue_sync_production, on_message_callback=callback_pokemon_sync_production, auto_ack=True)

print('En attente de messages dans la file d\'attente A. Pour quitter, appuyez sur CTRL+C')

for id in range(1011):
    print(id)
    message = json.dumps({"id": str(id)})
    print(message)
    channel.basic_publish(exchange='', routing_key=queue_api_sync, body=message)

channel.start_consuming()
