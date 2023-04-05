from notes.controller.notes_controller import NotesController
from notes.view.list_commands import ListCommands
from notes.model.note import Note
from notes.view.validation_input_data import ValidationInputData


class ViewNotepad:
    def __init__(self, notes_controller: NotesController, validation_input_data: ValidationInputData):
        self.__notes_controller = notes_controller
        self.__validation_input_data = validation_input_data


    def menu(self):

        print("При вводе комманд регист не имеет значение")

        while True:

            command_from_user = input("Введите комманду: ").upper()

            match command_from_user:
                case "HELP":
                    self.view_help()
                case "LIST":
                    self.view_read_all_note()
                case "EXIT":
                    return
                case "DELETE":
                    self.view_delete_one_note_by_id()
                case "CREATE":
                    self.view_add_one_new_note()
                case "READ":
                    self.view_read_one_note_by_id()
                case "UPDATE":
                    self.view_adjust_one_note_by_id()
                case "SORT_DATA":
                    self.view_sort_data()
                case "SORT_ID":
                    self.view_sort_id()

    def view_read_all_note(self):

        all_notes = self.__notes_controller.controller_read_all_note()

        if all_notes == []:
            print("В записной книжке нет записей ")

        for one_note in all_notes:
            print(one_note)

    def view_delete_one_note_by_id(self):

        id_note = input("Введите номер записи которую необходимо удалить: ")

        self.__validation_input_data.check_id(id_note)

        self.__notes_controller.controller_delete_one_note_by_id(id_note)

    def view_add_one_new_note(self):

        self.__notes_controller.controller_add_one_new_note(self.create_new_note())

    def view_read_one_note_by_id(self):

        id_note = input("Введите уникальный номер записи которую необходимо прочесть: ")

        self.__validation_input_data.check_id(id_note)

        faund_note = self.__notes_controller.controller_read_one_note_by_id(id_search_note=id_note)

        if faund_note is not None:
            print(faund_note)

    def view_adjust_one_note_by_id(self):

        id_search_note = input("Введите уникальный номер записи которую необходимо изменить: ")

        self.__validation_input_data.check_id(id_search_note)

        self.__notes_controller.controller_adjust_one_note_by_id(id_note=id_search_note,\
                                                                 adjust_note=self.create_new_note())

    def view_sort_data(self):

        print("Сортировка по дате проведена")

        self.__notes_controller.controller_sort_data()

    def view_sort_id(self):

        print("Сортировка по уникальному номеру проведена")

        self.__notes_controller.controller_sort_id()

    @staticmethod
    def create_new_note():

        title_new_note = input("Заголовок: ")
        body_new_note = input("Содержание: ")

        new_note = Note(title=title_new_note, body=body_new_note)

        return new_note

    @staticmethod
    def view_help():

        for one_command in ListCommands:
            print(one_command.command, " - ", one_command.description)