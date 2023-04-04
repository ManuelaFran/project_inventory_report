import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def __init__(self) -> None:
        pass

    @classmethod
    def import_data(cls, file_path: str, type_report: str):
        with open(file_path, "r") as file:
            reader = csv.DictReader(file)
            data = []
            for row in reader:
                data.append(row)
            if type_report == "simples":
                return SimpleReport.generate(data)
            else:
                return CompleteReport.generate(data)
