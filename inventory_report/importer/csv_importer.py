from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import Inventory


class CsvImporter(Importer):
    def import_data(file):
        if file.endswith(".csv"):
            return Inventory.reader_csv(file)
        else:
            raise ValueError("Arquivo inválido")
