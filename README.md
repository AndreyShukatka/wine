# Новое русское вино

  Сайт магазина авторского вина "Новое русское вино".
  
## Подготовка данных
Создайте файл Excel, содержащий следующие колонки 
`Категория \	Название \	Сорт \	Цена \	Картинка \	Акция`  
и заполните его данными

## Запуск

- Скачайте код
- Установите зависимости `pip3 install -r requirements.txt`
- Запустите сайт командой `python3 main.py -wp далее ваш путь к файлу с винами в формате xlsx`, по умолчанию стоит файл 'wine.xlsx' из сборки
- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000). 

## main.py
  Данный скрипт из файла `wine.xlsx` достаёт данные о винах и переносит их на сайт в файл `template.html`. 
  А после создаёт на основе `template.html` файл `index.html`, который уже виден как стартовая страница в интернете.

  При изменениях информации в файле `wine.xlsx` необходимо перезапускать `main.py`, для обновления информации на сайте.

### Файл `main.py` содержит следующие функции:
 ### get_wines()
  Данная функция преобразует информацию из файла `wine.xlsx` в словари, использую при помощи библиотеки `collections`

 ### calc_age_string(last_digit)
  Данная функция получает на вход последнюю цифру из числа равного колличеству лет, сколько существует данная винодельня
  и выдает в соответствии со скриптом, какое слово будет подставляться на сайте. Пример: `'Уже 102 года с вами'`, `'Уже 105 лет с вами'`.



        
