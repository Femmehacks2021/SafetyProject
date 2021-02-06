# Copyright 2018 Google LLC
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

# [START gae_python38_render_template]
# [START gae_python3_render_template]
import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def root():
    # For the sake of example, use static information to inflate the template.
    # This will be replaced with real information in later steps.

    return render_template('index.html')

@app.route('/emergencycall')
def emgergencyCall():
    # For the sake of example, use static information to inflate the template.
    # This will be replaced with real information in later steps.

    call_number = "+1(650)449-4279"

    return render_template('emergencyCall.html', call_number=call_number)

@app.route('/crimemap')
def crimeMap():
    # For the sake of example, use static information to inflate the template.
    # This will be replaced with real information in later steps.

    return render_template('crimeMap.html')

@app.route('/resources')
def resources():
    # For the sake of example, use static information to inflate the template.
    # This will be replaced with real information in later steps.

    return render_template('resources.html')

@app.route('/profile')
def profile():
    # For the sake of example, use static information to inflate the template.
    # This will be replaced with real information in later steps.

    return render_template('profile.html')

@app.route('/tips')
def tips():
    # For the sake of example, use static information to inflate the template.
    # This will be replaced with real information in later steps.

    return render_template('tips.html')

@app.route('/textHelpline')
def textHelpline():
    # For the sake of example, use static information to inflate the template.
    # This will be replaced with real information in later steps.

    return render_template('textHelpline.html')

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python3_render_template]
# [END gae_python38_render_template]
