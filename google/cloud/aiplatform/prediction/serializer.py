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

from fastapi import HTTPException
from fastapi import Request
from starlette.responses import JSONResponse
from typing import Dict, Optional


class Serializer:

    def deserialize(
        self,
        request: Request,
        content_type: str,
    ):
        """Deserializes the request. Invoked before predict.

        Args:
            request (Request):
                The request sent to the application.
            content_type (str):
                The specified content type of the request.
        """
        pass

    def serialize(
        self,
        predictions: Dict,
        content_type: str,
    ):
        """Invoked after predict.

        Args:
            prediction (Dict):
                The generated prediction to be sent back to clients.
            content_type (str):
                The specified content type of the response.
        """
        pass


class DefaultSerializer(Serializer):

    async def deserialize(
        self,
        request: Request,
        content_type: str,
    ):
        """Deserializes the request. Invoked before predict.

        Args:
            request (Request):
                The request sent to the application.
            content_type (str):
                The specified content type of the request.

        Returns:
            Request body.
        """
        if content_type == 'application/json':
            data = await request.json()
            return data
        else:
            raise HTTPException(
                status_code=400,
                detail="Unsupported content type of the request.",
            )

    def serialize(
        self,
        prediction: Dict,
        content_type: str,
    ):
        """Serializes the prediction. Invoked after predict.

        Args:
            prediction (Dict):
                The generated prediction to be sent back to clients.
            content_type (str):
                The specified content type of the response.

        Retuns:
            Prediction results.
        """
        if content_type == 'application/json':
            return JSONResponse(prediction)
        else:
            raise HTTPException(
                status_code=400,
                detail="Unsupported content type of the response.",
            )
