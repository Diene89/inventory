from collections import Counter

from inventory_report.reports.simple_report import SimpleReport


# class CompleteReport(SimpleReport):
#     @classmethod
#     def get_products_quantity_by_company(self, stock):

#         companies = Counter(
#             product["nome_da_empresa"] for product in stock
#         ).most_common()
#         complete_stock = ""

#         for company, quantity in companies:
#             complete_stock += f"- {company}: {quantity}\n"

#         return complete_stock

#     @classmethod
#     def generate(self, stock):
#         report = SimpleReport.generate(stock)
#         products_list = self.get_products_quantity_by_company(self, stock)

#         return (
#             f"{report}\n"
#             f"Produtos estocados por empresa:\n"
#             f"{products_list}"
#         )

class CompleteReport():
    def get_products_quantity_by_company(self, stock):
        count_companies = list()
        complete_stock = ""

        for product in stock:
            count_companies.append(product["nome_da_empresa"])

        most_common_company = Counter(count_companies).most_common()

        for product, quantity in most_common_company:
            complete_stock += f"- {product}: {quantity}\n"

        return complete_stock

    @classmethod
    def generate(self, stock):
        report = SimpleReport.generate(stock)
        products_list = self.get_products_quantity_by_company(self, stock)

        return (
            f"{report}\n"
            f"Produtos estocados por empresa:\n"
            f"{products_list}"
        )
