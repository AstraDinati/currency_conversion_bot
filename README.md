# Бот конвертер валют


## Описание проекта

Этот бот разработан с использованием библиотеки **[pyTelegramBotAPI](https://pytba.readthedocs.io/en/latest/)** и интегрирует внешний сервис **[FreeCurrencyAPI](https://freecurrencyapi.com/)** для предоставления последних данных о курсах валют. Он предлагает удобный способ мгновенного доступа к актуальной финансовой информации, делая процесс конвертации валют простым и интуитивно понятным. 

#### Список команд бота:
- /start - Начало работы с ботом
- /help - Вывод списка команд
- /currencies - Вывод списка валют, доступных для конвертации
- /convert <сумма> <из_валюты> to <в_валюту> - конвертация валют ![пример работы конвертации](https://i.imgur.com/Xt21cKd.png)

#### Полный список валют доступных для конвертации с помощью FreeCurrencyAPI:
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

#### Дополнитеьные функции бота:
>
> - Бот может распознавать 15 вариаций приветствий и прощаний от пользователя и соответствующе реагировать на них
> - В случае получения неизвестной команды или сообщения, бот вежливо предложит пользователю написать команду /help и ознакомиться со списком доступных команд
> - Бот ведёт логгирование всех действий пользователя и сохраняет информаци о них в файл с логами

#### Файловая структура проекта

- Чувствительные переменные такие как **TELEGRAM_BOT_TOKEN** и **FREECURRENCYAPI_KEY** находятся в файле *.env*. 
- Вся информация о необходимых для работы зависимостях и бибилиотеках находится в файле *requirements.txt*.
- Логи работы бота сохраняются в файл *bot_logs.log*