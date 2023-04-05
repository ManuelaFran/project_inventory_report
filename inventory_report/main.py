import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def main():
    try:
        _, path, report_type = sys.argv
        if path.endswith(".csv"):
            result = (InventoryRefactor(CsvImporter).import_data(
                path, report_type
            ))

        elif path.endswith(".json"):
            result = InventoryRefactor(JsonImporter).import_data(
                path, report_type
            )

        else:
            result = InventoryRefactor(XmlImporter).import_data(
                path, report_type
            )

    except ValueError:
        sys.stderr.write("Verifique os argumentos\n")

    else:
        sys.stdout.write(result)
