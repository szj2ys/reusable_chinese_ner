# *_*coding:utf-8 *_*
from os.path import dirname, abspath, join

# 获取项目根目录
ROOT = dirname(dirname(abspath(__file__)))

# 数据文件存放路径
DATASETS = join(ROOT, "datasets")

VOCABS = join(DATASETS, "vocabs")

OUTPUT = join(ROOT, "output")

CHECKPOINT = join(ROOT, "checkpoints", "bilstm-crf")

# log文件路径
LOGS = join(ROOT, "logs")
