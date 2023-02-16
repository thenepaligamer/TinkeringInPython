"""
pip install requests
"""

import requests

BASE_URL = 'https://fakestoreapi.com'

"""
limit the no of data to be shown by response
"""
query_params = {
    "limit": 3
}

"""
GET request
via requests.get()
"""
response = requests.get(f"{BASE_URL}/products", params=query_params)
print(response.json())

"""
for specific product, we can use /products/<product_id>
"""
response = requests.get(f"{BASE_URL}/products/18")
print(response.json())


"""
POST request
via response.post()
"""

new_product = {
    "title": 'test 123',
    "price": '12.2',
    "description": 'testing 123',
    "category": 'spandex',
    "image": 'https://gravatra.com'
}

response = requests.post(f"{BASE_URL}/products", json = new_product)
print(response.json())

"""
PUT Request
via requests.put()
will completely replace old data with new one
"""

updated_product = {
    "title": 'LTT Underwear',
    "description": '95% Spandex, 5% cotton. Great for your bottom'
}

response = requests.put(f"{BASE_URL}/products/21", json = updated_product)
print(response.json())

"""
PATCH Request
for modifying only certain fields in the old data
via requests.patch()
"""

updated_product = {
    "title": 'UNDERWEAR 3-PACK'
}

response = requests.patch(f"{BASE_URL}/products/21", json = updated_product)
print(response.json())

"""
DELETE Request
via requests.delete()
"""

response = requests.delete(f"{BASE_URL}/products/21")
print(response.json())