# Copyright 2020 Google LLC
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

import os

import pytest

import video_detect_faces_gcs

RESOURCES = os.path.join(os.path.dirname(__file__), "resources")


@pytest.mark.flaky(max_runs=3, min_passes=1)
def test_detect_faces(capsys):
    input_uri = "gs://cloud-samples-data/video/googlework_short.mp4"

    video_detect_faces_gcs.detect_faces(gcs_uri=input_uri)

    out, _ = capsys.readouterr()

    assert "Face detected:" in out
