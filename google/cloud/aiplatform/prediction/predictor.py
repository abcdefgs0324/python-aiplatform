# -*- coding: utf-8 -*-

# Copyright 2021 Google LLC
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
#

from typing import Dict, Optional


class Predictor:
    """Interface for Predictor class that users would be implementing."""

    def __init__(self):
        pass

    def load(self, model_uri: Optional[str] = None):
        """Loads the model.

        Args:
            model_uri (Optional[str]):
                The environment variable of AIP_STORAGE_URI.
        """
        pass

    def predict(self, request_body: Dict) -> Dict:
        """Performs custom prediction.

        Args:
            request_body (Dict):
                The JSON deserialized prediction request body.

        Returns:
            predictions (Dict):
                Prediction. The returned value must be JSON serializable.
        """
        pass
