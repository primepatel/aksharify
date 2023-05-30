+++
title = "Usage"
hascode = true
tags = ["syntax", "code"]
+++

# Usage

\toc

## Importing the module

Make sure you have installed the module

```python
from aksharify import TextArt
```

## Importing the Image

Make sure image is in your working directory or provide absolute path to the image file

```python
# input image file
art = TextArt("julia.png")
```

## Setting the dimension

```python
# set dimension of output text
art.set_dim(80)
```

## Generate TextArt

```python
# genetate text
art.asciify()
```

## See the result

```python
art.show_art()
```

## Save the Result in .txt
```python
# output into .txt file
art.text_output("output")
```
## Colored output

```python
# generate colored text using html
art.colorify()
```

### Save the result in .html

```python
# output into .html file
art.color_output("output")
```

### Save the result in .png

```python
# output into .html file
art.png_output("output")
```