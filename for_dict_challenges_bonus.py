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
    print(sent_by_counts)
    # Нахождение пользователя с максимальным количеством сообщений
    most_messages_user = sent_by_counts.most_common(1)
    print(most_messages_user)
    if most_messages_user:
        user_id, count = most_messages_user[0]
        print(f'Пользователь с id {user_id} отправил больше всего сообщений: {count}.')
    else:
        print('Нет отправленных сообщений.')


def get_max_threds(messages):
    lists =[]
    message_id = {}

    for i in range(0, len(messages)):
        id = messages[i]['reply_for']
        lists.append(id)

    for i in range(0, len(lists)):
        message_id[lists[i]] = lists.count(lists[i])
        
    sorted_message_id = sorted(message_id.items(), key=lambda item: item[1], reverse=True)
    #max_key = max(message_id, key = message_id.get)
    if sorted_message_id[0][0] == None:
        return sorted_message_id[1][0]
    else:
        return sorted_message_id[0][0]


if __name__ == "__main__":
    messages = generate_chat_history()
    print(f"ID пользователя, который написал больше всех сообщений:{get_max_messages(messages)}",
          f"идентификатор сообщений, который стал началом для самых длинных тредов (цепочек ответов):{get_max_threds(messages)}", sep='\n')
