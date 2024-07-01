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

import click

from zhixin.package.commands.exec import package_exec_cmd
from zhixin.package.commands.install import package_install_cmd
from zhixin.package.commands.list import package_list_cmd
from zhixin.package.commands.outdated import package_outdated_cmd
from zhixin.package.commands.pack import package_pack_cmd
from zhixin.package.commands.publish import package_publish_cmd
from zhixin.package.commands.search import package_search_cmd
from zhixin.package.commands.show import package_show_cmd
from zhixin.package.commands.uninstall import package_uninstall_cmd
from zhixin.package.commands.unpublish import package_unpublish_cmd
from zhixin.package.commands.update import package_update_cmd


@click.group(
    "pkg",
    commands=[
        package_exec_cmd,
        package_install_cmd,
        package_list_cmd,
        package_outdated_cmd,
        package_pack_cmd,
        package_publish_cmd,
        package_search_cmd,
        package_show_cmd,
        package_uninstall_cmd,
        package_unpublish_cmd,
        package_update_cmd,
    ],
    short_help="Unified Package Manager",
)
def cli():
    pass
