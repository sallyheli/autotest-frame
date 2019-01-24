import requests
from PIL import Image
from io import BytesIO

def get_image(url=None):
    url = "https://pic.qiushibaike.com/system/avtnew/3069/30690114/thumb/20190110003901.jpg?imageView2/1/w/90/h/90"
    res = requests.get(url)
    i = Image.open(BytesIO(res.content))
    i.save("thumb.jpg")

if __name__ == "__main__":
    get_image()