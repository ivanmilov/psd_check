from psd_tools import PSDImage
import sys
import os.path
import string

transtab = str.maketrans('', '', string.ascii_letters + string.digits + '_')


def check(name):
    res = name.translate(transtab)
    if len(res) > 0:
        print('-> ', name, ': ', res)


def check_layer(layer):
    if layer.is_group():
        print('group', layer.name)
        for l in layer:
            check_layer(l)
    check(layer.name)
    print('\tlayer: ', layer.name)


if __name__ == '__main__':
    for file in sys.argv[1:]:
        psd = PSDImage.open(file)
        base = os.path.splitext(file)[0]

        for layer in psd:
            check_layer(layer)
