import back.crawler as crawler
import back.database as database
from collections import deque


def benchmark(func):
    import time
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        print("--- {0} seconds ---".format(time.time() - start_time))
        return res
    return wrapper


class Indexer():
    def __init__(self, start_url):
        self.quene = deque([start_url])
        self.inv = database.InvertedDatabase()
        self.forw = database.ForwardDatabase()

    @benchmark
    def process_link(self):
        # try:
        cur = crawler.Crawler(self.quene.popleft())

        for link in cur.urls_on_the_page:
            self.quene.append(link)
        if self.forw.make_insertion(cur.web_address, cur.string_text) == 0:
            for each in cur.clear_text:
                self.inv.make_insertion(each, cur.web_address)
            print("Indexed: " + cur.web_address)
        else:
            print("repeated link" + cur.web_address)
        # except:
        #     print("quene is empty")
        # oh you))





def main():
    a = Indexer("http://www.bsuir.by/en/enrollment")
    # while True:
    a.process_link()







if __name__ == '__main__':
    main()

