import requests

class YandexDisk:

    def __init__(self, token):
        self.token = token


    def get_headers(self):
        return {
            "Content-Type": "application/json",
            "Authorization": f'OAuth {self.token}'
        }


    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()


    def upload_file_to_disk(self, disk_file_path, filename):
        href_response = self._get_upload_link(disk_file_path=disk_file_path)
        href = href_response.get("href", "")
        response = requests.put(url=href, data=open(filename, "rb"))
        if response.status_code == 201:
            print("Success")
