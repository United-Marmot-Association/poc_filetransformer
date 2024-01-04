import requests


class RepoReader:
    def __init__(self, url, username, repository, path, branch):
        self.__url = url
        self.__username = username
        self.__repository = repository
        self.__path = path
        self.__branch = branch

    def get_file_contents(self):
        url = f'https://raw.githubusercontent.com/{self.__username}/{self.__repository}/{self.__branch}/{self.__path}'

        try:
            response = requests.get(url)
            response.raise_for_status()  # Check for HTTP errors
            content = response.text
            return content
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None
