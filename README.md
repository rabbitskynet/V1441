# ponyauto

users (Пользователи)

    -login (логин)
    -pass (пароль)
    -email (email)
    -FIO (ФИО)
    -telephone (телефон)
    -adv (обьявления)
    -county (страна)
    -city (город)
    -moderator (является ли модератором)
    primary key (login)
	
advs (Обьявления)

    -name (название)
    -user (пользователь)
    -autoname (автомобиль)
    -automark (автомобиль)
    -descrition (описание)
    -year (год выпуска)
    -gearbox (кпп)
    -owners (владельцы)
    -price (цена)
    -color (цвет)
    -fuel (топливо)
    -body (кузов)
    -enginev(обьем двигателя)
    -state (состояние)
    -price (цена)
    -photos (фотографии)
    -comments (комментарии)
    primary key (name,user)

photos (фотографии)

    -advname (название обьявления)
    -user (пользователь)
    -number (порядковый номер)
    -filename (название файла)
    primary key (advname,user,number)

messages (сообщения)

    -advname (название обьявления)
    -recepient (получатель)
    -sender (автор)
    -message (сообщение)
    -datetime (время/дата отправки)
    primary key (advname,recepient,sender,datetime)

