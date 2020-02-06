import shutil, os
from pathlib import Path
import json
import Backup
import PyQt5

class Application():
    config = {}

    def init(self):
        self.config()

    def getConfig(self):
        with open('config.json') as configFile:
            self.config = json.loads(configFile)

    def writeConfig(self):
        with open('config.json') as configFile:
            configFile.write(json.dumps(self.config))

    def setBackupFolder(self, folder):
        self.config['paths']['backups'] = folder
        self.writeConfig()

    def setUIConfigFolder(self, folder):
        self.config['paths']['uiConfig'] = folder
        self.writeConfig()

    def setWoWFolder(self, folder):
        self.config['paths']['wow'] = folder
        self.writeConfig()

    def setAccountname(self, name):
        self.config['account']['name'] = name
        self.writeConfig()

    def setRealm(self, realm):
        self.config['account']['realm'] = realm
        self.writeConfig()

    def setCharacters(self, characters):
        self.config['account']['characters'] = characters
        self.writeConfig()

    def backupWTF(self):
        Backup.toZip(self.config['paths']['wow'], self.config['paths']['backups'])