from notes.model.note import Note


def template_for_safe_file(note: Note):

    one_line_in_file = [note.get_id(), note.get_title(), note.get_body(), note.get_date_creation()]

    return one_line_in_file


class TemplateForNote:
    def __init__(self):
        pass

    def template_for_load_file(self, one_line: list):

        note = Note(id=one_line[0], title=one_line[1], body=one_line[2], date_creation=one_line[3])

        return note
