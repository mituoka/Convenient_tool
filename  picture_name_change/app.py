import glob
import os
import sys

def main():
    path='null'
    print('変更ディレクトリを入力してください')
    dir_name = input('>> ')
    print('統一したいファイル名を入力してください')
    new_file_name_input = input('>> ')

    files_path = glob.glob("./"+dir_name+"/*")
    for (number,file_path) in enumerate(files_path, 1):
        
        # ファイル名を取得する
        file_name=os.path.basename(file_path)

        # 拡張子の取得('script', '.py')
        path, ext = os.path.splitext( os.path.basename(file_path) )

        # 新しいファイル名を生成
        new_file_name=str(number)+'_'+new_file_name_input

        # 新しいファイルパスを生成
        new_path="./"+dir_name+'/'+new_file_name

        os.rename(file_path,new_path+ext)

# プログラム7｜mainを呼び出す
if __name__ == "__main__":
    main()