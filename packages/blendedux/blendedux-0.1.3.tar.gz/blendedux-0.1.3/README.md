Blended python flask is a web framework, it is a python module that lets you develop web applications easily. Flask is very Pythonic. It is easy to get started with Flask, because it does not have a huge learning curve. On top of that it is very explicit, which increases readability. Simply, you can install the blended python flask, specify the path of your theme, run the server and can browse your website which is running on a Blended theme.

## Installation

pip install blendedux

## Usages

#### Setup of Blended Python Flask

Run the following commands sequentially. First will create virtual environment, second will take you to the newly created virtual environment, third will activate the virtual environment and fourth will install blendedux inside the virtual environment.
```
python -m virtualenv env_name
cd env_name
Scripts\activate
pip install blendedux
```

#### Create a file name app.py in the root directory and paste below line of code and save.

```
from flask import Flask
from blendedUx import *
from blendedUx.blended_flask.bl_flask_app import Bl_Flask

PACKAGE_DIR = "themes-directory"

app = Bl_Flask(__name__, package_dir= PACKAGE_DIR)

user_name = 'user_name'
theme_name = 'theme_name'
password = ''

theme = app.load(theme_name, user_name)

@app.route("/css/<path:path>")
@get_css('css_path')
def css():
   pass
@app.route("/media/<path:path>")
@get_media('media_path')
def media():
    pass
@app.route("/js/<path:path>")
@get_js('js_path')
def js():
    pass

@app.route('/')
def home(**kwargs):
    """
    """
    context = theme
    file_content = get_template('home.html')
    try:
        return render_code(file_content, context)
    except UnicodeDecodeError:
        return render_code(file_content.decode('utf-8'), context)

if __name__ == "__main__":
    app.run()
```
Note: Please specify your path in the package directory. You can point to your working directory which you have set up during cli and make sure that blended directory structures is there and it has a valid blended theme. Password is optional.
For an example:
```
PACKAGE_DIR = "C:/Users/themes" 
user_name = 'blended' 
theme_name = 'base_theme' 
password = '' 
```
#### How to Include the theme into your flask application?

Create a templates directory in the root and create a home.html inside the templates directory and paste below line of code in the home.html and save.

```
{% extends theme.template.home|template %} 
{% block title %}
<title>My Blended Site </title> 
{% endblock title %} 
{% block css %}
<link rel="stylesheet" href="{{css(theme)}}">
{% endblock %}
```
Note: It is extending the home template of the theme. Extending a predefined Blended template should allow you to add a new page in your flask application. This host template is extending the theme base template named as home.html. Base templates are part of Blended theme which resides in the html directory.For an example:
```
{% extends theme.template.home|template %}
```
#### Run the Flask Server

python app.py

Just load the below URL (http://localhost:5000/) in a browser to see the output.


## API

#### CSS ENDPOINT
By default, the /static directory will serve the static contents. If you want to provide the path of CSS then you can change this by following API:
```
  @app.route("/css/<path:path>")
  @get_css("css_path") 
  def css(): 
    pass
```
Note: User will need to give the absolute path in the css_path like this @get_css("C:/blendedUx/static/css")

#### Js ENDPOINT
By default, the /static directory will serve the static contents. If you want to provide the path of js then you can change this by following API:
```
  @app.route("/js/<path:path>")
  @get_js("js_path") 
  def js(): 
    pass
```
Note: User will need to give the absolute path in the js_path like this @get_js("C:/blendedUx/static/js")    

#### Media ENDPOINT

Add Media Endpoint
By default application will host the media at /static directory in the root but you can change this by following API:
```
  @app.route("/media/<path:path>")
  @get_media("media_path") 
  def media(): 
     pass
```
Note: User will need to give the absolute path in the media_path like this @get_media("C:/blendedUx/static/media") 

#### Add Route
```
  @app.route("/")
  def home(**kwargs):
    """
    """
    context = theme 
    file_content = get_template("home.html")
    try:
      return render_code(file_content, context)
    except UnicodeDecodeError:
      return render_code(file_content.decode("utf-8"), context)
```
Note: It is registering the root URL for your application. This route is rendering a home.html template file by accepting the Blended theme context object. The home.html is a Blended host template and you can add many more as per your requirements in templates directory and then define a route for that template based on above code snippet in app.py. 
 
For more details go to [Quickstart Python Flask](https://hub.blended.co/learn/quickstart_blended_flask/)

## License
MIT
