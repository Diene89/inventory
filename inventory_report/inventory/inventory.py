import csv
import json
import xmltodict

from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def reader_csv(self, path):
        stock = []
        with open(path) as file:
            stock_csv = csv.DictReader(file)
            for product in stock_csv:
                stock.append(product)
        return stock

    @classmethod
    def reader_json(self, path):
        stock = []
        with open(path) as file:
            stock_json = json.load(file)
            for product in stock_json:
                stock.append(product)
        return stock

    @classmethod
    def reader_xml(self, path):
        inventory_list = []
        with open(path) as file:
            read_file = xmltodict.parse(file.read())
            inventory_list = read_file["dataset"]["record"]
        return inventory_list

    @classmethod
    def import_data(self, path, type):
        if path.endswith(".csv"):
            product_list = self.reader_csv(path)
        elif path.endswith(".json"):
            product_list = self.reader_json(path)
        elif path.endswith(".xml"):
            product_list = self.reader_xml(path)
        return self.verify_type(product_list, type)

    @classmethod
    def verify_type(self, product_list, type):

        if (type == 'simples'):
            return SimpleReport.generate(product_list)
        elif (type == 'completo'):
            return CompleteReport.generate(product_list)
