import os
from bisheng_ragas import evaluate
from bisheng_ragas.metrics import AnswerRecallBisheng
from datasets import Dataset
import openpyxl
import pandas as pd
import json
from bisheng_ragas.metrics.base import EvaluationMode, MetricWithLLM
os.environ["OPENAI_API_KEY"] = "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"
os.environ["OPENAI_PROXY"] = "http://118.195.232.223:39995"

def read_excel_columns(filename, columns):
    wb = openpyxl.load_workbook(filename)
    ws = wb.active

    data = []
    for row in ws.iter_rows(values_only=True):
        selected_data = [row[col - 1] for col in columns]
        data.append(selected_data)

    return data


# 提取的文件名称
q_a_k = 'gpt4de2.xlsx'
columns_to_read = [1, 8, 10, 15]
# columns_to_read = [1, 8, 10]
result = read_excel_columns(q_a_k, columns_to_read)
questions = []
ground_truths = []
answers = []
all_contexts = []
splitpoint = []
for row in result[1:]:
    questions.append(row[0])
    answers.append(row[1])
    ground_truths.append([row[2]])
    all_contexts.append([row[2]])
    splitpoint.append(row[3])

# for row in result[1:]:
#     questions.append(row[0])
#     answers.append(row[1])
#     ground_truths.append([row[2]])
#     all_contexts.append([row[2]])
        
df = pd.read_excel(q_a_k)
answer_recall_bisheng_score = AnswerRecallBisheng(whether_gtsplit=True)

data = {
    "question": questions,
    "answer": answers,
    "contexts": all_contexts,
    "ground_truths": ground_truths,
    "gt_split_point": splitpoint
}
# data = {
#     "question": questions,
#     "answer": answers,
#     "contexts": all_contexts,
#     "ground_truths": ground_truths
# }
dataset = Dataset.from_dict(data)
result = evaluate(
    dataset = dataset, 
    metrics=[
        answer_recall_bisheng_score
    ],
)
print(result)
df = result.to_pandas()
df.to_excel("test_gptchaifen4.xlsx")




