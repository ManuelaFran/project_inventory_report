from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    def __init__(self):
        pass

    @classmethod
    def import_data(cls, file_path: str, report_type: str):
        if file_path.endswith(".csv"):
            data = CsvImporter.import_data(file_path)
            return (
                SimpleReport.generate(data)
                if report_type == "simples"
                else CompleteReport.generate(data)
            )

        elif file_path.endswith(".json"):
            data = JsonImporter.import_data(file_path)
            return (
                SimpleReport.generate(data)
                if report_type == "simples"
                else CompleteReport.generate(data)
            )

        else:
            data = XmlImporter.import_data(file_path)
            return (
                SimpleReport.generate(data)
                if report_type == "simples"
                else CompleteReport.generate(data)
            )
