import pandas as pd
from loguru import logger

benchmark_gpt4 = '../data/gpt-4.xlsx'
benchmark_gpt4_sheet1 = pd.read_excel(benchmark_gpt4, sheet_name='Sheet1')
benchmark_gpt4_sheet2 = pd.read_excel(benchmark_gpt4, sheet_name='Sheet2')

for idx, row_sheet2 in benchmark_gpt4_sheet2.iterrows():
    question = row_sheet2['问题']
    query_type = benchmark_gpt4_sheet1.loc[benchmark_gpt4_sheet1['问题'] == question, 'query_type']
    row_sheet2.loc['query_type'] = query_type

# 对benchmark_gpt4_sheet2进行统计分析
# 1. 问题总数
total_questions = benchmark_gpt4_sheet2.shape[0]

# 2. 问题类型分布
query_type_distribution = benchmark_gpt4_sheet2.groupby('query_type').count()['问题']
# print(query_type_distribution)
query_type_distribution = query_type_distribution / total_questions
# print(query_type_distribution)

# 3. 错误类型分布
# 3.1 检索召回阶段错误类型分布
logger.info(benchmark_gpt4_sheet2.groupby('检索召回').count()['问题'].to_markdown())
# 当出现检索召回错误时，答案生成错误的分布
logger.info(benchmark_gpt4_sheet2.groupby(['检索召回', '答案生成']).count()['问题'].to_string())
