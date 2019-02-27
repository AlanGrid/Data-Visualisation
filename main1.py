import numpy as np
from bokeh.io import output_notebook
from bokeh.io import show as bshow
from bokeh.plotting import figure
from bokeh.models import Diamond

import bokeh
bokeh.sampledata.download()


def show(p):
    """
    'Pay no attention to the man behind the curtan!'

    """
    output_notebook()
    bshow(p)


x, y = [1, 2, 3, 4, 5], [6, 7, 2, 4, 5]

# My First Scatter Plot:

# create a new plot with default tools, using figure
p = figure(height=400)

# add a circle render with x and y coordinates
p.circle(x, y, radius=0.4)


# radius=0.4   - diameter to graph scale
# size=45
# size=[10, 20, 40, 80] # 'vectorize' sizes:

show(p)  # show the result

p = figure(plot_height=200, sizing_mode="scale_width")

p.title.text = 'First Plot'
p.background_fill_color = 'beige'
p.outline_line_width = 7
p.outline_line_alpha = 0.3
p.outline_line_color = "navy"

r = p.square(x, y, color="firebrick")

r.glyph.size = 50
r.glyph.fill_alpha = 0.2
r.glyph.line_color = "firebrick"
r.glyph.line_dash = [5, 1]
r.glyph.line_width = 2

show(p)  # show the results

# Bokeh Color Palettes: https://bokeh.pydata.org/en/latest/docs/reference/palettes.html
