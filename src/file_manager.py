"""
file manager
异步管理&收发文件
client 通过一些方式获得 imgs，将其发送到 server， server返回 img 的 results
所以 需要一个表
[image_id, image_data, predict_result, time, location]

[保持运行时]
"""
from pathlib import Path
from typing import Optional
import json
from os import path


class FileManager:
    {
        "iamges": [
            {
                "image_id": 123,
                "predict_result": [[1, 1, 20, 30], [100, 100, 130, 130]],
                'image_data':b'',

            }
        ]
    }

    def __init__(self, root_path: str):
        self.root_path = Path(root_path)
        self.image_path = self.root_path/'images'
        self.images_meta_json = (self.root_path/'images_meta.json')
        with open(self.images_meta_json, 'w') as json_file:
            json.dump({}, json_file)  # 使用json.dump将字典写入文件

    def load_images(self, image_path: [Path | None | str]):
        if image_path is None:
            image_path = self.image_path
        else:
            image_path = Path(image_path)if type(
                image_path) == str else image_path

        supported_suffix = ['.jpeg', '.png', '.jpg']
        image_files = [str(i)for i in image_path.iterdir()
                       if i.suffix in supported_suffix]
        return image_files


if __name__ == '__main__':
    file_manager = FileManager('../resources')
