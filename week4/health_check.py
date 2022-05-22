#! /usr/bin/env python3

"""
This Python script should send an email if there are problems, such as:
* Report an error if CPU usage is over 80%
* Report an error if available disk space is lower than 20%
* Report an error if available memory is less than 500MB
* Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"
"""

import os
import shutil
import psutil
import socket
from emails import generate_error_report, send_email

def check_cpu_usage():
    -- VISUAL --
