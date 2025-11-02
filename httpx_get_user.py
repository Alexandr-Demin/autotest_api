import httpx
from tools.fakers import get_random_email

requet_body = {
  "email": get_random_email(),
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

creat_request = httpx.post("http://localhost:8000/api/v1/users", json=requet_body)
creat_response_data = creat_request.json()
print("Statuis code:", creat_request.status_code)
print("Response body_newUser:", creat_response_data)


login_payload = {
    "email": requet_body['email'],
    "password": requet_body['password']
}

authentication_user = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
authentication_user_data = authentication_user.json()

print("Statuis code:", authentication_user.status_code)
print("Response body_auth:", authentication_user_data)

header_user = {
    "Authorization":f"Bearer {authentication_user_data['token']['accessToken']}"
}


search_user = httpx.get(f"http://localhost:8000/api/v1/users/{creat_response_data['user']['id']}", headers=header_user)
search_user_data = search_user.json()
print("Cred:", creat_response_data['user']['id'])
print("Statuis code:", search_user.status_code)
print("Response body:", search_user_data)