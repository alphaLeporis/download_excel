# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import re
from urllib.error import HTTPError

from openpyxl import load_workbook
import os
import wget

from image import resize

images = ["T", "U", "V", "W", "X", "Y"]
ean_col = "D"
name_col = "E"
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Give the location of the file
    abs = os.path.dirname(os.path.abspath(__file__))
    try:
        os.mkdir(abs + "/output/")
    except FileExistsError:
        pass
    loc = (abs+"/input.xlsx")
    wb = load_workbook(filename=loc)
    sheet_ranges = wb['Export']
    currentrow = 2
    images_sum = 0
    while (sheet_ranges[name_col+str(currentrow)].value):
        ean = str(sheet_ranges[ean_col+str(currentrow)].value)
        name = re.sub(r'[^\w\-_\. ]', '_', str(sheet_ranges[name_col+str(currentrow)].value))
        workingdir = abs+"/output/"+ean+"_"+name
        os.mkdir(workingdir)
        for col in images:
            url = sheet_ranges[col+str(currentrow)].value
            if url:
                filename = url.rsplit("\\", 1)[-1].rsplit("/", 1)[-1]
                try:
                    wget.download(url, workingdir+"/"+filename)
                    resize(workingdir+"/"+filename)
                    print(filename+ " ---- OK")
                    images_sum += 1
                except HTTPError:
                    print(filename + " ---- NOT OK - HTTP error")
                    print(url)
        currentrow += 1

    print("Done!")
    print("I downloaded "+str(images_sum)+ " images! Cool.")