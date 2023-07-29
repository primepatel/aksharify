import IPython.display as ipd
import ipywidgets as widgets
from aksharify import AksharArt
from .distributions import Exponential, Normal

def interact_normal(img, distribution, colored=True):
    m = widgets.FloatSlider(
            min=distribution.a_mean,
            max=distribution.b_mean,
            step=distribution.s_mean,
            value=(distribution.a_mean + distribution.b_mean)/2,
            description='mean:'
        )
    v = widgets.FloatSlider(
            min=distribution.a_var,
            max=distribution.b_var,
            step=distribution.s_var,
            value=(distribution.a_var + distribution.b_var)/2,
            description='var:'
        )
    output = widgets.Output()
    def handle_slider_change(change):
        with output:
            output.clear_output()
            norm = Normal(chars=distribution.chars, mean=m.value, var=v.value)
            art = AksharArt(img, norm)
            art.aksharify()
            art.show(colored)
    m.observe(handle_slider_change, 'value')
    v.observe(handle_slider_change, 'value')
    ipd.display(m, v, output)


def interact_exponential(img, distribution, colored=True):
    p = widgets.FloatSlider(
            min=distribution.a,
            max=distribution.b,
            step=distribution.s,
            value=(distribution.a + distribution.b)/2,
            description='power:'
        )
    output = widgets.Output()
    def handle_slider_change(change):
        with output:
            output.clear_output()
            expo = Exponential(chars=distribution.chars, power=p.value)
            art = AksharArt(img, expo)
            art.aksharify()
            art.show(colored)
    p.observe(handle_slider_change, 'value')
    ipd.display(p, output)