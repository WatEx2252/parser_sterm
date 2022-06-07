# parser_sterm
В данный момент это обычный парсер площадки Steam собирает он данные только с игры Counter-Strike Global Offensive  
Upd. добален сбор данных с market.csgo.ru
в дальнейшем после парсинга ещё нескольких страниц, я займусь написанием бота/скрипта для авто покупки и продажи вокруг steam.  
Есть возможность сохранения данных в 3 форматах sql, excel и csv.   
Используемые технологии:  
Python:   
sql       => psycopg2 для подключения к БД.
pandas    => для хранения и преобразования данных.  
requests  => для отправления запросов на сервера steam.  
UserAgent => fake_useragent изменияем данные агента чтобы он не банил исходящие от нас запросы.  
time      => искусственное замедление работы парсера, так что бы запросы не банились.  
bs4       => для работы с полученной html страницей.
