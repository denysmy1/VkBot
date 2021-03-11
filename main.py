from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.bot_longpoll import VkBotEventType
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import vk_api
import requests
import subprocess
import json
import re
from tram import Tram
import tram_rasp


class Server:

    def __init__(self, api_token, group_id, server_name: str = "Empty"):
        self.group_id = # айди группы в формате integer

        self.api_token = "Ваш токен"
        # Даем серверу имя
        self.server_name = server_name

        # Для Long Poll
        self.vk = vk_api.VkApi(token=api_token)

        # Для использования Long Poll API
        self.long_poll = VkBotLongPoll(self.vk, group_id, wait=100)

        # Для вызова методов vk_api
        self.vk_api = self.vk.get_api()

        self.valutes = ["Австралийский доллар", "Азербайджанский манат", "Фунт стерлингов Соединенного королевства",
                        "Армянских драмов", "Белорусский рубль", "Болгарский лев", "Бразильский реал",
                        "Венгерских форинтов",
                        "Гонконгских долларов",
                        "Датская крона", "Доллар США", "Евро", "Индийских рупий", "Казахстанских тенге",
                        "Канадский доллар",
                        "Киргизских сомов", "Китайский юань", "Молдавских леев", "Норвежских крон", "Польский злотый",
                        "Румынский лей", "СДР - специальные права заимствования", "Сингапурский доллар",
                        "Таджикских сомони", "Турецкая лира", "Новый туркменский манат", "Узбекских сумов",
                        "Украинских гривен", "Чешских крон", "Шведских крон", "Швейцарский франк",
                        "Южноафриканских рэндов",
                        "Вон Республики Корея", "Японских иен"]
        self.valuteskod = ["AUD", "AZN", "GBP", "AMD", "BYN", "BGN", "BRL", "HUF", "HKD", "DKK", "USD", "EUR", "INR",
                           "KZT",
                           "CAD", "KGS", "CNY", "MDL", "NOK", "PLN ", "RON", "XDR", "SGD", "TJS", "TRY", "TMT", "UZS",
                           "UAH",
                           "CZK", "SEK", "CHF", "ZAR", "KRW", "JPY"]
        self.citys = ["Москва", "Санкт-Петербург", "Краснодар", "Новосибирск", "Красноярск", "Владивосток",
                      "Ростов-На-Дону"]

        self.keyboard = VkKeyboard(one_time=True)
        self.keyboard.add_button('Погода❄⛈🌤', color=VkKeyboardColor.PRIMARY)
        self.keyboard.add_button('Последняя новость', color=VkKeyboardColor.PRIMARY)
        self.keyboard.add_line()
        self.keyboard.add_button('Расписание', color=VkKeyboardColor.POSITIVE)
        self.keyboard.add_button('Курс валют', color=VkKeyboardColor.POSITIVE)
        self.keyboard.add_line()
        self.keyboard.add_location_button()

        self.raspis = VkKeyboard(one_time=True)
        self.raspis.add_button('Москва', color=VkKeyboardColor.PRIMARY)
        self.raspis.add_button('Санкт-Петербург', color=VkKeyboardColor.PRIMARY)
        self.raspis.add_line()
        self.raspis.add_button('Краснодар', color=VkKeyboardColor.PRIMARY)
        self.raspis.add_button('Новосибирск', color=VkKeyboardColor.PRIMARY)
        self.raspis.add_line()
        self.raspis.add_button('Красноярск', color=VkKeyboardColor.PRIMARY)
        self.raspis.add_button('Владивосток', color=VkKeyboardColor.PRIMARY)
        self.raspis.add_line()
        self.raspis.add_button('Ростов-На-Дону', color=VkKeyboardColor.PRIMARY)
        self.raspis.add_line()
        self.raspis.add_button('Другой город', color=VkKeyboardColor.SECONDARY)
        self.raspis.add_button('Меню', color=VkKeyboardColor.SECONDARY)

        self.moneykb = VkKeyboard(one_time=True)
        self.moneykb.add_button('Доллар США и Евро', color=VkKeyboardColor.PRIMARY)
        self.moneykb.add_button('Курс биткоина', color=VkKeyboardColor.PRIMARY)
        self.moneykb.add_line()
        self.moneykb.add_button('Список валют', color=VkKeyboardColor.POSITIVE)
        self.moneykb.add_line()
        self.moneykb.add_button('Меню', color=VkKeyboardColor.SECONDARY)

        self.kblist1 = VkKeyboard(one_time=True)
        self.kblist1.add_button('Австралийский доллар', color=VkKeyboardColor.PRIMARY)
        self.kblist1.add_button('Азербайджанский манат', color=VkKeyboardColor.PRIMARY)
        self.kblist1.add_line()
        self.kblist1.add_button('Фунт стерлингов Соединенного королевства', color=VkKeyboardColor.PRIMARY)
        self.kblist1.add_button('Армянских драмов', color=VkKeyboardColor.PRIMARY)
        self.kblist1.add_line()
        self.kblist1.add_button('Белорусский рубль', color=VkKeyboardColor.PRIMARY)
        self.kblist1.add_button('Болгарский лев', color=VkKeyboardColor.PRIMARY)
        self.kblist1.add_line()
        self.kblist1.add_button('Бразильский реал', color=VkKeyboardColor.PRIMARY)
        self.kblist1.add_button('Китайский юань', color=VkKeyboardColor.PRIMARY)
        self.kblist1.add_line()
        self.kblist1.add_button('Гонконгских долларов', color=VkKeyboardColor.PRIMARY)
        self.kblist1.add_button('Датская крона', color=VkKeyboardColor.PRIMARY)
        self.kblist1.add_line()
        self.kblist1.add_button('Датская крона', color=VkKeyboardColor.PRIMARY)
        self.kblist1.add_button('Доллар США', color=VkKeyboardColor.PRIMARY)
        self.kblist1.add_line()
        self.kblist1.add_button('Евро', color=VkKeyboardColor.PRIMARY)
        self.kblist1.add_button('Индийских рупий', color=VkKeyboardColor.PRIMARY)
        self.kblist1.add_line()
        self.kblist1.add_button('Казахстанских тенге', color=VkKeyboardColor.PRIMARY)
        self.kblist1.add_button('Канадский доллар', color=VkKeyboardColor.PRIMARY)
        self.kblist1.add_line()
        self.kblist1.add_button('Меню', color=VkKeyboardColor.PRIMARY)
        self.kblist1.add_button('Далее', color=VkKeyboardColor.PRIMARY)

        self.kblist2 = VkKeyboard(one_time=True)
        self.kblist2.add_button('Казахстанских тенге', color=VkKeyboardColor.PRIMARY)
        self.kblist2.add_button('Канадский доллар', color=VkKeyboardColor.PRIMARY)
        self.kblist2.add_line()
        self.kblist2.add_button('Киргизских сомов', color=VkKeyboardColor.PRIMARY)
        self.kblist2.add_button('Венгерских форинтов', color=VkKeyboardColor.PRIMARY)
        self.kblist2.add_line()
        self.kblist2.add_button('Молдавских леев', color=VkKeyboardColor.PRIMARY)
        self.kblist2.add_button('Норвежских крон', color=VkKeyboardColor.PRIMARY)
        self.kblist2.add_line()
        self.kblist2.add_button('Польский злотый', color=VkKeyboardColor.PRIMARY)
        self.kblist2.add_button('Румынский лей', color=VkKeyboardColor.PRIMARY)
        self.kblist2.add_line()
        self.kblist2.add_button('СДР - специальные права заимствования', color=VkKeyboardColor.PRIMARY)
        self.kblist2.add_button('Сингапурский доллар', color=VkKeyboardColor.PRIMARY)
        self.kblist2.add_line()
        self.kblist2.add_button('Таджикских сомони', color=VkKeyboardColor.PRIMARY)
        self.kblist2.add_button('Турецкая лира', color=VkKeyboardColor.PRIMARY)
        self.kblist2.add_line()
        self.kblist2.add_button('Новый туркменский манат', color=VkKeyboardColor.PRIMARY)
        self.kblist2.add_button('Венгерских форинтов', color=VkKeyboardColor.PRIMARY)
        self.kblist2.add_line()
        self.kblist2.add_button('Узбекских сумов', color=VkKeyboardColor.PRIMARY)
        self.kblist2.add_button('Украинских гривен', color=VkKeyboardColor.PRIMARY)
        self.kblist2.add_line()
        self.kblist2.add_button('Чешских крон', color=VkKeyboardColor.PRIMARY)
        self.kblist2.add_button('Шведских крон', color=VkKeyboardColor.PRIMARY)
        self.kblist2.add_line()
        self.kblist2.add_button('Нaзад', color=VkKeyboardColor.PRIMARY)
        self.kblist2.add_button('Далeе', color=VkKeyboardColor.PRIMARY)

        self.kblist3 = VkKeyboard(one_time=True)
        self.kblist3.add_button('Швейцарский франк', color=VkKeyboardColor.PRIMARY)
        self.kblist3.add_button('Южноафриканских рэндов', color=VkKeyboardColor.PRIMARY)
        self.kblist3.add_line()
        self.kblist3.add_button('Вон Республики Корея', color=VkKeyboardColor.PRIMARY)
        self.kblist3.add_button('Японских иен', color=VkKeyboardColor.PRIMARY)
        self.kblist3.add_line()
        self.kblist3.add_button('Назaд', color=VkKeyboardColor.PRIMARY)
        self.kblist3.add_button('Меню', color=VkKeyboardColor.PRIMARY)

        self.tram1 = Tram()

    def start(self):
        for event in self.long_poll.listen():  # Слушаем сервер

            # Пришло новое сообщение
            if event.type == VkBotEventType.MESSAGE_NEW:
                comand = ""
                wlst = event.object.text.split()
                if len(wlst) == 2:
                    comand = str(wlst[0]).lower()
                print('Текст сообщения: ' + str(event.object.text))
                response = event.object.text.lower()
                if event.object.peer_id and not event.object.peer_id < 0 and not event.object.from_me:
                    if response == "погода❄⛈🌤" or response == "погода":
                        self.vk.method('messages.send',
                                       {'peer_id': event.object.peer_id, 'message': "Город:",
                                        'random_id': get_random_id(), 'keyboard': self.raspis.get_keyboard()})
                    elif any([re.search(weat, event.object.text) for weat in self.citys]):
                        self.vk.method('messages.send',
                                       {'peer_id': event.object.peer_id,
                                        'message': requests.get(
                                            'https://wttr.in/' + event.object.text + '?format=Город: %l ,'
                                                                                     'Температура воздуха: %t%c ,По ощущению: %f ,'
                                                                                     'Ветер: %w ,Осадки: %p').text.replace(
                                            ',', '\n'),
                                        'random_id': get_random_id(), 'keyboard': self.keyboard.get_keyboard()})
                    elif response == "другой город":
                        self.vk.method('messages.send',
                                       {'peer_id': event.object.peer_id,
                                        'message': "Чтобы посмотреть погоду в любом городе мира - введите команду"
                                                   " <<Погода город>>",
                                        'random_id': get_random_id(), 'keyboard': self.keyboard.get_keyboard()})
                    elif comand == "погода" and len(wlst) == 2:
                        self.vk.method('messages.send',
                                       {'peer_id': event.object.peer_id, 'message': weather(wlst[1]),
                                        'random_id': get_random_id(), 'keyboard': self.keyboard.get_keyboard()})
                    elif response == "последняя новость":
                        self.vk.method('messages.send',
                                       {'peer_id': event.object.peer_id,
                                        'message': news(),
                                        'random_id': get_random_id(), 'keyboard': self.keyboard.get_keyboard()})
                    elif response == "курс валют":
                        self.vk.method('messages.send',
                                       {'peer_id': event.object.peer_id,
                                        'message': "Выберете валюту",
                                        'random_id': get_random_id(), 'keyboard': self.moneykb.get_keyboard()})
                    elif response == "доллар сша и евро":
                        self.vk.method('messages.send',
                                       {'peer_id': event.object.peer_id,
                                        'message': self.money(),
                                        'random_id': get_random_id(), 'keyboard': self.keyboard.get_keyboard()})
                    elif response == "список валют":
                        self.vk.method('messages.send',
                                       {'peer_id': event.object.peer_id,
                                        'message': "Страница1",
                                        'random_id': get_random_id(), 'keyboard': self.kblist1.get_keyboard()})
                    elif response == "далее":
                        self.vk.method('messages.send',
                                       {'peer_id': event.object.peer_id,
                                        'message': "Страница 2",
                                        'random_id': get_random_id(), 'keyboard': self.kblist2.get_keyboard()})
                    elif response == "далeе":
                        self.vk.method('messages.send',
                                       {'peer_id': event.object.peer_id,
                                        'message': "Страница 3",
                                        'random_id': get_random_id(), 'keyboard': self.kblist3.get_keyboard()})
                    elif response == "далеe":
                        self.vk.method('messages.send',
                                       {'peer_id': event.object.peer_id,
                                        'message': "Страница 4",
                                        'random_id': get_random_id(), 'keyboard': self.kblist4.get_keyboard()})
                    elif response == "нaзад":
                        self.vk.method('messages.send',
                                       {'peer_id': event.peer_id,
                                        'message': "Страница 1",
                                        'random_id': get_random_id(), 'keyboard': self.kblist1.get_keyboard()})
                    elif response == "назaд":
                        self.vk.method('messages.send',
                                       {'peer_id': event.object.peer_id,
                                        'message': "Страница 2",
                                        'random_id': get_random_id(), 'keyboard': self.kblist2.get_keyboard()})
                    elif any([re.search(val, event.object.text) for val in self.valutes]):
                        for num in range(len(self.valutes)):
                            if event.object.text == self.valutes[num]:
                                break
                        nlav = self.valuteskod[num]
                        self.vk.method('messages.send',
                                       {'peer_id': event.object.peer_id,
                                        'message': self.indmoney(nlav),
                                        'random_id': get_random_id(), 'keyboard': self.keyboard.get_keyboard()})
                    elif response == "курс биткоина":
                        btc = requests.get("https://apirone.com/api/v1/ticker?currency=btc")
                        btc_json = json.loads(btc.text)
                        bt = btc_json['RUB']['last']
                        self.vk.method('messages.send',
                                       {'peer_id': event.object.peer_id,
                                        'message': "BTC к RUB = " + str(round(bt, 4)),
                                        'random_id': get_random_id(), 'keyboard': self.keyboard.get_keyboard()})
                    elif response == "расписание":
                        self.vk.method('messages.send',
                                       {'peer_id': event.object.peer_id,
                                        'message': "Город",
                                        'random_id': get_random_id(), 'keyboard': self.tram1.t_k_rasp.get_keyboard()})
                    elif response == "трамвай":
                        self.vk.method('messages.send',
                                       {'peer_id': event.object.peer_id,
                                        'message': "Маршрут",
                                        'random_id': get_random_id(), 'keyboard': self.tram1.t_k_marsh.get_keyboard()})
                    elif response == "kраснодар":
                        self.vk.method('messages.send',
                                       {'peer_id': event.object.peer_id,
                                        'message': "Транспорт",
                                        'random_id': get_random_id(), 'keyboard': self.tram1.rasp.get_keyboard()})
                    elif comand == "кт":
                        self.vk.method('messages.send',
                                       {'peer_id': event.object.peer_id,
                                        'message': tram_rasp.start(wlst[1]),
                                        'random_id': get_random_id(), 'keyboard': self.keyboard.get_keyboard()})
                    elif response == "вернуть":
                        self.vk.method('messages.send',
                                       {'peer_id': event.object.peer_id,
                                        'message': "Транспорт",
                                        'random_id': get_random_id(), 'keyboard': self.tram1.rasp.get_keyboard()})
                    elif response == "троллейбус":
                        self.vk.method('messages.send',
                                       {'peer_id': event.object.peer_id,
                                        'message': "Маршрут",
                                        'random_id': get_random_id(), 'keyboard': self.tram1.tl_k_marsh.get_keyboard()})
                    elif comand == "ктл":
                        self.vk.method('messages.send',
                                       {'peer_id': event.object.peer_id,
                                        'message': tram_rasp.krastrolleybus(wlst[1]),
                                        'random_id': get_random_id(), 'keyboard': self.keyboard.get_keyboard()})
                    elif response == "автобус":
                        self.vk.method('messages.send',
                                       {'peer_id': event.object.peer_id,
                                        'message': "Маршрут",
                                        'random_id': get_random_id(), 'keyboard': self.tram1.b_k_marsh.get_keyboard()})
                    elif comand == "ат":
                        self.vk.method('messages.send',
                                       {'peer_id': event.object.peer_id,
                                        'message': tram_rasp.krasbus(wlst[1]),
                                        'random_id': get_random_id(), 'keyboard': self.keyboard.get_keyboard()})
                    elif response == "рoстов-на-дону":
                        self.vk.method('messages.send',
                                       {'peer_id': event.object.peer_id,
                                        'message': "Транспорт",
                                        'random_id': get_random_id(), 'keyboard': self.tram1.raspr.get_keyboard()})
                    elif response == "aвтобус":
                        self.vk.method('messages.send',
                                       {'peer_id': event.object.peer_id,
                                        'message': "Маршрут",
                                        'random_id': get_random_id(), 'keyboard': self.tram1.b_r_marsh.get_keyboard()})
                    elif comand == "ар":
                        self.vk.method('messages.send',
                                       {'peer_id': event.object.peer_id,
                                        'message': tram_rasp.rastbus(wlst[1]),
                                        'random_id': get_random_id(), 'keyboard': self.keyboard.get_keyboard()})
                    elif response == "дальшe":
                        self.vk.method('messages.send',
                                       {'peer_id': event.object.peer_id,
                                        'message': "Страница 2",
                                        'random_id': get_random_id(), 'keyboard': self.tram1.b_r_marsh2.get_keyboard()})
                    elif response == "дaльше":
                        self.vk.method('messages.send',
                                       {'peer_id': event.object.peer_id,
                                        'message': "Страница 3",
                                        'random_id': get_random_id(), 'keyboard': self.tram1.b_r_marsh3.get_keyboard()})
                    elif response == "вперед":
                        self.vk.method('messages.send',
                                       {'peer_id': event.object.peer_id,
                                        'message': "Страница 4",
                                        'random_id': get_random_id(), 'keyboard': self.tram1.b_r_marsh4.get_keyboard()})
                    elif response == "вeрнуть":
                        self.vk.method('messages.send',
                                       {'peer_id': event.object.peer_id,
                                        'message': "Страница 1",
                                        'random_id': get_random_id(), 'keyboard': self.tram1.b_r_marsh.get_keyboard()})
                    elif response == "bернуть":
                        self.vk.method('messages.send',
                                       {'peer_id': event.object.peer_id,
                                        'message': "Страница 2",
                                        'random_id': get_random_id(), 'keyboard': self.tram1.b_r_marsh2.get_keyboard()})
                    elif response == "beрнуть":
                        self.vk.method('messages.send',
                                       {'peer_id': event.object.peer_id,
                                        'message': "Страница 3",
                                        'random_id': get_random_id(), 'keyboard': self.tram1.b_r_marsh3.get_keyboard()})
                    elif response == "tроллейбус":
                        self.vk.method('messages.send',
                                       {'peer_id': event.object.peer_id,
                                        'message': "Маршрут",
                                        'random_id': get_random_id(), 'keyboard': self.tram1.tl_r_marsh.get_keyboard()})
                    elif comand == "тлр":
                        self.vk.method('messages.send',
                                       {'peer_id': event.object.peer_id,
                                        'message': tram_rasp.rastrolleubus(wlst[1]),
                                        'random_id': get_random_id(), 'keyboard': self.keyboard.get_keyboard()})
                    elif response == "tрамвай":
                        self.vk.method('messages.send',
                                       {'peer_id': event.object.peer_id,
                                        'message': "Маршрут",
                                        'random_id': get_random_id(), 'keyboard': self.tram1.t_r_marsh.get_keyboard()})
                    elif comand == "тр":
                        self.vk.method('messages.send',
                                       {'peer_id': event.object.peer_id,
                                        'message': tram_rasp.rastram(wlst[1]),
                                        'random_id': get_random_id(), 'keyboard': self.keyboard.get_keyboard()})
                    elif response == "межгородской":
                        self.vk.method('messages.send',
                                       {'peer_id': event.object.peer_id,
                                        'message': "Маршрут",
                                        'random_id': get_random_id(), 'keyboard': self.tram1.no_city_rast.get_keyboard()})
                    elif comand == "мгр":
                        self.vk.method('messages.send',
                                       {'peer_id': event.object.peer_id,
                                        'message': tram_rasp.mrast(wlst[1]),
                                        'random_id': get_random_id(), 'keyboard': self.keyboard.get_keyboard()})
                    else:
                        self.vk.method('messages.send',
                                       {'peer_id': event.object.peer_id,
                                        'message': "Доступные команды",
                                        'random_id': get_random_id(), 'keyboard': self.keyboard.get_keyboard()})


    def money(self):
        mny = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
        s = json.loads(mny.text)
        usd = s['Valute']['USD']['Value']
        eur = s['Valute']['EUR']['Value']
        raznusd = s['Valute']['USD']['Value'] - s['Valute']['USD']['Previous']
        razneur = s['Valute']['EUR']['Value'] - s['Valute']['EUR']['Previous']
        if raznusd > 0:
            endusd = s['Valute']['USD']['Name'] + " " + str(round(usd, 4)) + " ⬆ " + str(round(raznusd, 4))
        else:
            endusd = s['Valute']['USD']['Name'] + " " + str(round(usd, 4)) + " ⬇ " + str(round(raznusd, 4))
        if razneur > 0:
            endeur = s['Valute']['EUR']['Name'] + " " + str(round(eur, 4)) + " ⬆ " + str(round(razneur, 4))
        else:
            endeur = s['Valute']['EUR']['Name'] + " " + str(round(eur, 4)) + " ⬇ " + str(round(razneur, 4))
        endmoney = endusd + "\n" + endeur
        return endmoney

    def indmoney(self, st):
        mny = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
        s = json.loads(mny.text)
        val = s['Valute'][st]['Value']
        raznval = s['Valute'][st]['Value'] - s['Valute'][st]['Previous']
        if raznval > 0:
            endval = s['Valute'][st]['Name'] + " " + str(round(val, 4)) + " ⬆ " + str(round(raznval, 4))
        else:
            endval = s['Valute'][st]['Name'] + " " + str(round(val, 4)) + " ⬇ " + str(round(raznval, 4))
        return endval


def weather(s):
    st = s[0]
    s = s.replace(st, st.upper(), 1)
    weath = requests.get('https://wttr.in/' + s + '?format=Город: %l ,Температура воздуха: %t%c ,'
                                                  'По ощущению: %f ,Ветер: %w ,Осадки: %p').text

    return weath.replace(',', '\n')


def news():
    new = subprocess.check_output(['./test.sh'])
    return new
