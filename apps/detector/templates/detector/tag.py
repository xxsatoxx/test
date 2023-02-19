import requests
from requests.structures import CaseInsensitiveDict
import json
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

QUERY_TAG = "dog" # the tag you want to search for

headers = CaseInsensitiveDict()
headers["Authorization"] = ""

URL = "https://api.unsplash.com/search/photos?query=
{}&per_page=10".format(QUERY_TAG)

response = requests.get(URL, headers=headers)
data = json.loads(response.text)

images = data["results"]

for image in images:
    image_url = image["urls"]["raw"]
    image = Image.open(BytesIO(requests.get(image_url).content))
    plt.imshow(image)
plt.show()
