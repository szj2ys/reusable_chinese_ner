# *_*coding:utf-8 *_*

try:
    from .dirs import *
except:
    from configs.dirs import *

# 训练集
TRAIN_FILE = join(DATASETS, "train.csv")
# 测试集
DEV_FILE = join(DATASETS, "dev.csv")

# 停用词路径
STOPWORDS = join(DATASETS, "stopwords.txt")
# print(FILE_STOP_WORDS)
# 自定义切词表
USER_DICT = join(DATASETS, "userdict.txt")
