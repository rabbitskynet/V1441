# ponyauto

users (������������)

    -login (�����)
    -pass (������)
    -email (email)
    -FIO (���)
    -telephone (�������)
    -adv (����������)
    -county (������)
    -city (�����)
    -moderator (�������� �� �����������)
    primary key (login)
	
advs (����������)

    -name (��������)
    -user (������������)
    -autoname (����������)
    -automark (����������)
    -descrition (��������)
    -year (��� �������)
    -gearbox (���)
    -owners (���������)
    -price (����)
    -color (����)
    -fuel (�������)
    -body (�����)
    -enginev(����� ���������)
    -state (���������)
    -price (����)
    -photos (����������)
    -comments (�����������)
    primary key (name,user)

photos (����������)

    -advname (�������� ����������)
    -user (������������)
    -number (���������� �����)
    -filename (�������� �����)
    primary key (advname,user,number)

messages (���������)

    -advname (�������� ����������)
    -recepient (����������)
    -sender (�����)
    -message (���������)
    -datetime (�����/���� ��������)
    primary key (advname,recepient,sender,datetime)

