from datetime import *

from notes.model.note import Note
from notes.model.template_for_note import TemplateForNote
from notes.model.working_with_file import FileOperation


class RepositoryNote:
    def __init__(self, file: FileOperation, template_for_file: TemplateForNote):
        self.__file = file
        self.__template_for_file = template_for_file

    def read_all_note(self):

        all_note = []

        all_entries_from_file = self.__file.reading_all_file()

        for one_line in all_entries_from_file:

            note = self.__template_for_file.template_for_load_file(one_line)

            all_note.append(note)
        return all_note

    def overwrite_all_note(self, all_notes: list[Note]):

        all_line_in_file = []

        for one_note in all_notes:

            one_line_in_file = self.__template_for_file.template_for_safe_file(one_note)

            all_line_in_file.append(one_line_in_file)

        self.__file.overwriting_file(all_line_in_file)

    def add_one_new_note(self, new_note: Note):

        all_notes = self.read_all_note()

        maximum_value = 0

        for one_note in all_notes:
            id_one_note = int(one_note.get_id())
            if maximum_value < id_one_note:
                maximum_value = id_one_note

        id_for_new_note = maximum_value + 1

        new_note.set_id(str(id_for_new_note))
        new_note.set_date_creation(datetime.now())

        all_notes.append(new_note)
        self.overwrite_all_note(all_notes)
