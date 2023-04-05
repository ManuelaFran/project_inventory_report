import csv
import json
import xml.etree.ElementTree as ET
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def __init__(self) -> None:
        pass

    @classmethod
    def import_data(cls, file_path: str, report_type: str):
        if file_path.endswith(".csv"):
            with open(file_path, "r") as file:
                reader = csv.DictReader(file)
                data = [row for row in reader]
                return (
                    SimpleReport.generate(data)
                    if report_type == "simples"
                    else CompleteReport.generate(data)
                )

        elif file_path.endswith(".json"):
            with open(file_path) as file:
                data = json.load(file)
                return (
                    SimpleReport.generate(data)
                    if report_type == "simples"
                    else CompleteReport.generate(data)
                )

        elif file_path.endswith(".xml"):
            with open(file_path) as file:
                tree = ET.parse(file)
                root = tree.getroot()
                data = []

                product = {}
                for element in root.iter():
                    if "\n" not in element.text:
                        product[element.tag] = element.text
                    if element.tag == "instrucoes_de_armazenamento":
                        data.append(product)
                        product = {}
                return (
                    SimpleReport.generate(data)
                    if report_type == "simples"
                    else CompleteReport.generate(data)
                )

        else:
            raise ValueError("Invalid file format")
