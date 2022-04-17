import os
import re

from telegram import *
from telegram.ext import *

API_KEY = os.getenv("TG_API_KEY")
CHANNEL = os.getenv("TG_CHANNEL_ID")


def send_to_channel(project):
    if os.getenv("ENVIRONMENT", None) == "test":
           return
    bot = Bot(API_KEY)
    obj = f"""
user : {project.user.username}
title : {project.title}
description : {project.description}
project_link : {project.project_link}
"""
    bot.send_message(CHANNEL, obj)
    return
