# 2020-01-01-upload.pdf

import requests
base_url = "http://127.0.0.1:8080/"
option = input("options: d: download r: results, t: test: \n")


def months():
    for i in range(1, 13):
        if i < 10:
            i = f"0{i}"
            days(i)
        else:
            days(i)


def days(month):
    for i in range(1, 32):
        if i < 10:
            i = f"0{i}"
            filename(month, i)
        else:
            filename(month, i)


def filename(month, day):
    file = f"2020-{day}-{month}-upload.pdf"
    if option != "t":
        get_document(file)
    else:
        print(base_url + file)


def get_document(file):
    url = base_url + file
    req = requests.get(url)
    status = req.status_code

    if status != 404:
        if option == "d":
            download(req, file)
        if option == "r":
            results(url)


def download(req, file):
    pdf_file = open(file, "wb")
    pdf_file.write(req.content)
    pdf_file.close


def results(url):
    file = open('results.txt', "a")
    file.write(url + "\n")
    file.close


if __name__ == '__main__':
    months()
