# This module is just a fancy way to get settings from file and/or environment variables

import os

token = os.getenv('TOKEN', '')
