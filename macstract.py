# shebang goes here

import argparse, shutil

parser = argparse.ArgumentParser(description='TODO')
parser.add_argument('destination', help='Destination to copy files')
parser.add_argument('-f',action='count',help='Force script to copy all files regardless of size')
args = parser.parse_args()

def copy_verbose(source_path, dest_path):
    try:
        print('Copying {}...'.format(source_path))
        shutil.copy(source_path, dest_path)
    except:
        print('Error copying {}')

if __name__ == "__main__":
    dest_path = args.destination

    print("End")
