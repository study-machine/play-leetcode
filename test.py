# coding=utf8
import json
import re


def read_log(file_path):
    paper_num = 0
    paper_list = []
    data = None
    with open(file_path, 'r') as f:
        for line in f.readlines():
            if line[:5] == 'data:':
                # 发现新的data:开头，将之前的放进列表
                if data:
                    paper_list.append(data)
                paper_num += 1
                data = {'paper_num': paper_num,
                        'paper_data': json.loads(line[5:])}
            elif line[:10] == 'SectionID:':
                m = re.match('SectionID:(\d+)', line)
                # SectionID 转 int
                data['SectionID'] = int(m.group(1))
                m = re.match('.*Difficult:(\d+\.\d+)-(\d+\.\d+)', line)
                # Difficult两个浮点数放到tuple
                data['Difficult'] = (float(m.group(1)), float(m.group(2)))
                m = re.match('.*QuestionType:(\[.*?\])', line)
                data['QuestionType'] = json.loads(m.group(1))
                m = re.match('.*QuestionKnow:(\[.*\])', line)  # 贪婪最后一个]号
                data['QuestionKnow'] = json.loads(m.group(1))
    return paper_list


