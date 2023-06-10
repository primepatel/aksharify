from aksharify import TextArt, URLtoImg

# img = URLtoImg("url")
img = "../julia.png"

art = TextArt(img)
art.set_dim(80)
art.set_font_size(20)
art.asciify()
art.svgify(bold=True)
art.svg_output("../main.svg")