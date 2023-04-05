from notes.model.repository_note import RepositoryNote
from notes.model.template_for_note import TemplateForNote
from notes.model.working_with_file import FileOperation
from notes.controller.notes_controller import NotesController
from notes.view.validation_input_data import ValidationInputData
from notes.view.view_notepad import ViewNotepad


data = FileOperation("data")
template = TemplateForNote()
validation = ValidationInputData()
repository = RepositoryNote(data, template)
controller = NotesController(repository)
view = ViewNotepad(controller, validation)
view.menu()