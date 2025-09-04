import requests


my_headers = {'Content-Type': 'application/json',
              'Authorization': '' # noqa
              }

user = {"043e77b3-8a85-4eea-a8a5-e1c5f2b48b52": "admin"}


class YouGile_API():

    def __init__(self, url):
        self.url = url

    def creat_project(self, name):
        body = {'title': name,
                'users': user}
        result = requests.post(
            self.url, json=body, headers=my_headers).status_code
        return result

    def get_new_id(self, name):
        body = {'title': name,
                'users': user}
        new_id = requests.post(
            self.url, json=body, headers=my_headers).json()
        return new_id['id']

    def delete_project(self, id):
        new_id = id
        body_del = {'deleted': True}
        delete = requests.put(
            self.url+new_id, json=body_del, headers=my_headers).status_code
        return delete

    def get_list_project(self):
        search = requests.get(self.url, headers=my_headers).status_code
        return search

    def find_by_id(self, id):
        my_id = id
        find = requests.put(
            self.url+my_id, headers=my_headers).status_code
        return find

    def cleaner(self):
        search = requests.get(self.url, headers=my_headers).json()
        id_c = {}
        id_c = search["content"]
        if (len(id_c) > 0):
            body_del = {'deleted': True}
            requests.put(
                self.url+id_c[0]['id'], json=body_del, headers=my_headers)
            YouGile_API.cleaner(self)
        else:
            return None
