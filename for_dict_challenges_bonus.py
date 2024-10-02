"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений.
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
import random
import uuid
import datetime
from collections import Counter
import lorem
from itertools import groupby


def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list(
        {random.randint(1, 10000) for _ in range(random.randint(5, 20))}
    )
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice(
                [
                    None,
                    (
                        random.choice([m["id"] for m in messages])
                        if messages else None
                    ),
                ],
            ),
            "seen_by": random.sample(users_ids,
                                     random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    return messages

def get_max_messages(messages): #функция считает айди пользователя, который написал больше всех сообщений
    """
    создаем пустой список и словарь. В список собираем все id пользователей, 
    в словаре в виде ключ:значение храним id пользователя и сколько раз он написал сообщение: {id:id_count}
    """
    """
    lists = []
    user_id = {}

    for i in range(0, len(messages)):
        id = messages[i]['sent_by'] #пробигаемся по списку словарей с сообщениями и "выдергиваем" из словарей id пользователя
        lists.append(id) #добавляем id пользователя в список
    
    for i in range(0, len(lists)):
        user_id[lists[i]] = lists.count(lists[i]) #теперь пробигаемся по списку с id и считаем сколько раз каждый id встретился в списке
        max_key = max(user_id, key = user_id.get)
    return max_key
    """
    sent_by_counts = Counter(message['sent_by'] for message in messages)
    most_messages_user = sent_by_counts.most_common(1)
    if most_messages_user:
        user_id, count = most_messages_user[0]
        return user_id, count
        
        #print(f'Пользователь с id {user_id} отправил больше всего сообщений: {count}.')
    else:
        print('Нет отправленных сообщений.')


def printing(messages):
    for message in messages:
        print(message, end='\n*********************************************************************************************************************\n')


def get_id_of_max_reply_message(threads, messages):
    for message in messages:
        if threads == message['id']:
            return message['sent_by']
        
def get_user_id_seen_by_max_users(messages):
    max_seen_by = 0
    for message in messages:
        new_message_seen_by = [i for i, _ in groupby(message['seen_by'])]
        seen_by = len(new_message_seen_by)    
        if seen_by > max_seen_by:
            max_seen_by = seen_by
            id = message['sent_by']
    return max_seen_by, id 

def max_time_for_messages(messages):
    before_12 = 0
    between_12_18 = 0
    after_18 = 0
    
    for message in messages:
        time = message['sent_at']
        if time.hour <=12:
            before_12 += 1
        elif time.hour >=12 and time.hour <=18:
            between_12_18 += 1
        else:
            after_18 += 1 
        
    if between_12_18 <  before_12 > after_18:
        return "больше всего сообщений утром (до 12)"
    elif before_12 < between_12_18 > after_18:
        return 'больше всего сообщений днем (с 12 до 18)'
    else:
        return 'больше всего сообщений вечером (после 18)' 
    


def get_max_threds(messages):
    lists =[]
    message_id = {}

    for i in range(0, len(messages)):
        id = messages[i]['reply_for']
        lists.append(id)

    for i in range(0, len(lists)):
        message_id[lists[i]] = lists.count(lists[i])
        
    sorted_message_id = sorted(message_id.items(), key=lambda item: item[1], reverse=True)
    if sorted_message_id[0][0] == None:
        return sorted_message_id[1][0]
    else:
        return sorted_message_id[0][0]


if __name__ == "__main__":
    messages = generate_chat_history()
    printing(messages)
    print(f"айди пользователя с максимальным числом отправленных сообшений:{get_max_messages(messages)[0]}, число сообщений от пользователя: {get_max_messages(messages)[1]}",
          f"айди пользователя на сообщение которого больше всего отвечали: {get_id_of_max_reply_message(get_max_threds(messages), messages)}",
          f"айди пользователя, сообщения которого видело больше всего уникальных пользователей:{get_user_id_seen_by_max_users(messages)[1]}",
          max_time_for_messages(messages),
          f"идентификатор сообщений, который стал началом для самых длинных тредов (цепочек ответов):{get_max_threds(messages)}", sep='\n')
    
