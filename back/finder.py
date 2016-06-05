import back.database
import postgresql.driver as pg_driver


class Finder():
    def __init__(self, request):
        base = back.database.InvertedDatabase()
        self.a = base.finding(request)

    def response(self):
        answer = {}
        for each in self.a:
            if each in answer:
                answer[each] += 1
            else:
                answer[each] = 1
        return answer




def main():
    f = Finder("and")
    print(f.response())

if __name__ == '__main__':
    main()


# delete from inverted_index *;
# delete from forward_index *;