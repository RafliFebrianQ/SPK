from http import HTTPStatus
from flask import Flask, request, abort
from flask_restful import Resource, Api 
from models import Salmon as SalmonModel
from engine import engine
from sqlalchemy import select
from sqlalchemy.orm import Session

session = Session(engine)

app = Flask(__name__)
api = Api(app)        

class BaseMethod():

    def __init__(self):
        self.raw_weight = {'harga': 4, 'umur': 3, 'berat': 4, 'lemak': 6, 'omega_3': 3}

    @property
    def weight(self):
        total_weight = sum(self.raw_weight.values())
        return {k: round(v/total_weight, 2) for k, v in self.raw_weight.items()}

    @property
    def data(self):
        query = select(SalmonModel.id_salmon, SalmonModel.harga, SalmonModel.umur, SalmonModel.berat, SalmonModel.lemak, SalmonModel.omega_3)
        result = session.execute(query).fetchall()
        print(result)
        return [{'id_salmon': salmon.id_salmon, 'harga': salmon.harga, 'umur': salmon.umur, 'berat': salmon.berat, 'lemak': salmon.lemak, 'omega_3': salmon.omega_3} for salmon in result]

    @property
    def normalized_data(self):
        harga_values = []
        umur_values = []
        berat_values = []
        lemak_values = []
        omega_3_values = []

        for data in self.data:
            harga_values.append(data['harga'])
            umur_values.append(data['umur'])
            berat_values.append(data['berat'])
            lemak_values.append(data['lemak'])
            omega_3_values.append(data['omega_3'])

        return [
            {'id_salmon': data['id_salmon'],
             'harga': min(harga_values) / data['harga'],
             'umur': data['umur'] / max(umur_values),
             'berat': data['berat'] / max(berat_values),
             'lemak': data['lemak'] / max(lemak_values),
             'omega_3': data['omega_3'] / max(omega_3_values)
             }
            for data in self.data
        ]

    def update_weights(self, new_weights):
        self.raw_weight = new_weights

class WeightedProductCalculator(BaseMethod):
    def update_weights(self, new_weights):
        self.raw_weight = new_weights

    @property
    def calculate(self):
        normalized_data = self.normalized_data
        produk = []

        for row in normalized_data:
            product_score = (
                row['harga'] ** self.raw_weight['harga'] *
                row['umur'] ** self.raw_weight['umur'] *
                row['berat'] ** self.raw_weight['berat'] *
                row['lemak'] ** self.raw_weight['lemak'] *
                row['omega_3'] ** self.raw_weight['omega_3']
            )

            produk.append({
                'id_salmon': row['id_salmon'],
                'produk': product_score
            })

        sorted_produk = sorted(produk, key=lambda x: x['produk'], reverse=True)

        sorted_data = []

        for product in sorted_produk:
            sorted_data.append({
                'id_salmon': product['id_salmon'],
                'score': product['produk']
            })

        return sorted_data


class WeightedProduct(Resource):
    def get(self):
        calculator = WeightedProductCalculator()
        result = calculator.calculate
        return result, HTTPStatus.OK.value
    
    def post(self):
        new_weights = request.get_json()
        calculator = WeightedProductCalculator()
        calculator.update_weights(new_weights)
        result = calculator.calculate
        return {'data': result}, HTTPStatus.OK.value
    

class SimpleAdditiveWeightingCalculator(BaseMethod):
    @property
    def calculate(self):
        weight = self.weight
        result = {row['id_salmon']:
                  round(row['harga'] * weight['harga'] +
                        row['umur'] * weight['umur'] +
                        row['berat'] * weight['berat'] +
                        row['lemak'] * weight['lemak'] +
                        row['omega_3'] * weight['omega_3'], 2)
                  for row in self.normalized_data
                  }
        sorted_result = dict(
            sorted(result.items(), key=lambda x: x[1], reverse=True))
        return sorted_result

    def update_weights(self, new_weights):
        self.raw_weight = new_weights

class SimpleAdditiveWeighting(Resource):
    def get(self):
        saw = SimpleAdditiveWeightingCalculator()
        result = saw.calculate
        return result, HTTPStatus.OK.value

    def post(self):
        new_weights = request.get_json()
        saw = SimpleAdditiveWeightingCalculator()
        saw.update_weights(new_weights)
        result = saw.calculate
        return {'data': result}, HTTPStatus.OK.value


class salmon(Resource):
    def get_paginated_result(self, url, list, args):
        page_size = int(args.get('page_size', 10))
        page = int(args.get('page', 1))
        page_count = int((len(list) + page_size - 1) / page_size)
        start = (page - 1) * page_size
        end = min(start + page_size, len(list))

        if page < page_count:
            next_page = f'{url}?page={page+1}&page_size={page_size}'
        else:
            next_page = None
        if page > 1:
            prev_page = f'{url}?page={page-1}&page_size={page_size}'
        else:
            prev_page = None
        
        if page > page_count or page < 1:
            abort(404, description=f'Halaman {page} tidak ditemukan.') 
        return {
            'page': page, 
            'page_size': page_size,
            'next': next_page, 
            'prev': prev_page,
            'Results': list[start:end]
        }

    def get(self):
        query = select(SalmonModel)
        data = [{'id_salmon': salmon.id_salmon, 'harga': salmon.harga, 'umur': salmon.umur, 'berat': salmon.berat, 'lemak': salmon.lemak, 'omega_3': salmon.omega_3} for salmon in session.scalars(query)]
        return self.get_paginated_result('salmon/', data, request.args), HTTPStatus.OK.value


api.add_resource(salmon, '/salmon')
api.add_resource(WeightedProduct, '/wp')
api.add_resource(SimpleAdditiveWeighting, '/saw')

if __name__ == '__main__':
    app.run(port='5005', debug=True)
