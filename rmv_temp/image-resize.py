from PIL import Image
import sys
import os

# Filepaths to all of the file folders
full_res_filepath = './../full-res-images/'
reduced_filepath = './src/'
watermark_filepath = './icons/'

file_names =  [f for f in os.listdir(full_res_filepath) if f.lower().endswith('.jpg')]
existing_file_names = [f for f in os.listdir(reduced_filepath) if f.lower().endswith('.jpg')]

files_to_convert = [f for f in file_names if f not in existing_file_names]

# Uncomment to print all file names and resolutions
# for f in file_names:
#     foo = Image.open(full_res_filepath + f)
#     print(f, foo.size)

# print("CONVERTING " + str(len(files_to_convert)) + " IMAGES:")

watermark = Image.open(watermark_filepath + 'Watermark-Full-Small.png')
watermark_width, watermark_height = watermark.size


# Lowers resolution of files and adds a watermark to the bottom right corner of each one
for f in files_to_convert:
    foo = Image.open(full_res_filepath + f)
    print('\tCONVERTING ' + f, end='\r')

    if (foo.size[0] < 1024 or foo.size[1] < 1024):
        foo.save(reduced_filepath + f, quality=95)
        foo.close()
        continue
    
    scale_factor = foo.size[0] / 1024
    new_width = 1024
    new_height = round(foo.size[1] / scale_factor)

    frame = Image.new(mode='RGBA', size=(new_width,new_height), color=0)
    foo = foo.resize((new_width, new_height), Image.ANTIALIAS)
    foo.putalpha(255)

    watermark_position = (new_width - watermark_width - 16, new_height - watermark_height - 16)
    frame.paste(im=foo)
    frame.paste(watermark, watermark_position, watermark)
    frame = frame.convert('RGB')
    frame.save(reduced_filepath + f, quality=95, optimize=True)

    print('\tCONVERTED ' + f + "!")
    foo.close()

print("DONE!")