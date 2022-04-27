import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["example_database"]

customers = db["customers"]
items = db["items"]

customers_data = [{"firstname": "Bob", "lastname": "Adams"},
                  {"firstname": "Amy", "lastname": "Smith"},
                  {"firstname": "Rob", "lastname": "Bennet"},]

items_data = [{"title": "USB", "price": 10.2},
              {"title": "Mouse", "price": 12.23},
              {"title": "Monitor", "price": 199.99},]

customers.insert_many(customers_data)
items.insert_many(items_data)