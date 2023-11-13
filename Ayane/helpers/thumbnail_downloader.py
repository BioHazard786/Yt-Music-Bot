from .__init__ import *


def dl_thumbnail_image(link, user_id):
    response = requests.get(link)
    if response.status_code == 200:
        try:
            os.remove(f"thumbnail_{user_id}.jpg")
        except:
            pass

        with open(f"thumbnail_{user_id}.jpg", "wb") as cover:
            cover.write(response.content)
        return f"thumbnail_{user_id}.jpg"
    else:
        return None
