from PIL import Image
import struct
import os

source_path = "data/source"
result_path = "data/result"

def cloneWithColor(color):
    files = os.listdir(source_path)

    for file in files:
        image = Image.open(source_path+'/'+file)
        image = image.convert('RGBA')

        color_tuple = struct.unpack('BBBB',struct.pack('I',int("0x"+color[1:], 16)))[:3]

        for i in range(image.size[0]):
            for j in range(image.size[1]):
                a = image.getpixel((i,j))[3]

                if a != 0 and image.getpixel((i,j))[0] != 0 and image.getpixel((i,j))[1] != 0 and image.getpixel((i,j))[2] != 0:
                    image.putpixel((i, j), ((color_tuple[0], color_tuple[1], color_tuple[2], a)))

        print(result_path+"/"+file[0: -4]+color+file[-4:])
        image.save(result_path+"/"+file[0: -4]+color+file[-4:])

if __name__ == '__main__':
    #run()
    cloneWithColor('#0fa1a3')
    #cloneWithColor('#a400ee')
    #cloneWithColor('#1a5670')
