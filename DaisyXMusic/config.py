# DAISYXMUSIC- Telegram bot project
# Copyright (C) 2021  Roj Serbest
# Copyright (C) 2021  Inuka Asith
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# Modified by Inukaasith

import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQBXdOzmQ5XIm9xnH0jN2nkvr8ismbOk23EXSgvz18HZs_Z1t426KRowQw7QSQAd876V3gNgbWz9CzgjrIHbvjlWi8Jq2T4GvAntXpJop8d647ucMPQUbVsAf7-bqY9usBLICb-AKPeJ7nt2YjkFJmJopS0DtHxUJUxiQhXEC2VfAO5DxvhSudtuoUKfZhSbAF_H-p82tNEQwt0bSTUY9kfBJauRuWk7IMZqV5L_jeCJ_CmSALGWqrlagzwVF-npBsJUJar8SrXtjky7cZ68OIriK9o-pCDJerzR46f-Q3QxJb2Oj2IrOVqM4qPbJHL97QKkezfsgWKlHEVEWQcbkiVqVmdKvwA")
BOT_TOKEN = getenv("BOT_TOKEN","1978000206:AAH8RZdfyTz4iefS978gUIaespDFLWsNJ8Q")
BOT_NAME = getenv("BOT_NAME", "kingdom family grpup help bot")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "kingdom_family_chanel")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/5a27d60b051ec1bf17dd0.jpg")
admins = {}
API_ID = int(getenv("API_ID", "7635212"))
API_HASH = getenv("API_HASH","d2ff99e45bef6b7f94628277f888a644")
BOT_USERNAME = getenv("BOT_USERNAME", "kingdom_family_help_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "kingdom_music")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "kingdom_family")
PROJECT_NAME = getenv("PROJECT_NAME", "kingdom family music")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/TeamDaisyX/DaisyXMusic")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS","1985638127").split()))
