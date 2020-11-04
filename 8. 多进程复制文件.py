from multiprocessing import Pool, Manager
import os

def main():
    # Get basic info
    old_folder_name = input('Please enter the target folder name with its path: ')
    new_folder_name = input('Please enter the new folder name with its path: ')
    
    os.mkdir(new_folder_name)
    file_names = os.listdir(old_folder_name)
    new_file_names = []

    # multiprocessing.Pool
    # 给主程序创建个对象的队列
    q = Manager().Queue()
    p = Pool(4)
    for file in file_names:
        p.apply_async(copyFolderFiles, args = (file, old_folder_name, new_folder_name, q))
        new_file_names.append(q.get())

    percent = len(new_file_names)/len(file_names)
    print(f'{round(percent,2)*100}% of the files have been copied')
    
    p.close()
    p.join()

def copyFolderFiles(file, old_folder_name, new_folder_name, q):

    old_file_path = old_folder_name + '/' + file
    new_file_path = new_folder_name + '/' + file
    
    with open(old_file_path, 'rb') as reader, open(new_file_path, 'wb') as writer:
        while reader.readline():
            line = reader.readline()
            writer.write(line)

    # reader.close()
    # writer.close()
    # 把文件名扔进主程序的队列
    q.put(file)

if __name__ == '__main__':
    main()