import os
from datetime import datetime, timedelta

from apscheduler.schedulers.background import BackgroundScheduler

from config.env_config import config
from utils.common import is_dir_exists


# =====================================
# 清理数据目录下昨日文件
# =====================================
def clean_tmp_file():
    yesterday = datetime.today().date() - timedelta(days=1)
    parent_path = config.DATA_PATH + os.sep + yesterday.strftime("%Y%m%d")
    print(f"获得的路径：", parent_path)
    if not is_dir_exists(parent_path):
        pass
    file_list = os.listdir(parent_path)
    for file in file_list:
        file_path = os.path.join(parent_path, file)
        if os.path.isfile(file_path):
            os.remove(file_path)


# 创建调度器
scheduler = BackgroundScheduler()

# # 添加任务，每5秒执行一次
scheduler.add_job(clean_tmp_file, 'cron',  hour=0, minute=10)
# scheduler.add_job(clean_tmp_file, 'interval', seconds=5)
