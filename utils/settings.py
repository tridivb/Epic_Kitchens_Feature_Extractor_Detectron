import os

from utils import AttrDict

config = AttrDict()
user_home_dir = os.path.expanduser("~")

config.video_list = "./misc/vid_list.txt"
config.video_root = os.path.join(user_home_dir, "epic_kitchens/EPIC_KITCHENS_2018/videos")
config.weights = "./weights/ek18-2gpu-e2e-faster-rcnn-R-101-FPN_1x.pkl"
config.cfg_file = "./config/ek18-2gpu-e2e-faster-rcnn-R-101-FPN_1x.yaml"
config.sample_fps = 60
config.top_predictions = 100
config.out_path = os.path.join(user_home_dir, "detections")

try:
    from utils.local_settings import *
except Exception:
    pass
