# Author Jaredhao
# Email 9190632@qq.com
# Created 2024/4/23 9:41
import json
import uuid
from io import BytesIO
from pathlib import Path

from PIL import Image
from docx import Document
from openai import OpenAI


# 上传文件并获取到对应内容
# 将内容转化为txt文本使用fileid作为文件名存储到用户uuid对应的文件夹下
# 根据上传的文件id删除kimi存储的文件
# 对文件内容进行总结生成一个json表，用来映射内容梗概和文件id
MOONSHOT_SERVER = "https://api.moonshot.cn/v1"
class KimiFiles:
    def __init__(self,MOONSHOT_API_KEY):
        self.client = OpenAI(
            api_key=MOONSHOT_API_KEY,
            base_url=MOONSHOT_SERVER,
        )

    def uploadFileV2(self, file_path):
        _file_path = Path(file_path)
        files = [file_path]
        if _file_path.suffix == '.docx':
            doc = Document(file_path)
            for rel in doc.part.rels.values():
                if "image" in rel.target_ref:
                    img = rel.target_part
                    img_blob = img.blob
                    img_format = Image.open(BytesIO(img_blob)).format.lower()
                    img_ext = '.' + img_format if img_format else ''
                    img_name = str(uuid.uuid4()) + img_ext
                    img_path = _file_path.parent / img_name
                    with open(img_path, "wb") as f:
                        f.write(img_blob)
                    files.append(img_path)
        content = ""
        for file in files:
            file_id, file_content, file_name = self.uploadFile(file)
            content += file_content + "\n"
        return "file_id", content, "file_name"

    def uploadFile(self, file_path):
        try:
            file_object = self.client.files.create(file=Path(file_path), purpose="file-extract")
            file_id = file_object.id
            file_content = self.client.files.content(file_id=file_object.id).text
            print(file_object.filename)
            print("file_id:", file_id)
            print("file_content:", file_content)
            self.delFile(file_id)
            file_data = json.loads(file_content)
            return file_id, file_data['content'], file_object.filename
        except Exception as e:
            print("文档解析错误:", e, file_path)
            return "", "", ""

    def delFile(self, file_id):
        res = self.client.files.delete(file_id=file_id)
        print(res)

    def getFiles(self):
        file_list = self.client.files.list()
        for file in file_list.data:
            print(file)

