#!/usr/bin/python3

from psd_tools import PSDImage
import sys
import os.path
import string

transtab = str.maketrans('', '', string.ascii_letters + string.digits + '_')
filename = ''
logfile = ''
has_printed = False
log_reset = True


def print_out_and_file(s):
    print(s)

    global log_reset
    mode = 'a'
    if log_reset:
        mode = 'w'
        log_reset = False
    with open(logfile, mode) as f:
        print(s, file=f)


def check_and_rename(layer):
    name = layer.name.strip()
    res = name.translate(transtab)
    if len(res) > 0:
        for c in res:
            if(c.isspace()):
                name = name.replace(c, '_')
            else:
                name = name.replace(c, '')
    if layer.name != name:
        print_file_name()
        print_out_and_file(
            'rename [{}] -> [{}] ({})'.format(layer.name, name, res))
        layer.name = name


def check_same_name(layer, names):
    if not layer.is_group():
        if layer.name not in names:
            names[layer.name] = get_path(layer)
        else:
            print_file_name()

            new_name = layer.name
            i = 1
            while new_name in names:
                new_name = layer.name + '_' + f'{i}'
                i = i+1
            print_out_and_file(
                'rename [{}] -> [{}] (same name)'.format(get_path(layer), new_name))
            layer.name = new_name
            names[layer.name] = get_path(layer)


def get_path(layer):
    if layer.parent:
        return get_path(layer.parent) + '/' + layer.name

    return layer.name


def print_file_name():
    global has_printed
    if not has_printed:
        print(filename, ':')
        has_printed = True


if __name__ == '__main__':
    for file in sys.argv[1:]:
        filename = file
        psd = PSDImage.open(file)
        base = os.path.splitext(file)[0]
        logfile = base + '.log'
        log_reset = True
        has_printed = False

        names = {}

        # print(psd[0].name, psd[0][0].name)
        # print(psd[1].name, psd[1][0].name)

        # psd[0][0].name = 'huy# ,p`esda'

        # print(psd[0].name, psd[0][0].name)
        # print(psd[1].name, psd[1][0].name)

        # psd.save('out.psd')
        # break
        for l in psd.descendants():
            check_and_rename(l)
            check_same_name(l, names)

        # psd.save('out2.psd')
