import postgresql.driver as pg_driver


class ForwardDatabase():
    def __init__(self):
        self.db = pg_driver.connect(user="postgres",
                                    password='35227411',
                                    host='localhost',
                                    database='postgres',
                                    port=5432)
        self.new_ins = self.db.prepare("INSERT INTO forward_index VALUES ($1, $2, $3);")
        self.count_of_insertions = 0
        self.how_often_show_stats = 50
        print("Forward base connected")

    def show_all_words(self):
        for text in self.db.prepare("SELECT url FROM forward_index"):
            print(text[0])

    def get_text(self, link):
        results = self.db.prepare("SELECT content FROM forward_index WHERE url=\'"+link+"\'")
        content = []
        for con in results:
            content.append(con)
        title_res = self.db.prepare("SELECT title FROM forward_index WHERE url=\'"+link+"\'")
        title_content = []
        for con in title_res:
            title_content.append(con)
        # print("debug")
        return content[0][0], title_content[0][0]

    # def get_title(self, link):
    #     results = self.db.prepare("SELECT title FROM forward_index WHERE url=\'"+link+"\'")
    #     content = []
    #     for con in results:
    #         content.append(con)
    #     return content[0][0]

    def show_base(self):
        for text in self.db.prepare("SELECT * FROM forward_index;"):
            print(text)



    # def __del__(self):
    #     self.db.close()



    def make_insertion(self, key, value, title):
        # self.count_of_insertions += 1
        # if self.count_of_insertions % self.how_often_show_stats == 0:
        #     print("added: ", self.count_of_insertions)

        results = self.db.prepare("SELECT url FROM forward_index WHERE url=\'"+key+"\'")
        is_any_elements = []
        for each in results:
            is_any_elements.append(each)
        if len(is_any_elements) == 0:
            self.make_new_insertion(key, value, title)
            return 0
        else:
            return 1

    def make_new_insertion(self, url, all_text, title):
        s = ""
        c = 0
        for each in all_text:
            s += each + " "
            c += 1
            if c == 40:
                break
        self.new_ins(url, s, title)



class InvertedDatabase():
    def __init__(self):
        self.db = pg_driver.connect(user="postgres",
                                    password='35227411',
                                    host='localhost',
                                    database='postgres',
                                    port=5432)
        self.new_ins = self.db.prepare("INSERT INTO inverted_index VALUES ($1, $2);")
        self.update = self.db.prepare("UPDATE inverted_index SET urls=$1 WHERE word=$2;")
        self.count_of_insertions = 0
        self.how_often_show_stats = 10000
        self.find = self.db.prepare("select urls from inverted_index where word=$1;")
        print("Inverted Base connected")

    def show_all_words(self):
        for text in self.db.prepare("SELECT word FROM inverted_index"):
            print(text[0])

    def finding(self, request):
        a = []
        for word in request.split(" "):
            result = self.find(word)
            for ar in result:
                for link in ar[0]:
                    a.append(link)
        return a

    def show_base(self):
        for text in self.db.prepare("SELECT * FROM inverted_index;"):
            print(text)

    # def __del__(self):
    #     self.db.close()




    def make_insertion(self, key, value):
        self.count_of_insertions += 1
        if self.count_of_insertions % self.how_often_show_stats == 0:
            print("added: ", self.count_of_insertions)
        results = self.db.prepare("SELECT word FROM inverted_index WHERE word=\'"+key+"\'")
        is_any_elements = []
        for each in results:
            is_any_elements.append(each)
        if len(is_any_elements) != 0:
            self.make_old_insertion(key, value)
        else:
            self.make_new_insertion(key, value)

    def make_new_insertion(self, key, value):
        self.new_ins(key, [value])

    def make_old_insertion(self, key, value):
        results = self.db.prepare("SELECT urls FROM inverted_index WHERE word=\'"+key+"\'")
        urls = []
        for arrays in results:
            for array in arrays:
                for each in array:
                    urls.append(each)
        urls.append(value)
        # self.db
        self.update(urls, key)
        # print("added")


def main():

    # we can connect to database
    # add elements to it

    base = InvertedDatabase()
    base.finding("word1")
    # base.show_base()
    # del base


if __name__ == '__main__':
    main()