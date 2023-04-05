import xml.etree.ElementTree as ET
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, file_path: str):
        if file_path.endswith(".xml"):
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
        else:
            raise ValueError("Arquivo inválido")
        return data
