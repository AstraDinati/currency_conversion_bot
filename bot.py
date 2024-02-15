from telebot import types
from telebot.async_telebot import AsyncTeleBot
import logging
import asyncio
import freecurrencyapi
import os
from dotenv import load_dotenv

# загрузка переменных окружения
load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = AsyncTeleBot(TELEGRAM_BOT_TOKEN)

# настройки логгирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="bot_logs.log",
    filemode="a",
)

logging.info("Bot started")

# создание подключения к freecurrencyapi
FREECURRENCYAPI_KEY = os.getenv("FREECURRENCYAPI_KEY")
client = freecurrencyapi.Client(FREECURRENCYAPI_KEY)


@bot.message_handler(commands=["start"])
async def send_welcome(message):
    logging.info(f"User {message.from_user.id} called {message.text}")
    await bot.reply_to(
        message,
        "Привет! Я бот для конвертации валют. Используй команду /help для получения списка команд.",
    )


@bot.message_handler(commands=["help"])
async def send_help(message):
    logging.info(f"User {message.from_user.id} called {message.text}")
    help_text = "Доступные команды:\n/start - начало работы\n/help - помощь\n/convert <сумма> <из_валюты> to <в_валюту> - конвертация валют\n/currencies - Список валют, доступных для конвертации"
    await bot.reply_to(message, help_text)


@bot.message_handler(commands=["convert"])
async def convert_currency(message):
    logging.info(f"User {message.from_user.id} requested conversion: {message.text}")
    try:
        params = message.text.split()[1:]
        if len(params) != 4 or params[2].lower() != "to":
            logging.info(
                f"User {message.from_user.id} requested conversion with wrong format: {message.text}"
            )
            raise ValueError(
                "Неверный формат. Используйте: /convert <сумма> <из_валюты> to <в_валюту>"
            )
        amount, from_currency, _, to_currency = params

        # последние курсы обмена
        result = client.latest(base_currency=from_currency, currencies=[to_currency])
        rate = result["data"][to_currency]

        converted_amount = float(amount) * rate
        await bot.reply_to(
            message, f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}"
        )

    except Exception as e:
        logging.exception("Conversion error", exc_info=e)
        await bot.reply_to(message, "Произошла ошибка при конвертации валют.")


# список доступных для пересчёта валют
@bot.message_handler(commands=["currencies"])
async def send_currencies(message):
    logging.info(f"User {message.from_user.id} called {message.text}")
    currency_list = """
Доступные валюты для конвертации:

- EUR: Euro
- USD: US Dollar
- JPY: Japanese Yen
- BGN: Bulgarian Lev
- CZK: Czech Republic Koruna
- DKK: Danish Krone
- GBP: British Pound Sterling
- HUF: Hungarian Forint
- PLN: Polish Zloty
- RON: Romanian Leu
- SEK: Swedish Krona
- CHF: Swiss Franc
- ISK: Icelandic Króna
- NOK: Norwegian Krone
- HRK: Croatian Kuna
- RUB: Russian Ruble
- TRY: Turkish Lira
- AUD: Australian Dollar
- BRL: Brazilian Real
- CAD: Canadian Dollar
- CNY: Chinese Yuan
- HKD: Hong Kong Dollar
- IDR: Indonesian Rupiah
- ILS: Israeli New Sheqel
- INR: Indian Rupee
- KRW: South Korean Won
- MXN: Mexican Peso
- MYR: Malaysian Ringgit
- NZD: New Zealand Dollar
- PHP: Philippine Peso
- SGD: Singapore Dollar
- THB: Thai Baht
- ZAR: South African Rand
    """
    await bot.reply_to(message, currency_list)


# приветствие и прощание или help
@bot.message_handler(func=lambda message: True)
async def greet_goodbye(message):
    logging.info(f"User {message.from_user.id} called {message.text}")
    text = message.text.lower()
    if any(
        greeting in text
        for greeting in [
            "привет",
            "здравствуй",
            "здравствуйте",
            "добрый день",
            "доброе утро",
            "добрый вечер",
            "приветствую",
            "салют",
            "хай",
            "хелло",
            "прив",
            "доброго времени суток",
            "доброго дня",
            "рад тебя видеть",
            "ку",
        ]
    ):
        await bot.reply_to(message, "Привет! Чем могу помочь?")
    elif any(
        goodbye in text
        for goodbye in [
            "пока",
            "до свидания",
            "до встречи",
            "всего доброго",
            "прощай",
            "до скорого",
            "до завтра",
            "всего хорошего",
            "будь здоров",
            "увидимся",
            "до следующего раза",
            "счастливо",
            "до новых встреч",
            "до скорой встречи",
            "до послезавтра",
        ]
    ):
        await bot.reply_to(message, "До встречи! Буду рад помочь вам снова.")
    else:
        await bot.reply_to(
            message,
            "Не уверен, как на это ответить. Используйте /help для списка команд.",
        )


if __name__ == "__main__":
    asyncio.run(bot.polling())
