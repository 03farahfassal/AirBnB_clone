#!/usr/bin/python3
"""This module creates a unique FileStorage
for the application
"""


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
