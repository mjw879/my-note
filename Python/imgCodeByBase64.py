import base64
with open("VSCode/img/base64.png","rb") as file:
    data = base64.b64encode(file.read()) #读取文件内容，转换为base64编码
    print(data)