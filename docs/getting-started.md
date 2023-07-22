# __Getting Started__

Before we begin, make sure you have one of recent versions of Python installed on your computer.

## __Installation__

The recommended way to install Aksharify is via the python package manager, pip. Open your terminal or command prompt and run the following command:

```sh
python -m pip install aksharify
```

This command will automatically download + install Aksharify and its dependencies.

### Windows-specific Dependency

If you are using Aksharify on a Windows system, you will need to install an additional dependency. Follow these steps:

??? question "Why are there Windows specific dependencies?"
    
    Aksharify uses cairosvg package in order to export output into .png format. Cairosvg has annoying dependency problem because of cairocffi which is not built for windows. So windows users supposed to add the additional dependency as explained here [^1]. This is quite long procedure instead we can use a [quicker solution](https://stackoverflow.com/questions/73637315/oserror-no-library-called-cairo-2-was-found-from-custom-widgets-import-proje) which is by installing from an unofficial repository [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pycairo). You can choose whichever method that suits you better. For quicker solution (i.e. manually installing required binaries[^1]) follow the instuctions below.

Install pipwin using pip:

```sh
python -m pip install pipwin
```

To install binary

```sh
pipwin install cairocffi
```

We are ready to use aksharify and creating awesome Ascii art.

## __Quick Starter__

```python
from aksharify import AksharArt
from aksharify.image import Image
from aksharify.distributions import Linear
from aksharify.outputs import SVG
```

```python
image = Image("..\images\julia1.png")
image.set_dim(200)
image.show()
```

```python
lin = Linear("01")
lin.show()
```

```python
art = AksharArt(image, lin)
art.aksharify(show=True)
```

```python
config = SVG()
config.file_name = "..\\art"
config.bold = True
```

```python
art.svg_output(config)
```

_For examples from user community, please refer to the [primepatel.github.io/aksharify](https://primepatel.github.io/aksharify)_

[^1]: https://cairocffi.readthedocs.io/en/stable/overview.html