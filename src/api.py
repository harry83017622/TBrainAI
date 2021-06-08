from argparse import ArgumentParser
import base64
import datetime
import time
import hashlib
from pathlib import Path

import cv2
from flask import Flask
from flask import request
from flask import jsonify
from flask_executor import Executor
import numpy as np
import utils.imagestore as imagestore
from utils.tools import tesseractModel

model = tesseractModel()

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['EXECUTOR_TYPE'] = 'thread'
app.config['EXECUTOR_MAX_WORKERS'] = 10
executor = Executor(app)
request_img_output_dir = None

####### PUT YOUR INFORMATION HERE #####################
CAPTAIN_EMAIL = 'bgrhythm@yahoo.com.tw'               #
SALT = 'my_salt_4e5d9829-c533-49ca-93d9-1ccab209721f' #
#######################################################


def generate_server_uuid(input_string):
    """ Create your own server_uuid.

    @param:
        input_string (str): information to be encoded as server_uuid
    @returns:
        server_uuid (str): your unique server_uuid
    """
    s = hashlib.sha256()
    data = (input_string + SALT).encode("utf-8")
    s.update(data)
    server_uuid = s.hexdigest()
    return server_uuid


def base64_to_binary_for_cv2(image_64_encoded):
    """ Convert base64 to numpy.ndarray for cv2.

    @param:
        image_64_encode(str): image that encoded in base64 string format.
    @returns:
        image(numpy.ndarray): an image.
    """
    img_base64_binary = image_64_encoded.encode("utf-8")
    img_binary = base64.b64decode(img_base64_binary)
    image = cv2.imdecode(np.frombuffer(img_binary, np.uint8), cv2.IMREAD_COLOR)
    return image

def asnyc_base64_to_image_file(outputDir, image_64_encoded):
    executor.submit(imagestore.base64_to_image_file, outputDir, image_64_encoded)

def predict(image):
    """ Predict your model result.

    @param:
        image (numpy.ndarray): an image.
    @returns:
        prediction (str): a word.
    """

    ####### PUT YOUR MODEL INFERENCING CODE HERE #######
    # prediction = '陳'
    img_process = model.img_preprocessing_(image)
    prediction = model.predict_(img_process)

    ####################################################
    if _check_datatype_to_string(prediction):
        return prediction


def _check_datatype_to_string(prediction):
    """ Check if your prediction is in str type or not.
        If not, then raise error.

    @param:
        prediction: your prediction
    @returns:
        True or raise TypeError.
    """
    if isinstance(prediction, str):
        return True
    raise TypeError('Prediction is not in string type.')


@app.route('/inference', methods=['POST'])
def inference():
    """ API that return your model predictions when E.SUN calls this API. """
    data = request.get_json(force=True)

    # 自行取用，可紀錄玉山呼叫的 timestamp
    esun_timestamp = data['esun_timestamp']

    # 取 image(base64 encoded) 並轉成 cv2 可用格式
    image_64_encoded = data['image']
    asnyc_base64_to_image_file(request_img_output_dir, image_64_encoded) # save image file
    image = base64_to_binary_for_cv2(image_64_encoded)

    t = datetime.datetime.now()
    ts = str(int(t.utcnow().timestamp()))
    server_uuid = generate_server_uuid(CAPTAIN_EMAIL + ts)

    try:
        answer = predict(image)
    except TypeError as type_error:
        # You can write some log...
        raise type_error
    except Exception as e:
        # You can write some log...
        raise e
    server_timestamp = round(time.time())

    return jsonify({'esun_uuid': data['esun_uuid'],
                    'server_uuid': server_uuid,
                    'answer': answer,
                    'server_timestamp': server_timestamp})


if __name__ == "__main__":
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
    )
    arg_parser.add_argument('-p', '--port', default=8080, help='port')
    arg_parser.add_argument('-d', '--debug', default=True, help='debug')
    arg_parser.add_argument('-i', '--dirOfRequestImage', default="/home/tbrain/req-images", help='directory of request image to save')
    options = arg_parser.parse_args()

    request_img_output_dir = options.dirOfRequestImage.rstrip("/")
    Path(request_img_output_dir).mkdir(parents=True, exist_ok=True)
    print(f'request image output directory: {request_img_output_dir}')

    app.run(debug=options.debug, port=options.port, host='0.0.0.0')
