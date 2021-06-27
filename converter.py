from PIL import Image
import os
import sys, getopt

source_path = './data'
result_path = './doc.pdf'


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print
        'test.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print
            'converter.py -i <input> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            source_path = arg
        elif opt in ("-o", "--ofile"):
            result_path = arg

    files = os.listdir(source_path)
    files.sort()
    images = []
    for file in files:
        img = Image.open(r''+source_path+'/'+file)
        width, height = img.size
        if width > height:
            img = img.rotate(90)
        rgb = img.convert('RGB')
        images.append(rgb)

    exists = os.path.exists(result_path)
    if not exists:
        os.makedirs(result_path)
    img = images.pop(0)
    img.save(r'' + result_path , save_all=True, append_images=images)
    print('Done!')


if __name__ == "__main__":
   main(sys.argv[1:])