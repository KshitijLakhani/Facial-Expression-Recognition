import os
import numpy as np
import csv
from PIL import Image

photos_base_path = os.path.abspath(os.path.join(os.path.dirname(__file__) + '/photos/'))
data_kind = "PrivateTest"
emotion_mappings = {'angry': '0',
                    'disgust': '1',
                    'fear': '2',
                    'happy': '3',
                    'sad': '4',
                    'surprise': '5',
                    'neutral': '6'}
to_write = list()
to_write.append(["pixels", "Usage"])

for subdir, dirs, files in os.walk(photos_base_path):
    for file in files:
        curr_emotion = emotion_mappings[str(file.split('-')[0])]
        im = Image.open(os.path.join(subdir, file)).convert('L')
        pixels = list(im.getdata())
        width, height = im.size
        pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
        pixels = np.asarray(pixels).flatten().tolist()
        img_str = ' '.join(map(str, pixels))
        to_write.append([img_str, data_kind])

with open("test_data.csv", 'w') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(to_write)
