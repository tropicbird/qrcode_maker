# README

This repository is for simply creating a QRcode of strings in Python.

# Install packages

```
pip install -r requirements.txt
```

# Usage

```
import qrcode
img = qrcode.make('https://www.yahoo.co.jp/')
img.save('qrcode.png')
```
