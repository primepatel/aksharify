## __Overview__

Aksharify is Python package that enables users to transform images into captivating ASCII art representations. This sophisticated tool provides a straightforward four-step process, allowing individuals to explore the realm of visual expression with ease and creativity.

1. Load Image: Utilize the Image class to load the image you want to transform into ASCII art. You can provide either a local file path or a URL for loading.

2. Customize Distribution: Choose the desired distribution (e.g., Linear, Exponential or Normal) using the corresponding classes from the distributions module.

3. Generate ASCII Art: Create an AksharArt object by passing the loaded image and chosen distribution. Use the aksharify method to generate captivating ASCII art.

4. Output Art: Select an output file format (e.g., PDF, PNG, or SVG) by configuring the appropriate output class. Use the export method to save your final ASCII art.

## __Step 1: Load Image__

The `Image` class in "aksharify" loads and preprocesses images for ASCII art generation. You can load an image using the file path or URL. Use the `resize` method to adjust the dimensions, affecting the number lines and the number of characters in each line. The `Image` class allows you to specify either the width or height for resizing, and it automatically maintains the aspect ratio for distortion-free resizing. Optional normalization scales pixel values for enhanced visual quality. 
The show() method in "aksharify" previews the image used for ASCII art. Use grayscale=True to display the grayscale version.

Examples:
```python
from aksharify.image import Image

# Example 1: Load image from file path
image = Image(path="path/to/your/image.jpg")
image.resize(width=100, height=80)
image.normalize()

# Example 2: Load image from URL
image_url = "https://example.com/your-image.jpg"
image = Image(url=image_url)
image.resize(width=120, height=90)

# Both images are now ready for ASCII art with AksharArt class.

# Show the colored image
image.show()

# Show the grayscale version of the image
image.show(grayscale=True)
```

### __When resizing images for ASCII art, consider these key factors:__

- Aspect Ratio: Maintain the aspect ratio to prevent distortion and accurately represent the image.

- Level of Detail: Image dimensions affect the amount of detail in ASCII art. Smaller images simplify the representation, while larger ones offer more intricacy.

- Performance: Resizing to smaller dimensions reduces the character count, enhancing rendering speed and processing efficiency.

## __Step 2: Customize Distribution__


In the context of the Aksharify package, "distribution" refers to a method of arranging characters in the ASCII art representation based on their density or occurrence in the image. The distribution determines how the characters are assigned to different regions of the image based on the pixel values.

Aksharify offers different distribution options to users, each providing a unique way of generating ASCII art:

### __Linear Distribution__
The linear distribution assigns characters linearly based on their order in the specified character set. It is a simple and non-customizable distribution where characters are distributed evenly across the image.

### __Exponential Distribution__
The exponential distribution allows users to control the character density using a power parameter. Higher power values concentrate characters in darker regions of the image, creating a visually striking effect.

### __Normal Distribution__

The normal distribution enables users to emphasize specific regions of an image in ASCII art by adjusting the mean and standard deviation. The mean determines the central region with denser characters, while the std controls spread.

---

Common Parameters:

- chars::string (default='@%#*+=;:-,. '): The character set used for ASCII art representation.
- order::bool (default=False): If True, characters are selected based on their pixel density, creating a more organized output.

Exponential Distribution Specific Parameter:

- power::float (default=1.0): Controls the rate of change in character density. Lower values create "ultra-light" images, higher values produce "dark" images.

Normal Distribution Specific Parameters:

- mean::float (default=0.5): Represents the mean of the normal distribution, controlling the central character density.
- var::float (default=0.1): The var parameter controls the character spread around the mean, enabling emphasis on specific regions.

---

The package offers a "show" method for each distribution, generating graphs illustrating character assignments to pixel ranges. These graphs provide valuable insights into the behavior of each distribution, helping users select the most suitable one for their creative requirements.

__Examples__

1. Linear Distribution:
   ```python
   from aksharify.distributions import Linear

   linear = Linear(chars=" .:-=+*#%@")
   linear.show()
   ```

2. Exponential Distribution:
   ```python
   from aksharify.distributions import Exponential

   exponential = Exponential(chars="@%#*+=:- .", power=2.0)
   exponential.show()
   ```

3. Normal Distribution:
   ```python
   from aksharify.distributions import Normal

   normal = Normal(chars="@%#*+=:- .", mean=0.5, std_dev=0.2)
   normal.show()
   ```

Using these methods, you can explore different distribution options to create unique and visually captivating ASCII art from your images.

## __Step 3: Generate ASCII Art__

In the third step, we create an instance of the AksharArt class by providing the loaded image and the configured distribution as inputs. This allows us to generate ASCII art from the given image using the specified distribution.

```python
from aksharify import AksharArt
from aksharify.image import Image
from aksharify.distributions import Linear

# Load the image
image = Image("path/to/image.jpg")
image.resize(100)  # Resize the image to 100 characters in width (aspect ratio maintained)

# Configure the distribution
distribution = Linear("01")  # Linear distribution with characters "01"

# Create the AksharArt instance and generate ASCII art
art = AksharArt(image, distribution)
art.aksharify() # art.aksharify(show=True) for displaying there itself

# Display the ASCII art
art.show()
```

## __Step 4: Configure and Generate Output__

Aksharify supports various output formats to export the generated ASCII art. The supported formats are:

**SVG**: Vector-based representations for various graphics applications.

__Attributes:__

 <!-- - `font_family` (str): The font family to be used for the ASCII art. -->
 - `font_size` (int): The font size to be used for the ASCII art.
 - `background_color` (str): The background color of the SVG image.
 <!-- - `link` (str): A link to be added to the SVG image (optional). -->
 - `bold` (bool): Whether the ASCII art should be displayed in bold.
 - `fill_color` (str): The color to fill the ASCII characters (optional).
 - `file_name` (str): The default name for saving the SVG output file.


**PNG**: Visual details preserved for web usage and projects.

Attributes (In addition to SVG attributes):

 - `width` (int or None): The width of the PNG image in pixels. If `None`, the width will be determined by the content.
 - `height` (int or None): The height of the PNG image in pixels. If `None`, the height will be determined by the content.

**PDF**: High-quality output for sharing and printing.

Attributes (Same as SVG attributes):

**EPS** (Encapsulated PostScript): Scalable vector graphics for embedding in documents.

Attributes (Same as SVG attributes):

**TXT** (Plain Text): Simple and readable representations in text editors and terminals.

Attributes:

 - `file_name` (str): The default name for saving the SVG output file.

**HTML**: Interactive visualizations for web integration.

Attributes:

 - `font_family` (str): The font family to be used for the ASCII art.
 - `font_size` (int): The font size to be used for the ASCII art.
 - `bold` (bool): Whether the ASCII art should be displayed in bold.
 - `file_name` (str): The default name for saving the HTML output file.

We can save the ASCII art in different output formats specified above, by configuring the output options accordingly. Each output class provides attributes that allow you to customize the visual appearance of your ASCII art.

```python
# Example 1: Generating ASCII Art and Saving as SVG
from aksharify import AksharArt
from aksharify.image import Image
from aksharify.distributions import Linear
from aksharify.outputs import SVG

# Load Image
image = Image("path/to/image.jpg")
image.resize(150)

# Configure Distribution
distribution = Linear(chars="01")

# Create AksharArt object and Generate ASCII Art
art = AksharArt(image, distribution)
art.aksharify(show=False)

# Configure and Generate SVG Output
svg_config = SVG()
svg_config.file_name = "art"
svg_config.bold = True
art.export(svg_config)
```

The `.export()` method of the `AksharArt` class in Aksharify can accept multiple arguments, enabling users to provide multiple output configurations in a single call.

With this straightforward configuration-based approach, Aksharify ensures a clean and consistent interface to produce stunning ASCII art representations of your images. Experiment with various distributions and output formats to create unique art!
