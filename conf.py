# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Imagination Server キャストマニュアル'
copyright = '2022, Imagination Server'
author = 'Imagination Server'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinxcontrib.seqdiag',
    'sphinxcontrib.actdiag',
    'sphinxcontrib.nwdiag',
    'sphinxcontrib.blockdiag',
    'sphinx_copybutton'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'ja'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
# html_theme = 'default'
# html_theme = 'sphinxdoc'
# html_theme = 'scrolls'
# html_theme = 'agogo'
# html_theme = 'nature'
# html_theme = 'pyramid'
# html_theme = 'haiku'
# html_theme = 'traditional'
html_theme = 'bizstyle'


html_static_path = ['_static']

blockdiag_html_image_format \
    = seqdiag_html_image_format \
    = actdiag_html_image_format \
    = nwdiag_html_image_format \
    = rackiag_html_image_format \
    = packetdiag_html_image_format \
    = 'SVG'

blockdiag_fontpath \
    = seqdiag_fontpath \
    = nwdiag_fontpath = [
        '/usr/share/fonts/opentype/ipafont-mincho/ipam.ttf',
        '/usr/share/fonts/opentype/ipafont-gothic/ipagp.ttf',
        '/usr/share/fonts/opentype/ipafont-mincho/ipamp.ttf',
        '/usr/share/fonts/opentype/ipafont-gothic/ipag.ttf',
        '/usr/share/fonts/truetype/fonts-japanese-mincho.ttf',
        '/usr/share/fonts/truetype/fonts-japanese-gothic.ttf',
        '/usr/share/fonts/opentype/ipaexfont-gothic/ipaexg.ttf',
        '/usr/share/fonts/opentype/ipafont-gothic/ipagp.ttf',
        '/usr/share/fonts/truetype/vlgothic/VL-Gothic-Regular.ttf'
        '/system/Library/Fonts/ヒラギノ丸ゴ ProN W4.ttc',  # For Mac
        '/usr/share/fonts/ipa-gothic/ipag.ttf',  # IPA Gothic on Redhat
        '/usr/share/fonts/opentype/ipafont-gothic/ipag.ttf',  # IPA Gothic on Debian
    ]
