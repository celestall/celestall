import requests
from aiogram import Bot, Dispatcher, types, executor

API_TOKEN = '7157325103:AAEiWnB3pWi8VQf9hC2zgxz9eaMP1Dg4Gk0'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
API_KEY = 'AQVN3O-5290wJ3JP3bcQAyEzNGC8CrO5Bz4P6xjX'

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.reply("П-п-привет")

async def get_response(message_text):
    prompt = {
    "modelUri": "gpt://b1go1t8vie998tqjdjhu/yandexgpt-lite",
    "completionOptions": {
        "stream": False,
        "temperature": 1,
        "maxTokens": "2000"
    },
    "messages": [
        {
            "role": "system",
            "text": "Ты - очень стестнительный человек, твоя задача отвечать так, будто ты стесняешься всех в мире. Отправляй эмодзи вместе с сообщениями"
        },
        {
            "role": "user",
            "text": message_text
        }
    ]
}



    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Api-Key {API_KEY}"
    }

    response = requests.post(url, headers=headers, json=prompt)
    print(response)
    result = response.json()
    print(result)
    return result['result']['alternatives'][0]['message']['text']

@dp.message_handler()
async def analize_message(message:types.Message):
    response_text = await get_response((message.text))
    await message.answer(response_text)

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)