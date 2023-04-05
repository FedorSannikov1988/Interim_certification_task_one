
class ValidationInputData:
    def __init__(self):
        pass

    def check_id(self, id_str: str = ""):

        try:
            id_int = int(id_str)

            if id_int <= 0:
                print("Нумерация записей начинается с 1-ого")

        except:
            print("Введено не число в 10-ой системе исчисления")

