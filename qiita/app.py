import requests
import json
import pprint

def main():
    	
    USER_ID='Aqua_MT'
    URL = "https://qiita.com/api/v2/users/"+ USER_ID+"/items"
    TOKEN = "795547a640bf1781d8c193b3a3a42e10a3709510"
    HEADER = {
        'Authorization': 'Bearer {}'.format(TOKEN),
    }
    response = requests.get(URL, headers=HEADER)
    data=response.json()
    pprint.pprint(data)

    for i in data:
        print('タイトル：'+i['title'])
        print('いいね数：'+str(i['likes_count']))
        print('============')
    # pprint.pprint(data)
    # print(data.title)

if __name__ == "__main__":
    main()