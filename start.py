#!/usr/bin/env python3
import os
import subprocess
import time
import yaml


# Load in a yaml config file
def load_config(config_file):
    with open(config_file,'r') as stream:
        cfg = yaml.safe_load(stream).get('bdfrh')
    return cfg

config = load_config("config.yml")
bdfr_cfg = config['bdfr']
bdfrhtml_cfg = config['bdfrhtml']


idList = os.path.join(bdfr_cfg['output_folder'], "idList.txt")


while True:
    if runBdfr:
        subprocess.call(["python3.9", "-m", "bdfr", "archive", "--user", "me", "--saved", "-L", bdfr_cfg['limit'],
                         "--authenticate", bdfrhtml_cfg['input_folder']])
        subprocess.call(["python3.9", "-m", "bdfr", "download", "--user", "me", "--saved", "-L", bdfr_cfg['limit'],
                         "--exclude-id-file", idList, "--authenticate", "--file-scheme", "{POSTID}", inFolder])
    subprocess.call(["python3.9", "-m", "bdfrtohtml", "--input", inFolder, "--output", outFolder, "--recover_comments",
                     recover_comments, "--archive_context", archive_context, "--delete_input", delete])
    time.sleep(int(freq)*60)
