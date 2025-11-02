import httpx
from tools.fakers import get_random_email

user_payload = {
  "email": get_random_email(),
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

create_user = httpx.post("http://localhost:8000/api/v1/users", json=user_payload)
create_user_data = create_user.json()

print("Response Status Code:", create_user.status_code)
print("Response body, create user:", create_user_data)

login_payload = {
    "email": user_payload["email"],
    "password": user_payload["password"]
}

login_user = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_user_data = login_user.json()

print("Response Status Code:", login_user.status_code)
print("Response body, login user:", login_user_data)


heder_user = {
    "Authorization":f'Bearer {login_user_data['token']['accessToken']}'
}

delete_user = httpx.delete(
    f"http://localhost:8000/api/v1/users/{create_user_data['user']['id']}",
    headers=heder_user
)

print("Status code, delete user:", delete_user.status_code)
