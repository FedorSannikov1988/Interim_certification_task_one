import datetime


class Note:
    def __init__(self, id: str = "", title: str = "", body: str = "", date_creation: datetime = ""):
        self.__id = id
        self.__title = title
        self.__body = body
        self.__date_creation = date_creation

    def get_id(self) -> str:
        return self.__id

    def set_id(self, id: str):
        self.__id = id

    def get_title(self) -> str:
        return self.__title

    def set_title(self, title: str):
        self.__title = title

    def get_body(self) -> str:
        return self.__body

    def set_body(self, body: str):
        self.__body = body

    def get_date_creation(self):
            return self.__date_creation

    def set_date_creation(self, date_creation: datetime):
            self.__date_creation = date_creation

    def __str__(self):
        return f"<| Номер заметки: {self.__id} Заголовок: {self.__title} Содержание: {self.__body} Создана/Изменена: {self.__date_creation} |>"