# Copyright 2015 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_flex_quickstart]
import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import local_analysis
app = Flask(__name__)

upload_folder = os.path.join('static', 'Image')
read_folder = os.path.join('static', 'Image')
app.config['UPLOAD'] = upload_folder
app.config['READ'] = read_folder
@app.route('/', methods=['GET', 'POST'])
def analyze():
    #return "hello world"
    if request.method == 'GET':
        return render_template('image_render.html', out="Please submit the file and wait for approximately one minute.")

    if request.method == 'POST':
       file = request.files['img']
       filename = secure_filename(file.filename)
       file.save(os.path.join(app.config['UPLOAD'], filename))

       out = local_analysis.analyze('static/Image', filename)

       folder_100_1push0_7413_pth = os.path.join(app.config['READ'], 'vgg19', '001', '100_1push0.7413.pth')
       app.config['100_1push0_7413_pth'] = folder_100_1push0_7413_pth

       original_img = os.path.join(app.config['100_1push0_7413_pth'], 'original_img.png')
       most_activated_prototypes_folder = os.path.join(app.config['100_1push0_7413_pth'], 'most_activated_prototypes')

       app.config['MOST_ACTIVATED_PROTOTYPES'] = most_activated_prototypes_folder
       prototype_activation_map_by_top_1_prototype_png = os.path.join(app.config['MOST_ACTIVATED_PROTOTYPES'],  'prototype_activation_map_by_top-1_prototype.png')
       prototype_activation_map_by_top_2_prototype_png = os.path.join(app.config['MOST_ACTIVATED_PROTOTYPES'],  'prototype_activation_map_by_top-2_prototype.png')
       prototype_activation_map_by_top_3_prototype_png = os.path.join(app.config['MOST_ACTIVATED_PROTOTYPES'],  'prototype_activation_map_by_top-3_prototype.png')
       prototype_activation_map_by_top_4_prototype_png = os.path.join(app.config['MOST_ACTIVATED_PROTOTYPES'],  'prototype_activation_map_by_top-4_prototype.png')
       prototype_activation_map_by_top_5_prototype_png = os.path.join(app.config['MOST_ACTIVATED_PROTOTYPES'],  'prototype_activation_map_by_top-5_prototype.png')
       prototype_activation_map_by_top_6_prototype_png = os.path.join(app.config['MOST_ACTIVATED_PROTOTYPES'],  'prototype_activation_map_by_top-6_prototype.png')
       prototype_activation_map_by_top_7_prototype_png = os.path.join(app.config['MOST_ACTIVATED_PROTOTYPES'],  'prototype_activation_map_by_top-7_prototype.png')
       prototype_activation_map_by_top_8_prototype_png = os.path.join(app.config['MOST_ACTIVATED_PROTOTYPES'],  'prototype_activation_map_by_top-8_prototype.png')
       prototype_activation_map_by_top_9_prototype_png = os.path.join(app.config['MOST_ACTIVATED_PROTOTYPES'],  'prototype_activation_map_by_top-9_prototype.png')
       prototype_activation_map_by_top_10_prototype_png = os.path.join(app.config['MOST_ACTIVATED_PROTOTYPES'],  'prototype_activation_map_by_top-10_prototype.png')

       return render_template('image_render.html',
                    original_img=original_img,
                    prototype_activation_map_by_top_1_prototype_png=prototype_activation_map_by_top_1_prototype_png,
                    prototype_activation_map_by_top_2_prototype_png=prototype_activation_map_by_top_2_prototype_png,
                    prototype_activation_map_by_top_3_prototype_png=prototype_activation_map_by_top_3_prototype_png,
                    prototype_activation_map_by_top_4_prototype_png=prototype_activation_map_by_top_4_prototype_png,
                    prototype_activation_map_by_top_5_prototype_png=prototype_activation_map_by_top_5_prototype_png,
                    prototype_activation_map_by_top_6_prototype_png=prototype_activation_map_by_top_6_prototype_png,
                    prototype_activation_map_by_top_7_prototype_png=prototype_activation_map_by_top_7_prototype_png,
                    prototype_activation_map_by_top_8_prototype_png=prototype_activation_map_by_top_8_prototype_png,
                    prototype_activation_map_by_top_9_prototype_png=prototype_activation_map_by_top_9_prototype_png,
                    prototype_activation_map_by_top_10_prototype_png=prototype_activation_map_by_top_10_prototype_png,
                    out=out)


if __name__ == "__main__":
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app.
    app.run(host="127.0.0.1", port=8080, debug=True)
# [END gae_flex_quickstart]
