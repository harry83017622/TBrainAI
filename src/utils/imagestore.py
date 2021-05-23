
import base64
import datetime
import time

from PIL import Image 
import PIL

import imghdr
from pathlib import Path
import os
import threading
import random
import string
import sys

def base64_to_image_file(outputBaseDir, image_64_encoded):
    """ Convert base64 to numpy.ndarray for cv2.
    @param:
        outputBaseDir(str): output
        image_64_encode(str): image that encoded in base64 string format.
    """
    img_base64_binary = image_64_encoded.encode("utf-8")
    img_binary = base64.b64decode(img_base64_binary)

    # create directory of today if necessary
    now = datetime.datetime.now()
    dateTimeLog = now.strftime("%Y-%m-%d %H:%M:%S")
    dateTimeStr = now.strftime("%Y%m%d-%H%M%S")
    dateStr = now.strftime("%Y%m%d")
    letters = string.ascii_lowercase
    randomStr = ''.join(random.choice(letters) for i in range(6))
    destDir = f"{outputBaseDir}/{dateStr}"
    Path(destDir).mkdir(parents=True, exist_ok=True)

    # compose file name including extension
    ext = imghdr.what("", img_binary)
    filePath = f'{destDir}/{dateTimeStr}-{randomStr}.{ext}'
    print(f"{dateTimeLog} stored image path: {filePath}", file=sys.stdout, flush=True)
    f = open(filePath, 'wb')
    f.write(img_binary)
    f.close()

