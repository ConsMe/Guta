import requests

import cv2
import imutils
import numpy as np


urls = ['https://i.imgur.com/sjVZKOo.jpg',
        'https://i.imgur.com/6UihTbh.jpg',
        'https://i.imgur.com/txRM3L7.jpg',
        'https://i.imgur.com/enU5kd4.jpg',
        'https://i.imgur.com/lgzUGRe.jpg',
        ]
images = []
for i, url in enumerate(urls):
    print(f"[INFO] download image #{str(i+1)}")
    response = requests.get(url, stream=True).raw
    image = np.asarray(bytearray(response.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    images.append(image)
print("[INFO] stitching images...")
stitcher = cv2.createStitcher() if imutils.is_cv3() else cv2.Stitcher_create()
(status, stitched) = stitcher.stitch(images)
if status == 0:
    cv2.namedWindow("output", cv2.WINDOW_NORMAL)
    im_show = imutils.resize(stitched, width=1900)
    cv2.imshow("Stitched", im_show)
    cv2.waitKey(0)
    # cv2.imwrite('out.jpg', stitched)
else:
    print("[INFO] image stitching failed ({})".format(status))
