from icrawler.builtin import BingImageCrawler


def main():
    bing_crawler = BingImageCrawler(downloader_threads=4,storage={'root_dir': 'data'})
    bing_crawler.crawl(keyword='Hoshina Mizuki', filters=None, offset=0, max_num=100)

    # 画像のダウンロード
    crawler = BingImageCrawler(downloader_threads=4,
                                    storage={'root_dir': 'data'})
    filters = dict(
        type='“photo”',
        color='blackandwhite',
        size='1920x1080',
        license='commercial,modify',
        date='pastyear'
    )

    # --`type` – “photo”, “clipart”, “linedrawing”, “transparent”, “animated”.
    # --`color` – “color”, “blackandwhite”, “red”, “orange”, “yellow”, “green”, “teal”, “blue”, “purple”, “pink”, “white”, “ gray ”,“ black ”,“ brown ”
    # --`size` – “large”, “medium”, “small” or larger than a given size (e.g. “> 640x480”).
    # --`license` – “creativecommons”, “publicdomain”, “noncommercial”, “commercial”, “noncommercial, modify”, “commercial, modify”.
    # --`layout` – “square”, “wide”, “tall”.
    # --`people` – “face”, “portrait”.
    # --`date` – “pastday”, “pastweek”, “pastmonth”, “pastyear”.


    crawler.crawl(keyword='Hoshina Mizuki', filters=filters, offset=0, max_num=100)

if __name__ == "__main__":
    main()