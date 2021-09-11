import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_element_byid(pid):
    l = get_all_user_story()
    for i in l:
        if i['id'] == str(pid):
            return i
    return {}


def get_all_user_story():
    story_data_list = []
    story_data = open("data.csv", encoding="windows-1250")
    reader = csv.DictReader(story_data)
    for row in reader:
        story_data_list.append(row)
    story_data.close()
    return story_data_list


def write_all_user_story(user_story_list):
    print(user_story_list)
    with open("data.csv", "w", newline="") as story_data:
        fieldnames = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
        writer = csv.DictWriter(story_data, fieldnames=fieldnames)
        writer.writeheader()
        for d in user_story_list:
            writer.writerow(d)


def generate_id():
    list_of_ids = []
    data = get_all_user_story()
    for i in data:
        list_of_ids.append(int(i['id']))
    if not list_of_ids:
        highest_id = 0
    elif list_of_ids:
        highest_id = max(list_of_ids)
    highest_id += 1

    return highest_id


def update_data(dict):
    data = get_all_user_story()
    print(dict)
    fh = open("data.csv", "w")
    fh.write("id,title,user_story,acceptance_criteria,business_value,estimation,status\n")
    for i in data:
        if i['id']:
            if i['id'] != dict['id']:
                fh.write(i['id'] + ',' + i['title'] + ',' + i['user_story'] + ',' + i['acceptance_criteria'] + ',' + i[
                    'business_value'] + ',' + i['estimation'] + ',' + i['status'])
            else:
                fh.write(
                    dict['id'] + ',' + dict['title'] + ',' + dict['user_story'] + ',' + dict['acceptance_criteria'] + ',' +
                    dict['business_value'] + ',' + dict['estimation'] + ',' + dict['status'])
            fh.write("\n")
    fh.close()
