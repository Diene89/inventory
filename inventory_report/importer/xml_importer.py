from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import Inventory


class XmlImporter(Importer):
    def import_data(file):
        if file.endswith(".xml"):
            return Inventory.reader_xml(file)
        else:
            raise ValueError("Arquivo inválido")
