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

from zhixin.exception import ZhixinException, UserSideException


class ProjectError(ZhixinException):
    pass


class NotZhiXinProjectError(ProjectError, UserSideException):
    MESSAGE = (
        "Not a ZhiXin project. `zhixin.ini` file has not been "
        "found in current working directory ({0}). To initialize new project "
        "please use `zhixin project init` command"
    )


class InvalidProjectConfError(ProjectError, UserSideException):
    MESSAGE = "Invalid '{0}' (project configuration file): '{1}'"


class UndefinedEnvPlatformError(ProjectError, UserSideException):
    MESSAGE = "Please specify platform for '{0}' environment"


class ProjectEnvsNotAvailableError(ProjectError, UserSideException):
    MESSAGE = "Please setup environments in `zhixin.ini` file"


class UnknownEnvNamesError(ProjectError, UserSideException):
    MESSAGE = "Unknown environment names '{0}'. Valid names are '{1}'"


class InvalidEnvNameError(ProjectError, UserSideException):
    MESSAGE = (
        "Invalid environment name '{0}'. The name can contain "
        "alphanumeric, underscore, and hyphen characters (a-z, 0-9, -, _)"
    )


class ProjectOptionValueError(ProjectError, UserSideException):
    pass
