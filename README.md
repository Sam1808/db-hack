### Набор скриптов для правки базы данных [Электронного дневника школы](https://github.com/devmanorg/e-diary/tree/master)


#### Преамбула
Короче Ваня, похоже мне таки удалось это сделать... Наваять несколько скриптов для "работы" с базой данных электронного дневника.
Считай велик у тебя в кармане ;). Только будь внимателен и аккуратен, не увлекайся, а то нас раскроют... 

#### Как подключить скрипты?
Программист ты хоть и начинающий, но добраться до нужной базы данных (БД), уверен, сможешь... 
как никак уже 6-й класс заканчивается, считай взрослая жизнь.

Как отыщешь базу запускай консоль Django:
`python3 manage.py shell`

Получилось? Смело клади рядом с файликом `manage.py` файл из этого репозитория `scripts.py`, после чего перед тобой два пути: 
 - "копипастим" содержимое `scripts.py` прямо в консоль.., но copy-paste это детский сад, не так ли?
 -  импортируем файл прямо в консоль командой
 `from scripts import *`

И наслаждаемся магией Django ORM... :)
 
#### Доступные функции
Тут Ваня будь внимателен, если будешь делать все верно, значит все у тебя получится.
 И самое главное - не торопись, дочитай до конца, а потом уже пробуй пользовать функционал.
 Итак приступим... 
 
##### Функция "Долой плохие оценки!"
Функция называется `fix_marks` - удаляет все тройки, двойки... да хоть нули и вместо них ставит пятерки. Перед запуском определись кому будешь делать добро, например, что бы поправить успеваемость себе-любмому, смело запускай: 
 
 `fix_marks('Фролов Иван')`
 
**Важно:** 
  - Оценок много, скрипту для обработки нужно время. Наберись терпения.
  - Дневник хоть и "электронный", но соображает не всегда правильно. `Иван Фролов` для него не существует, а `Фролов Иван` есть...
  Всегда начинай с фамилии. Это хорошо, что в школе у нас нет полных тезок (удивительно, правда?), а то бы ещё пришлось Отчество добавлять.

И да, чуть не забыл... Если ошибешься (неправильно ФИО укажешь, или только Имя) скрипт об этом сообщит, я это предусмотрел.
 
 ##### Функция "Какие такие... замечания?"
Функция называется `remove_chastisements`, удаляет все замечания, которые тебе понаписали. Ох и любят эти преподы пожаловаться... Математик, Флоря Котов, тоже на меня косо смотрит... Особенностей у функции нет, запускается аналогично, работает быстро. Дерзай!
 
 `remove_chastisements('Фролов Иван')`
 
##### Функция "Похвали меня!"
  Когда удалили все замечания, нужно их чем то заменить, так? Для этого наваял функцию `create_commendation` - добавляет тебе похвалу по указанному тобой предмету за последний урок. При запуске укажи ФИО и предмет, например: 
  
  `create_commendation('Фролов Иван', 'Литература')`
  
  Я тебе ещё список стандартных хвалебных песен туда включил, чтоб само случайно выбиралось.
  
  **Важно:** Проверку неверного ФИО я тебе сделал, а вот правильность предметов скрипт проверять не умеет. Будь внимателен, ошибёшься - скрипт вылетит, начинай сначала. 
  Проверку такую сделать могу, но только после того как дашь на новом велике погонять. Ты обещал! 
  
 #### P.S.
 Вроде все... ничего не упустил... Если что не понятно - маякуй. Пользуй скрипты сколько душе угодно, вот только просьба у меня... Ты Силину Светку знаешь? Из 5В? Давай ей сюрприз сделаем? Уж больно мне нравится она... 
 - `fix_marks('Силина Светлана')`  - уберем плохие оценки
 - `remove_chastisements('Силина Светлана')`- сотрем замечания, если были
 -  `create_commendation('Силина Светлана', 'Иностранный язык')`  - похвалим по английскому, а то он что то у нее не идет..
 Спасибо!
 
 
 #### Описание
 Код написан в образовательных целях. 
 Учим Django ORM.
 Эпистолярный жанр сохранен. 
 Спасибо [Devman!](https://dvmn.org)
