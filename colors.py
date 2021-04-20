import random

colors_dictionary = {
    "#02343F": "#F0EDCC",
    "#331B3F": "#ACC7B4",
    "#0A174E": "#F5D042",
    "#07553B": "#CED46A",
    "#50586C": "#DCE2F0",
    "#815854": "#F9EBDE",
    "#A4193D": "#FFDFB9",
    "#1AAFBC": "#80634C",
    "#FFDFDE": "#6A7BA2",
    "#3B1877": "#DA5A2A",
    "#5F4B8B": "#E69A8D",
    "#000000": "#FFFFFF",
    "#00203F": "#ADEFD1",
    "#606060": "#D6ED17",
    "#2C5F2D": "#97BC62",
    "#00539C": "#EEA47F",
    "#101820": "#FEE715",
    "#CBCE91": "#d3687f",
    "#B1624E": "#5CC8D7",
    "#7b9acc": "#FCF6F5",
    "#101820": "#F2AA4C",
    "#A07855": "#D4B996",
    "#195190": "#A2A2A1",
    "#F95700": "#FFFFFF",
    "#DF6589": "#3C1053",
    "#1C1C1B": "#CE4A7E",
    "#BD7F37": "#A13941",
    "#F96167": "#FCE77D",
    "#DF678C": "#3D155F",
    "#EC4D36": "#1D1B1B",
    "#4A171E": "#E2B143",
    "#D2302C": "#F7F7F9",
    "#FFE8F5": "#9000FF",
    "#99F443": "#EC449B",
}


def random_color():
    color = random.choice(list(colors_dictionary))
    return color


random_color()