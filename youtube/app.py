import csv
from apiclient.discovery import build


def main():

    YOUTUBE_API_KEY = '自分のAPIキーを入力'

    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

    search_response = youtube.search().list(
    part='snippet',
    #検索したい文字列を指定
    q='ボードゲーム',
    #視聴回数が多い順に取得
    order='viewCount',
    type='video',
    ).execute() 

# プログラム7｜mainを呼び出す
if __name__ == "__main__":
    main()