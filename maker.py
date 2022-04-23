import subprocess
import sys


def recovery(name):
    with open('makefile', 'r') as f:
        old_data = f.read()

    new_data = old_data.replace(name, 'filename')

    with open('makefile', 'w') as f:
        f.write(new_data)


def changer(name):
    with open('makefile', 'r') as f:
        old_data = f.read()

    new_data = old_data.replace('filename', name)

    with open('makefile', 'w') as f:
        f.write(new_data)


def make_start():
    cmd = f'make'
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    result = p.communicate()[0].decode("utf-8")
    print(result)
    return result


def run():
    my_name = sys.argv[1]
    changer(my_name)
    make_start()
    recovery(my_name)


if __name__ == "__main__":
    run()
