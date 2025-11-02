import httpx

respons = httpx.get('https://postman-echo.com/get?foo1=bar1')
print (respons.status_code)
print(respons.json())

data = {
    "foo1": "bar111",
    "foo2": "bar2222"
}
respons = httpx.post('https://postman-echo.com/post', json=data)
print (respons.status_code)
print (respons.request.headers)
print(respons.json())


data = {"username": "USer"}

respons = httpx.post('https://httpbin.org/post', data=data)
print (respons.status_code)
print(respons.json())


header = {"Autorization": "Bearer My_secret_token"}
respons = httpx.get('https://httpbin.org/get', headers=header)
print(respons.request.headers)
print(respons.json())

params = {"foo1": "bar1"}


respons = httpx.get('https://postman-echo.com/get', params=params)
print(respons.url)
print(respons.json())


files = {"file": ("example.txt", open("example.txt", "rb"))}
respons = httpx.post('https://postman-echo.com/post', files=files)
print(respons.json())

with httpx.Client() as client:
    response1 = client.get('https://postman-echo.com/get?foo1=bar1')
    response2 = client.get('https://postman-echo.com/get?foo2=bar2')

print(response1.json())
print(response2.json())


client = httpx.Client(headers={"Autorization": "Bearer My_secret_token"})
response = client.get('https://postman-echo.com/get')

print(response.json())


try:
    response = httpx.get('https://postman-echo.com/invalid_url')
    response.raise_for_status()
except httpx.HTTPStatusError as e:
    print(f"Error request: {e}")



try:
    response = httpx.get('https://postman-echo.com/delay/5', timeout=2)
except httpx.ReadTimeout:

    print("Запросил превысил лимит времени")


