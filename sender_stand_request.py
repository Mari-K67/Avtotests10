import requests
import configuration
import data


def post_new_oder(user_body):
    return requests.post(configuration.url_cervice + configuration.create_oder_path,
                         json=user_body)


response = post_new_oder(data.user_body)
print(response.status_code)
auth_Token = response.json()["authToken"]
