from pdf2image import convert_from_path
import os


for subdir, dirs, files in os.walk('./'):
    for file in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file
        if filepath.endswith(".pdf"):
            try:
                os.mkdir(str(subdir).split('\\')[1]+'_images')
                location = str(subdir).split('\\')[1]+'_images'
            except FileExistsError as e :
                pass
            # print(filepath, str(file).split('.')[0], str(subdir).split('\\')[1])
            pages = None
            pages = convert_from_path(filepath, 500)
            name = str(file).split('.')[0]
            for page in pages:
                page.save('./'+location+'/'+name+'.jpg', 'JPEG')
            