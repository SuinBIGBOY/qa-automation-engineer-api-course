from os import access

import httpx

user_payload = {
  "email": "new_user@example.com",
  "password": "mypassword",
}
user_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=user_payload)
user_response_data = user_response.json()
print("Login user data:", user_response_data)

client = httpx.Client(
    base_url="http://localhost:8000",
    headers={"Authorization": f"Bearer {user_response_data['token']['accessToken']}"},
    timeout=100,
)
get_user_response = client.get("/api/v1/users/me")
get_user_response_data = get_user_response.json()
print("Get user data:", get_user_response_data)