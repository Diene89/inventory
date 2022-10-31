from datetime import datetime
from collections import Counter


class SimpleReport:
    @classmethod
    def get_oldest_manufacturing_date(self, stock):
        oldest_date = min(
            [product["data_de_fabricacao"] for product in stock]
        )
        return oldest_date

    @classmethod
    def get_closest_expiration_date(self, stock):
        closest_expiration_date = min(
            [
                product["data_de_validade"]
                for product in stock
                if product["data_de_validade"] > str(datetime.today().date())
            ]
        )
        return closest_expiration_date

    @classmethod
    def get_company_with_most_products(self, stock):
        companies = Counter(product["nome_da_empresa"] for product in stock)
        return companies.most_common(1)[0][0]
       
    @classmethod
    def generate(self, stock):

        oldest_manufacturing_date = self.get_oldest_manufacturing_date(stock)
        closest_expiration_date = self.get_closest_expiration_date(stock)
        company = self.get_company_with_most_products(stock)

        return (
            f'Data de fabricação mais antiga: {oldest_manufacturing_date}\n'
            f'Data de validade mais próxima: {closest_expiration_date}\n'
            f'Empresa com mais produtos: {company}'
        )
