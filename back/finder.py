import back.database
import postgresql.driver as pg_driver


class Finder():
    def __init__(self, request):
        self.req = request
        ibase = back.database.InvertedDatabase()
        self.fbase = back.database.ForwardDatabase()
        self.response = ibase.finding(request)
        self.response = self.ranging()
        self.get_description()

    def get_description(self):
        for link in self.response:
            text = self.fbase.get_text(link)
            text = text.replace("\n", "")
            self.response[link] = (self.response[link], text[:200]+"...")

    def ranging(self):
        answer = {}
        for each in self.response:
            if each in answer:
                answer[each] += 1
            else:
                answer[each] = 1
        return answer




def main():
    f = Finder("postgres")
    # print(f.response)
    res = f.response
    print("Searching for: \"", f.req, "\"")
    for link in res:
        print(link,"\n", res[link])

if __name__ == '__main__':
    main()


# delete from inverted_index *;
# delete from forward_index *;