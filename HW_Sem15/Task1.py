from collections import namedtuple
import logging
import os

def dir_content(path):
    logging.basicConfig(filename='content.log.', filemode='w', encoding='utf-8', level=logging.INFO)
    logger = logging.getLogger(__name__)
    File = namedtuple('File', ['name', 'extension', 'is_dir', 'parent_dir'])
    for path, dirs, files in os.walk(path):
        parent = path.split('\\')[-2]
        for dir in dirs:
            name = dir
            ext = None
            is_dir = True
            temp = File(name, ext, is_dir, parent)
            logger.info(temp)
        for file in files:
            name = file.split('.')[0]
            if len(file.split('.')) > 1:
                ext = '.' + file.split('.')[1]
            else:
                ext = None
            is_dir = False
            temp = File(name, ext, is_dir, parent)
            logger.info(temp)

if __name__ == '__main__':
    dir_content('c:\\Users\\Вождь\\Pictures\\Screenshots\\Linux')