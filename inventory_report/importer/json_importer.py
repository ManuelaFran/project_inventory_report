import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, file_path: str):
        if file_path.endswith(".json"):
            with open(file_path) as file:
                data = json.load(file)
        else:
            raise ValueError("Arquivo inválido")
        return data
