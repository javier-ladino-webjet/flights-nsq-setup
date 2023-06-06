import json
import requests

from pathlib import Path


class App:

    FILEPATH = Path().absolute()
    URL = 'http://localhost:4151'
    file = None

    def __init__(self):
        self.file = open(f'{self.FILEPATH}/src/topics.json')

    def process_topics(self, data):
        try:

            for index, topic in enumerate(data['topics']):

                # Delete topic if exists including all channels
                rtd = requests.post(
                    url=f'{self.URL}/topic/delete?topic={topic["name"]}', timeout=10)

                rt = requests.post(
                    url=f'{self.URL}/topic/create?topic={topic["name"]}', timeout=10)

                if (rt.ok):
                    for channel in data['topics'][index]['channels']:
                        rc = requests.post(
                            url=f'{self.URL}/channel/create?topic={topic["name"]}&channel={channel["name"]}', timeout=10)
        except Exception as err:
            raise Exception(err)
        finally:
            self.file.close()

    def process_file(self):
        try:
            return json.load(self.file)
        except Exception as err:
            raise Exception(err)


if __name__ == '__main__':
    try:
        print('Creating topics/channels...')
        app = App()
        data = app.process_file()
        app.process_topics(data)
        print('Topics/channels created!')
    except Exception as err:
        print(err)
