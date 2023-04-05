import csv


class FileOperation:
    def __init__(self, file_name: str = ""):
        self.__file_name = file_name + ".csv"
        create_file = open(f"{file_name + '.csv'}", "a+")
        create_file.close()

    def overwriting_file(self, data: list[str]):
        with open(self.__file_name, "w", newline="") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerows(data)

    def reading_all_file(self):
        all_records = []
        with open(self.__file_name, "r", newline="") as file:
            all_records_from_file = csv.reader(file, delimiter=";")
            for position in all_records_from_file:
                one_record = [position[0], position[1], position[2], position[3]]
                all_records.append(one_record)
        return all_records