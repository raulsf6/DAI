from flask import Flask
from flask import render_template
from flask import request
from PIL import Image
from random import random

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/user/<name>')
def get_user(name):
    return render_template("users.html", user=name)

@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404


@app.route('/mandelbrot')
def get_mandelbrot():
    # get params
    x1 = float(request.args.get('x1'))
    x2 = float(request.args.get('x2'))
    y1 = float(request.args.get('y1'))
    y2 = float(request.args.get('y2'))

    c = complex(random() * 2.0 - 1.0, random() - 0.5)
    
    maxIt = 256
    # image size
    imgx = 512
    imgy = 512
    image = Image.new("RGB", (imgx, imgy))

    for y in range(imgy):
        zy = y * (y2 - y1) / (imgy - 1)  + y1
        for x in range(imgx):
            zx = x * (x2 - x1) / (imgx - 1) + x1
            z = complex(zx, zy)
            n = mandelbrot(z, c, maxIt)
            r = n % 4 * 64
            g = n % 8 * 32
            b = n % 16 * 16
        
            image.putpixel((x, y), b * 65536 + g * 256 + r)
    
    image.save("./static/mandelbrot.png", "PNG")

    return render_template('mandelbrot.html', x1=x1, x2=x2, y1=y1, y2=y2)

        

def mandelbrot(z, c, maxIt):
    for n in range(maxIt):
        if abs(z) > 2:
            break
        z = z * z + c
    return n