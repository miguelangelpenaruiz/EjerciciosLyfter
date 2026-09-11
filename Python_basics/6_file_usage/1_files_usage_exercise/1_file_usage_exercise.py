def main(path):
    with open(path,'r', encoding = 'utf-8') as file:
        content = file.readlines()
        print(content)
        new_content = order_alphabetical(content)
        create_new_file(new_content)

def order_alphabetical(list):
    for i in range(len(list)):
        for index in range(len(list)-1-i):
            if list[index] > list[index + 1]:
                list[index], list[index +1] = list[index + 1], list[index]
    return list

def create_new_file(list):
    with open('6_File_Usage/1_files_usage_exercise/songs2.txt','w', encoding='utf-8') as file:
        file.writelines(list)

main('6_File_Usage/1_files_usage_exercise/songs.txt')
