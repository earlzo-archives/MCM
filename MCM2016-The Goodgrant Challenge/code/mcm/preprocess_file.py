# -*- coding:utf-8 -*-
from __future__ import unicode_literals, print_function
import sys

reload(sys)
sys.setdefaultencoding('utf8')

import os
import pandas as pd
from pprint import pprint
from mcm import data_dir, logger

# 候选学校名单
# 全部为 IPED 记录的所机构, 共 2977 所
candidate_schools = pd.read_excel(
    os.path.join(data_dir, r'Problem C - IPEDS UID for Potential Candidate Schools.xlsx'),
    index_col=0,
)

print(candidate_schools.describe())

all_data_dir = os.path.join(data_dir, 'Web/IPEDS_ALL')

file_names = os.listdir(all_data_dir)
data_file_names = filter(lambda v: v.endswith('.csv'), file_names)

valid_files = []
loss_files = []
error_files = []
diff_result_dir = os.path.join(all_data_dir, 'diff_result')
for f in data_file_names:
    try:
        df = pd.read_csv(os.path.join(all_data_dir, f), index_col=0, usecols=[0])
    except pd.parser.CParserError as e:
        error_files.append(f)
        logger.error('{} 数据读取时发生错误'.format(f))
    diff = candidate_schools.index.difference(df.index)
    if diff.size > 0:
        loss = '_'.join([unicode(diff.size), f])
        loss_files.append(loss)
        candidate_schools.ix[diff].to_excel(
            os.path.join(diff_result_dir, '{}_diff.xls'.format(loss.rstrip('.csv'))))
        logger.warning('{} 有 {} 所学校缺少数据'.format(f, diff.size))
    else:
        valid_files.append(f)
        logger.info('{} 包含了所有需要的数据'.format(f))

valid_count = len(valid_files)
loss_count = len(loss_files)
error_count = len(error_files)
msg = '共有 {} 个文件数据不够, {} 个文件解析错误, {} 个文件完整, 共 {} 个文件'.format(
    loss_count,
    error_count,
    valid_count,
    loss_count + error_count + valid_count
)

with open(os.path.join(diff_result_dir, 'IPED_data_check_result.txt'), 'wb') as fp:
    text = '\n'.join([msg,
                      '-----valid_files-----', '\n'.join(valid_files), '\n',
                      '-----error_files-----', '\n'.join(error_files), '\n',
                      '-----loss_files-----', '\n'.join(loss_files)])
    fp.write(text)

logger.warning(msg)
