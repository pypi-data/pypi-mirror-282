import os
import random
import json
import copy
from langchain.document_loaders import PyPDFLoader
from langchain_core.prompts import PromptTemplate
from bisheng_langchain.document_loaders import ElemUnstructuredLoader
from bisheng_ragas.trainset import TrainsetGenerator

os.environ["OPENAI_API_KEY"] = "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"
os.environ["OPENAI_PROXY"] = "http://118.195.232.223:39995"


prompt_template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.

{context}

Question: {question}
Helpful Answer:"""
PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
)


def generate_qa():
    loader = PyPDFLoader('达梦数据库招股说明书.pdf')
    documents = loader.load()
    print('documents:', len(documents))

    trainsetgenerator = TrainsetGenerator.from_default(openai_generator_llm='gpt-4-1106-preview')
    train_size = 500
    trainset = trainsetgenerator.generate(documents, train_size=train_size)

    df = trainset.to_pandas()
    df.to_excel("trainset_gen.xlsx")


def format_qa():
    import pandas as pd
    df = pd.read_excel("trainset_gen.xlsx")
    df = df[['question', 'ground_truth_context', 'ground_truth']]
    all_questions_info = list()
    # 遍历每一行
    for index, row in df.iterrows():
        # 遍历每一列
        question_info = dict()
        for column in df.columns:
            value = row[column]
            question_info[column] = value
            # print(f"Row {index}, Column {column} has value {value}")
        all_questions_info.append(question_info)
    
    random.shuffle(all_questions_info)
    train_samples = []
    test_samples = []
    for i, question_info in enumerate(all_questions_info):
        question = question_info['question']
        ground_truth_context = eval(question_info['ground_truth_context'])[0]
        ground_truth = eval(question_info['ground_truth'])[0]
        prompt = PROMPT.format(context=ground_truth_context, question=question)
        each_sample = {'instruction': '', 
                        'input': prompt, 
                        'output': ground_truth,
                        'history': []}

        if i < 0.8 * len(all_questions_info):
            train_samples.append(each_sample)
        else:
            test_samples.append(each_sample)
    
    random.shuffle(train_samples)
    random.shuffle(test_samples)
    print(f'train_samples: {len(train_samples)} test_samples: {len(test_samples)}')
    with open('train_samples.json', 'w') as f:
        json.dump(train_samples, f, indent=2, ensure_ascii=False)
    with open('test_samples.json', 'w') as f:
        json.dump(test_samples, f, indent=2, ensure_ascii=False)


def format_qa_v2():
    random.seed(123)
    with open('train_samples.json', 'r') as f:
        train_samples = json.load(f)
    
    with open('test_samples.json', 'r') as f:
        test_samples = json.load(f)

    train_contexts = []
    for sample in train_samples:
        input = sample['input']
        context = input.split('make up an answer.\n\n')[1].split('\n\nQuestion:')[0]
        train_contexts.append(context)
    
    test_contexts = []
    for sample in test_samples:
        input = sample['input']
        context = input.split('make up an answer.\n\n')[1].split('\n\nQuestion:')[0]
        test_contexts.append(context)
    
    all_train_samples = []
    for sample in train_samples:
        input = sample['input']
        context = input.split('make up an answer.\n\n')[1].split('\n\nQuestion:')[0]
        question = input.split('\n\nQuestion: ')[1].split('\nHelpful Answer:')[0]
        num = 0
        while num < 5:
            sample_copy = copy.deepcopy(sample)
            random_number = random.randint(3, 7)
            random_context = random.sample(train_contexts, random_number)
            if context in random_context:
                random_context.remove(context)
            # 将当前context随机插入到其他context中
            insert_position = random.randint(0, len(random_context))
            random_context.insert(insert_position, context)

            random_context = '\n\n'.join(random_context)
            prompt = PROMPT.format(context=random_context, question=question)
            sample_copy['input'] = prompt
            all_train_samples.append(sample_copy)
            num += 1

    for sample in test_samples:
        input = sample['input']
        context = input.split('make up an answer.\n\n')[1].split('\n\nQuestion:')[0]
        question = input.split('\n\nQuestion: ')[1].split('\nHelpful Answer:')[0]
        random_number = random.randint(3, 7)
        random_context = random.sample(test_contexts, random_number)
        if context in random_context:
            random_context.remove(context)
        insert_position = random.randint(0, len(random_context))
        random_context.insert(insert_position, context)

        random_context = '\n\n'.join(random_context)
        prompt = PROMPT.format(context=random_context, question=question)
        sample['input'] = prompt

    print(f'train_samples: {len(all_train_samples)} test_samples: {len(test_samples)}')
    with open('train_samples_ganrao_5.json', 'w') as f:
        json.dump(all_train_samples, f, indent=2, ensure_ascii=False)
    with open('test_samples_ganrao.json', 'w') as f:
        json.dump(test_samples, f, indent=2, ensure_ascii=False)

# generate_qa()
# format_qa()
format_qa_v2()