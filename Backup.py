import zipfile, shutil, os
from pathlib import Path
from datetime import datetime

def toZip(folder, output):
    folder = os.path.abspath(folder)
    output = os.path.abspath(output)
    date = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    while True:
        zipFilename = os.path.basename(folder) + '_' + date + '.zip'
        if not os.path.exists(zipFilename):
            break

    backupZip = zipfile.ZipFile(zipFilename, 'w')

    for foldername, subfolders, filenames in os.walk(folder):
        backupZip.write(foldername)
        for filename in filenames:
            newBase = os.path.basename(folder) + "_"
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
