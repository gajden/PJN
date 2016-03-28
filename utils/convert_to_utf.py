import subprocess

from os.path import join

from os import listdir

if __name__ == '__main__':
    src_dir = '../data/corpus'
    dump_dir = '../data/utf'

    paths = listdir(src_dir)

    for p in paths:
        print('File: %s' % p)
        command = "iconv -t UTF-8 %s > %s" % (join(src_dir, p),
                                                            join(dump_dir, p))

        print(command)
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output = process.communicate()[0]
