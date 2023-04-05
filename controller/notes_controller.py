from datetime import *

from notes.model.note import Note
from notes.model.repository_note import RepositoryNote


class NotesController:
    def __init__(self, notepad: RepositoryNote):
        self.__notepad = notepad

    def controller_read_all_note(self):
        return self.__notepad.read_all_note()

    def controller_add_one_new_note(self, new_note: Note):
        self.__notepad.add_one_new_note(new_note)

    def controller_overwrite_all_note(self, all_notes: list[Note]):
        self.__notepad.overwrite_all_note(all_notes)

    def controller_read_one_note_by_id(self, id_search_note: str):
        all_note = self.__notepad.read_all_note()
        return self.controller_search_note_by_id(id_note=id_search_note, all_notes=all_note)

    def controller_adjust_one_note_by_id(self, id_note: str, adjust_note: Note):

        all_notes = self.__notepad.read_all_note()

        found_note = self.controller_search_note_by_id(id_note=id_note, all_notes=all_notes)

        try:
            found_note.set_id(id_note)
            found_note.set_title(adjust_note.get_title())
            found_note.set_body(adjust_note.get_body())
            found_note.set_date_creation(datetime.now())
        except:
            print("Запись не изменена")

        finally:
            self.__notepad.overwrite_all_note(all_notes)

    def controller_delete_one_note_by_id(self, id_note_by_delete: str):

        all_notes_from_file = self.__notepad.read_all_note()

        try:
            found_note = self.controller_search_note_by_id(id_note=id_note_by_delete, all_notes=all_notes_from_file)
            all_notes_from_file.remove(found_note)

        except:
            print("Запись не удалена")

        finally:
            self.__notepad.overwrite_all_note(all_notes_from_file)

    def controller_sort_data(self):

        all_notes_from_file = self.__notepad.read_all_note()

        self.controller_bubble_sort_method(all_notes_from_file=all_notes_from_file,
                                           selecting_parameter_which_sorting="data")

        self.__notepad.overwrite_all_note(all_notes_from_file)

    def controller_sort_id(self):

        all_notes_from_file = self.__notepad.read_all_note()

        self.controller_bubble_sort_method(all_notes_from_file=all_notes_from_file,
                                           selecting_parameter_which_sorting="id")

        self.__notepad.overwrite_all_note(all_notes_from_file)

    def controller_bubble_sort_method(self, all_notes_from_file: list[Note],
                                      selecting_parameter_which_sorting: str):

        length = len(all_notes_from_file)

        for i in range(length):
            for j in range(0, length - i - 1):

                match selecting_parameter_which_sorting:

                    case "id":
                        if all_notes_from_file[j].get_id() > all_notes_from_file[j + 1].get_id():
                            self.controller_data_communication(index=j, array=all_notes_from_file)

                    case "data":
                        if all_notes_from_file[j].get_date_creation() > all_notes_from_file[j + 1].get_date_creation():
                            self.controller_data_communication(index=j, array=all_notes_from_file)

    @staticmethod
    def controller_data_communication(index: int, array: list[Note]):
        temp = array[index]
        array[index] = array[index + 1]
        array[index + 1] = temp

    @staticmethod
    def controller_search_note_by_id(id_note: str, all_notes: list[Note]):
        for one_note in all_notes:
            if id_note == one_note.get_id():
                return one_note

        print("Запись не нейдена")
