import csv
import json
import xmltodict

from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    def reader_csv(path):
        stock = []
        with open(path) as file:
            stock_csv = csv.DictReader(file)
            for product in stock_csv:
                stock.append(product)
        return stock

    def reader_json(path):
        stock = []
        with open(path) as file:
            stock_json = json.load(file)
            for product in stock_json:
                stock.append(product)
        return stock

    def reader_xml(path):
        inventory_list = []
        with open(path) as file:
            read_file = xmltodict.parse(file.read())
            inventory_list = read_file["dataset"]["record"]
        return inventory_list

    @classmethod
    def reader_file(self, path):
        if path.endswith(".csv"):
            return self.reader_csv(path)
        elif path.endswith(".json"):
            return self.reader_json(path)
        elif path.endswith(".xml"):
            return self.reader_xml(path)

    @classmethod
    def import_data(self, path, type):
        stock = self.reader_file(path)

        if (type == 'simples'):
            return SimpleReport.generate(stock)
        elif (type == 'completo'):
            return CompleteReport.generate(stock)
