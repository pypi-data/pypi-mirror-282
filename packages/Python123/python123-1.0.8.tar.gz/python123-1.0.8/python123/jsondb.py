# json文件处理
import json


class JSONDatabase:
    """JSON文件操作类"""

    def __init__(self, file_path):
        self.file_path = file_path  # JSON文件路径

    def read(self):
        with open(self.file_path, 'r', encoding="utf-8") as f:
            return json.loads(f.read())

    def write(self, document):
        with open(self.file_path, 'w', encoding="utf-8") as f:
            f.write(json.dumps(document, ensure_ascii=False, indent=4))


if __name__ == '__main__':
    json_db = JSONDatabase('data.json')
    d = {"1": 2, "2": 3, "3": 4, "4": 5, "5": 6}
    json_db.write(d)
    print(json_db.read())
