import back.crawler as crawler
import back.database as database
from collections import deque
from multiprocessing import Process
import argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', "--link", default='https://www.postgresql.org/')
    parser.add_argument('-c', "--count", nargs='?', default='100')
    parser.add_argument('-r', "--relative", action='store_false')
    return parser


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
        self.indexed = 0

    def process_link(self):
        # try:
        self.indexed += 1
        cur = crawler.Crawler(self.quene.popleft())
        if cur.is_banned:
            print("banned by ", cur.web_address)
            return
        for link in cur.urls_on_the_page:
            self.quene.append(link)
        if self.forw.make_insertion(cur.web_address, cur.clear_text, cur.title) == 0:
            print("Indexing: " + cur.web_address +" words:"+str(cur.count_of_words))
            for each in cur.clear_text:
                self.inv.make_insertion(each, cur.web_address)
        else:
            print("repeated link:  " + cur.web_address)
        # except:
        #     print("quene is empty")
        # oh you))


def multiproc(a):
    p1 = Process(target=a.process_link())
    p2 = Process(target=a.process_link())
    p3 = Process(target=a.process_link())
    p4 = Process(target=a.process_link())
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()



def indexing(link, count ,isRelative):

    print("Entering point: {},\n going throught {} links".format(link, str(count)))
    a = Indexer(link)
    # cpus = multiprocessing.cpu_count()
    for _ in range(int(count/4)):
        multiproc(a)
    print("indexed: "+str(a.indexed))
    # a.process_link()




def main():
    parser = create_parser()
    namespace = parser.parse_args()
    indexing(namespace.link, int(namespace.count), namespace.relative)


if __name__ == '__main__':
    main()

