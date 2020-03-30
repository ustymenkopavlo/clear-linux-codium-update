# -*- coding: utf-8 -*-
import urllib
from bs4 import BeautifulSoup

import os


def update(url, package):
    os.system('wget ' + url)
    os.system('sudo rpm -U --nodeps ' + package)
    os.system('rm ' + package)


def getHeader(arrayOfObj):
    headerDiv = arrayOfObj.find('div', {'class', 'release-header'})
    headerA = headerDiv.find('div', {'class', 'f1'})
    return headerA.find('a').text


def getUpdateName(arrayOfObj):
    for item in arrayOfObj:
        parsedItem = item.find('span', {'class': 'flex-auto'}).text
        if parsedItem[-4:] == '.rpm':
            return parsedItem


def get():
    url = 'https://github.com/vscodium/vscodium/releases'
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    lastRelease = soup.find('div', {'class': 'release-main-section'})
    items = lastRelease.find_all('div', {'class': 'Box-body'})
    header = getHeader(lastRelease)
    updatename = getUpdateName(items)
    url = 'https://github.com/VSCodium/vscodium/releases/download/' + \
        header + '/' + updatename
    update(url, updatename)


if __name__ == "__main__":
    get()
