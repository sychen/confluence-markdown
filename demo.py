#!/usr/bin/env python


from __future__ import print_function

import sys
import os
import collections
import json
import inspect
import time
import getpass
import re
import datetime
import argparse


def get_script_directory():
    return os.path.realpath(
        os.path.dirname(
            inspect.getfile(
                get_script_directory)))


def change_python_intepreter():
    script_directory = get_script_directory()
    environment = os.path.join(script_directory, 'environment')

    print('environment:', environment)

    # Create virtualenv outside the git repositories,
    # because git clean are always executed.

    if not os.path.exists(environment):
        print("Virtualenv is not found, initializing")
        os.system(os.path.join(script_directory, 'initialize-virtualenv'))

    print("Relaunching from virtualenv")

    path_of_python = os.path.join(environment, 'bin', 'python')

    print('path_of_python:', path_of_python)

    os.execv(path_of_python, [path_of_python] + sys.argv)


try:
    import requests
    from jinja2 import Environment, FileSystemLoader
    from jira import JIRA
    from flask import Flask, render_template
    import ntplib
    import markdown
except Exception as e:
    print(e)
    print("Trigger virtualenv initialization")
    change_python_intepreter()


if __name__ == "__main__":
    pass


