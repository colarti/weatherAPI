import zipfile
import os

def extractZip(zip, folder):
    print(f'CURRENT DIR: {os.getcwd()}')
    print(f'LIST DIR: {os.listdir()}')
    with zipfile.ZipFile(zip, 'r') as z:
        z.extractall(folder)