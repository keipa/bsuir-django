from crawler import *
import Queue
from multiprocessing import Process
import argparse
from models import Forward, Inverted


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
        # self.queue = deque([start_url])
        self.queue = Queue.Queue()
        self.queue.put(start_url)
#        self.inv = database.InvertedDatabase()
#        self.forw = database.ForwardDatabase()
        self.indexed = 0

    def process(self):
        # try:
        self.indexed += 1
        while not self.queue.empty():
            self.process_one_link()
      
    def process_one_link(self):
        cur = Crawler(self.queue.get())
        if cur.is_banned:
            print("banned by ", cur.web_address)
            return
        for link in cur.urls_on_the_page:
            self.queue.put(link)

        try:
            Forward.objects.get(link=cur.web_address)
            print("repeated link:  " + cur.web_address)
        except Forward.DoesNotExist:
            Forward(link = cur.web_address, title = cur.title, text = " ".join(cur.clear_text),
                number_of_words = len(cur.clear_text)).save()
            print("Indexed {}".format(cur.web_address))

        for current_word in cur.clear_text:
            try:
                w = Inverted.objects.get(word = current_word, link = cur.web_address)
                w.entries += 1
                w.save()
            except Inverted.DoesNotExist:
                Inverted(word = current_word, link = cur.web_address).save()    

 
def process_one_link(web_adress):
    indexer = Indexer(web_adress)
    proc = Process(target = indexer.process_one_link)
    proc.start()


def multiproc():
    indexer1 = Indexer("https://www.python.org/")
    indexer2 = Indexer("https://www.postgresql.org/")
    indexer3 = Indexer("https://angularjs.org/")
    indexer4 = Indexer("https://www.twitter.com/")

    p1 = Process(target=indexer1.process)
    p2 = Process(target=indexer2.process)
    p3 = Process(target=indexer3.process)
    p4 = Process(target=indexer4.process)
    p1.start()
    p2.start()
    p3.start()
    p4.start()



def indexing(link, count):

    print("Entering point: {},\n going throught {} links".format(link, str(count)))
    # a = Indexer(link)
    # cpus = multiprocessing.cpu_count()
    # for _ in range(int(count/4)):
    multiproc()
    # a.process_link()
    # print("indexed: "+str(a.indexed))
    # a.process_link()




def main(link = "https://www.postgresql.org/"):
    # parser = create_parser()
    # namespace = parser.parse_args()
    indexing(link, 100 )


# if __name__ == '__main__':
#     main()