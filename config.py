"""Configuration for FastNote"""
import os
import pathlib

default_path = os.path.expanduser('~/fastnote.txt')
text_path = os.getenv('FASTNOTE_PATH', default_path)
