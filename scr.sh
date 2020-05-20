#!/bin/sh
date
cd /home/zhi/GitHub/CAWS_status
python hf.py && git add . && git commit -m "Updated: `date +'%Y-%m-%d %H:%M:%S'`" && git push
echo '---------------------'

