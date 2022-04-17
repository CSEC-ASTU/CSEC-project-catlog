import os

from telegram import *
from telegram.ext import *

API_KEY = os.getenv("TG_API_KEY")
CHANNEL = os.getenv("TG_CHANNEL_ID")


bot = Bot(API_KEY)


def send_to_channel(project):
    obj = ""
    obj += f"user : {project.user.username} \n"
    obj += f"title : {project.title} \n"
    obj += f"description : {project.description} \n"
    obj += f"project_link : {project.project_link} \n"

    keyboard = [[InlineKeyboardButton("Browse", url=project.project_link)]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    """
    Error when i try to add inlinekeyboradbutton
    
       Error = Object of type InlineKeyboardMarkup is not JSON serializable

    Since we've prject link we dont need to have redirecting button... I think  
    """

    bot.send_message(CHANNEL, obj)
