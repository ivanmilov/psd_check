from psd_tools import PSDImage
import sys
import os.path
import string

transtab = str.maketrans('', '', string.ascii_letters + string.digits + '_')


def check(name):
    res = name.translate(transtab)
    # if len(res) > 0:
    #     print('->', name, ': ', res)
    return len(res) > 0, res


def check_layer(layer):
    err = False
    layers = []
    if layer.is_group():
        # print('group', layer.name)
        for l in layer:
            e, l = check_layer(l)
            err = err or l
            layers.extend(l)
    check_err, res = check(layer.name)
    if check_err:
        err = True
        layers.append([layer.name, res])
        # print('\tNOK layer: ', layer.name)

    return err, layers


if __name__ == '__main__':
    for file in sys.argv[1:]:
        psd = PSDImage.open(file)
        base = os.path.splitext(file)[0]

        errs = []

        for layer in psd:
            e, l = check_layer(layer)
            errs.extend(l)
        if len(errs) > 0:
            print("file:", file, ":")
            for t in errs:
                print("\tlayer[{}] -> [{}]".format(t[0], t[1]))
        else:
            print("file:", file, " OK")
