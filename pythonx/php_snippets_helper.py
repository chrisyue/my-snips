import os
import os.path
import re
import json

def namespace(path):
    m = re.search(r'(?<=/)[A-Z]\w+(/[A-Z]\w+)*(?=/[^/]+$)', path)

    ns = m.group().replace('/', '\\') if m else ''
    if not os.path.isfile('composer.json'):
        return ns

    with open('composer.json') as json_file:
        data = json.load(json_file)
        if not ('autoload' in data) or not ('psr-4' in data['autoload']):
            return ns

        psr4 = data['autoload']['psr-4']
        for key in psr4:
            if psr4[key] in path:
                return (key + ns).strip('\\')

def fqn(path):
    m = re.search(r'(?<=/)[A-Z]\w+(/[A-Z]\w+)+(?=\.php)', path)
    if m:
        return m.group().replace('/', '\\')

# Symfony

def controller_slug(snip):
    name = snip.basename.rsplit('Controller', 1)[0]
    name = re.sub(r'[A-Z]', '-\g<0>', name)
    name = name.strip('-')

    return '/' + name.lower()

def controller_route_prefix(path):
    parts = fqn(path).split('Controller')

    return (parts[0].replace('Bundle\\', '') + parts[1]).replace('\\', '_').lower()

def controller_tpl_prefix(path):
    return fqn(path).split('Controller')[1].strip('\\').replace('\\', '/').lower()
