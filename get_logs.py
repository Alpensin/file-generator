import os, shutil
from datetime import datetime, timedelta

dirlist = os.walk(".")
export_dir = f'..\export{datetime.now().strftime("%Y%m%d%H%M%S")}'
if not os.path.exists(export_dir):
    os.mkdir(export_dir)
for f_object in dirlist:
    for log_file in f_object[2]:
        fulldir = os.path.join(f_object[0], log_file)
        if datetime.strptime("05.08.2017", "%d.%m.%Y") <= datetime.fromtimestamp(os.stat(fulldir).st_mtime) <=datetime.strptime("18.09.2017", "%d.%m.%Y"):
            n_dir = f_object[0].replace(".", export_dir, 1)
            print(n_dir)
            if not os.path.exists(n_dir):
                os.mkdir(n_dir)
            shutil.copy(fulldir, n_dir)

