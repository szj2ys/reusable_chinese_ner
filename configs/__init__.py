# *_*coding:utf-8 *_*
from __future__ import absolute_import, division, print_function
import os
import typing

from dynaconf import Dynaconf
from os.path import dirname, abspath, join
from dataclasses import dataclass, field
from rich.console import Console

CONFIG_PATH = dirname(abspath(__file__))
settings_toml = join(CONFIG_PATH, 'settings.toml')
config_json = join(CONFIG_PATH, '.config.json')

settings = Dynaconf(
    settings_files=[settings_toml, config_json],
    # path/glob
    environments=True,  # activate layered environments
    env_switcher="ENV",  # `export MODE=production`
    load_dotenv=True,  # read a .env file
    dotenv_path="configs/.env"  # custom path for .env file to be loaded
)
Console().print(f"Using env is [bold cyan]{settings.current_env}[/bold cyan]")
