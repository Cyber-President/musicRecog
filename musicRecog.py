import requests
data = {
    'url': 'https://drive.google.com/uc?id=1PlZl03BitMV8GrD8GcO3V_QjW888Sb2g',
    'return': 'apple_music,spotify',
    'api_token': 'test'
}
result = requests.post('https://api.audd.io/', data=data)
print(result.text)
print(result.headers['Content-Type'])

json_datta =result.json()

# print(json_datta[])