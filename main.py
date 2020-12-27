key = '3ac9704c2708e6d299a2a91f7e52b6139c6a249a68a9418a7e94fbfa6855f0977df37b943b42b02745daa'

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

vk_session = vk_api.VkApi(token=key)
longpoll = VkLongPoll(vk_session)

vk = vk_session.get_api()

keyboard = VkKeyboard(one_time=True)
keyboard.add_button('Hi!', color=VkKeyboardColor.POSITIVE)
keyboard.add_button('Bye', color=VkKeyboardColor.NEGATIVE)
keyboard.add_line()
keyboard.add_location_button()
keyboard.add_line()
keyboard.add_button('Nothing', color=VkKeyboardColor.SECONDARY)


for e in longpoll.listen():
    if e.type == VkEventType.MESSAGE_NEW and e.text and e.to_me:
        if e.text == "Начать":
            vk.messages.send(
                user_id=e.user_id,
                random_id=get_random_id(),
                keyboard=keyboard.get_keyboard(),
                message='Начинаем'
            )

        elif e.text == "Hi!":
            vk.messages.send(
                user_id=e.user_id,
                random_id=get_random_id(),
                message='Здравствуйте!'
            )

        elif e.text == "Bye":
            vk.messages.send(
                user_id=e.user_id,
                random_id=get_random_id(),
                message='Аста ла виста, беби!'
            )