import glob
import os
import sys

def main():
    dir_name=sys.argv[1]

    files_path = glob.glob("./"+dir_name+"/*.jpg")
    for (number,file_path) in enumerate(files_path, 1):
        
        # ファイル名を取得する
        file_name=os.path.basename(file_path)
        new_file_name=str(number)+'_'+file_name
        new_path="./"+dir_name+'/'+new_file_name

        os.rename(file_path,new_path)

# プログラム7｜mainを呼び出す
if __name__ == "__main__":
    main()