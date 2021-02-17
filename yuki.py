import argparse
import codecs
import cv2
import hashlib
import os
import shutil
import yaml

     
def main(args):
    # Load configuration file
    config_file = os.path.join('static', 'profile.yml')
    try:
        with codecs.open(config_file, 'r', 'utf-8') as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
    except FileNotFoundError:
        config = list()

    # Save image to target floder
    original_floder = os.path.join('static', 'original')
    thumbnail_floder = os.path.join('static', 'thumbnail')
    os.makedirs(original_floder, exist_ok=True)
    os.makedirs(thumbnail_floder, exist_ok=True)

    ori_im = cv2.imread(args.image)
    ori_height, ori_width = ori_im.shape[:2]
    ori_sha256 = hashlib.sha256(ori_im.tobytes()).hexdigest()
    ori_name = ori_sha256 + '.jpg'
    cv2.imwrite(os.path.join(original_floder, ori_name), ori_im)

    thu_height, thu_width = int(640 * ori_height / ori_width), 640
    thu_im = cv2.resize(ori_im, (thu_width, thu_height)) 
    thu_sha256 = hashlib.sha256(thu_im.tobytes()).hexdigest()
    thu_name = thu_sha256 + '.jpg'
    cv2.imwrite(os.path.join(thumbnail_floder, thu_name), thu_im)
    
    # Update configuration file
    tags = list(set(args.tags))
    score = args.score
    image_info = {
        'ori_name': ori_name,
        'ori_url': 'https://kanda-mashiro.github.io/Yuki/static/original/' + ori_name,
        'ori_width': ori_width,
        'ori_height': ori_height,
        'thu_name': thu_name,
        'thu_url': 'https://kanda-mashiro.github.io/Yuki/static/thumbnail/' + thu_name,
        'thu_width': thu_width,
        'thu_height': thu_height,
        'tags': tags,
        'score': score 
    }
    position = None
    for index in range(len(config)): 
        if config[index]['ori_name'] == ori_name:
            position = index 
            break
    if position is not None:
        config[position] = image_info 
    else:
        config.append(image_info)

    # Save configuration file
    with codecs.open(config_file, 'w', 'utf-8') as f:
        yaml.dump(config, f, sort_keys=False, allow_unicode=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--image')
    parser.add_argument('--tags', nargs='*', default=['Unclassified'])
    parser.add_argument('--score', type=int, default=0)
    main(parser.parse_args())
