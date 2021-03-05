# -------------------------------------- #
import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from WhiteEyeUserBot.Configs import Config
from WhiteEyeUserBot.db_start import BASE, SESSION

# -------------------------------------- #
