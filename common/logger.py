import logging
import os
from logging import handlers
from config.ProjectConfig import VBConfig

def logger():
    os.makedirs("{}logs".format(VBConfig.TEST_DIR), exist_ok=True)
    log = logging.getLogger("{}logs/et.log".format(VBConfig.TEST_DIR))
    format_str = logging.Formatter('%(asctime)s [%(module)s] %(levelname)s [%(lineno)d] %(message)s', '%Y-%m-%d %H:%M:%S')
    # 按天录入日志，最多保存7天的日志
    handler = handlers.TimedRotatingFileHandler(filename=("{}logs/et.log".format(VBConfig.TEST_DIR)), when='D', backupCount=7, encoding='utf-8')
    log.addHandler(handler)
    log.setLevel(logging.INFO)
    handler.setFormatter(format_str)
    return log

write_log = logger()