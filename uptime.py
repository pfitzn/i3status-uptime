#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 18:17:28 2022

@author: pat
"""

import subprocess
import datetime

raw_uptime = subprocess.check_output('cat /proc/uptime', shell=True)
text_uptime = raw_uptime.decode('utf-8').split()[0]
raw_formatted = datetime.timedelta(seconds=(float(text_uptime)))
well_formatted = str(raw_formatted).split(".")[0]
strip_seconds = well_formatted[:-3]
print(strip_seconds)
