from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import Inventory


class JsonImporter(Importer):
    def import_data(file):
        if file.endswith(".json"):
            return Inventory.reader_json(file)
        else:
            raise ValueError("Arquivo inválido")
