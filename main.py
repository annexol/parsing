from parse import ParseApps
from db import DataBase

if __name__ == '__main__':
    apps = ParseApps()
    DataBase(apps.data)
