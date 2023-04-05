import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, file_path: str):
        if file_path.endswith(".csv"):
            with open(file_path, "r") as file:
                reader = csv.DictReader(file)
                data = [row for row in reader]
        else:
            raise ValueError("Arquivo inválido")
        return data
