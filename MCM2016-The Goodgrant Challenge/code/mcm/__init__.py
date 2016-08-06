# -*- coding:utf-8 -*-
from __future__ import unicode_literals, print_function
import os
import logging

data_dir = r'D:\Documents\工作存档\数学建模\2016美赛\ProblemCDATA'

work_dir = os.path.realpath(os.curdir)
report_dir = os.path.join(work_dir, 'report')
mat_dir = os.path.join(work_dir, 'mat')

logger = logging.Logger('MCM_ICM', logging.INFO)

logger.addHandler(logging.StreamHandler())

log_file_handle = logging.FileHandler('MCM_ICM.log')
log_file_handle.setLevel(logging.WARNING)
log_file_handle.setFormatter(logging.Formatter('%(levelname)s: %(message)s -%(filename)s %(lineno)d'))

logger.addHandler(log_file_handle)

