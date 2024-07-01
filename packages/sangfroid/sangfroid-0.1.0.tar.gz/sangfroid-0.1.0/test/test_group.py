import sangfroid
from test import *

def test_canvas_children():
    sif = get_animation('circles.sif')

    EXPECTED = [
            "[🔵circle 'Red circle']",
            "[📂group 'More circles']",
            "[📂group \"Well, it's round\"]",
            "[📂group 'Blurry circle']",
            "[📂group 'Background circle']",
            ]

    found = [str(layer) for layer in sif.children]

    assert found==EXPECTED

def test_canvas_descendants():
    sif = get_animation('circles.sif')

    EXPECTED = [
            "[🔵circle 'Red circle']",
            "[📂group 'More circles']",
            "[-🔵circle 'Yellow circle']",
            "[-📂group 'All right, one more circle']",
            "[-🔵circle 'Orange circle']",
            "[📂group \"Well, it's round\"]",
            "[-🔵circle 'Purple circle']",
            "[📂group 'Blurry circle']",
            "[-🟠blur 'Blur']",
            "[-🔵circle 'Blue circle']",
            "[📂group 'Background circle']",
            "[-🔵circle 'Maybe white circle']",
            "[-🔵circle 'Black circle']",
            ]

    found = [str(layer) for layer in sif.descendants]

    assert found==EXPECTED
