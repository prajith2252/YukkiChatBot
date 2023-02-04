#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/YukkiChatBot >.
#
# This file is part of < https://github.com/TeamYukki/YukkiChatBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiChatBot/blob/master/LICENSE >
#
# All rights reserved.
#

from os import getenv

from dotenv import load_dotenv

load_dotenv()

# Get it from my.telegram.org
API_ID = 9301845#int(getenv("API_ID"))
API_HASH = '563e9fd30b529442b705c7230f766b83'#getenv("API_HASH")

## Get it from @Botfather in Telegram.
BOT_TOKEN = "5423234125:AAF3MaDrImAN9TOasM_A6MUNyBP4tNUfR1g"#getenv("BOT_TOKEN")

# SUDO USERS
SUDO_USER = list(
    map(int, getenv("SUDO_USER", "1952992043").split())
)  # Input type must be interger

# You'll need a Private Group ID for this.
LOG_GROUP_ID = "-1001785407908"#int(getenv("LOG_GROUP_ID"))

# Message to display when someone starts your bot
PRIVATE_START_MESSAGE = "Hello 👋, Thanks for Contacting TMA Support.\n\nPlease Join our :- \nUpdates Channel @Tmaadda  \nBackup channel @TMABackup. "#getenv(
  #  "PRIVATE_START_MESSAGE",
    #"Hello! Welcome to my Personal Assistant Bot",
#)

# Database to save your chats and stats... Get MongoDB:-  https://notreallyshikhar.gitbook.io/yukkimusicbot/deployment/mongodb#4.-youll-see-a-deploy-cloud-database-option.-please-select-shared-hosting-under-free-plan-here
MONGO_DB_URI = "mongodb+srv://tma:tma@cluster0.3pigxvy.mongodb.net/?retryWrites=true&w=majority"# getenv("MONGO_DB_URI", None)
