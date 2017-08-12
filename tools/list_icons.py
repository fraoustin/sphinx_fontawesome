#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    tools for generate list of icons from source of Font-Awesome
"""

import urllib
import yaml

URL_ICONS = "https://raw.githubusercontent.com/FortAwesome/Font-Awesome/master/src/icons.yml" 

icons =  yaml.load(urllib.urlopen(URL_ICONS).read())['icons']
with open('../sphinx_fontawesome/constant.py', 'w') as f:
    f.write("""#!/usr/bin/env python
# -*- coding: utf-8 -*-
\"\"\"
    list of icons Font-Awesome
\"\"\"

icons = [
""")
    for icon in icons:
        f.write("\t'%s',\n" % icon['id'])
        if 'aliases' in icon:
            for alias in icon['aliases']:
                f.write("\t'%s',\n" % alias)
    f.write("""]
# generate by tools/list_icons""")
