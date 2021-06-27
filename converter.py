from PIL import Image
import os
import sys, getopt

def main(argv):
    source_path = './data'
    result_path = './'
    file_name = 'doc.pdf'
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
        elif opt in ("-i", "--ifile") and file_name == 'doc.pdf':
            source_path = arg
            file_name = source_path.split('/')[-1] + '.pdf'
        elif opt in ("-o", "--ofile"):
            result_path = arg
        elif opt in ("-n", "--name"):
            file_name = arg

    files = os.listdir(source_path)
    files.sort()
    images = []
    for file in files:
        img = Image.open(r''+source_path+'/'+file)
        width, height = img.size
        if width > height:
            img = img.rotate(90, expand=True)
        img.thumbnail(size=(1000, 1000))
        rgb = img.convert('RGB')
        images.append(rgb)

    exists = os.path.exists(result_path)
    if not exists:
        os.makedirs(result_path)
    img = images.pop(0)
    img.save(r'' + result_path + "/" + file_name , save_all=True, append_images=images)
    print('Done!')


if __name__ == "__main__":
    args=[]
    try:
        args = sys.argv[1:]
    except Exception:
        print('without arguments')

    main(args)
