import urllib.request
import json

url = "http://127.0.0.1:8000/api/cars/"
data = {
    "brand": "Audi",
    "model": "Test Model",
    "year": 2024,
    "price": 50000,
    "km": 100,
    "fuel": "Petrol",
    "transmission": "Automatic",
    "description": "Test description",
    "status": "available",
    "images": ["https://images.unsplash.com/photo-1617788138017-80ad40651399"]
}

req = urllib.request.Request(url)
req.add_header('Content-Type', 'application/json; charset=utf-8')
jsondata = json.dumps(data)
jsondataasbytes = jsondata.encode('utf-8')
req.add_header('Content-Length', len(jsondataasbytes))

try:
    response = urllib.request.urlopen(req, jsondataasbytes)
    print(f"Status Code: {response.getcode()}")
    print(response.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print(f"HTTPError: {e.code}")
    print(e.read().decode('utf-8'))
except Exception as e:
    print(f"Error: {e}")
