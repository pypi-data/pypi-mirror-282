# Copyright (c) 2014-present ZhiXin <contact@ZhiXin-Semi.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ajsonrpc.core import JSONRPC20DispatchException

from zhixin.compat import aio_to_thread
from zhixin.home.rpc.handlers.base import BaseRPCHandler
from zhixin.registry.client import RegistryClient


class RegistryRPC(BaseRPCHandler):
    @staticmethod
    async def call_client(method, *args, **kwargs):
        try:
            client = RegistryClient()
            return await aio_to_thread(getattr(client, method), *args, **kwargs)
        except Exception as exc:  # pylint: disable=bare-except
            raise JSONRPC20DispatchException(
                code=5000, message="Registry Call Error", data=str(exc)
            ) from exc
