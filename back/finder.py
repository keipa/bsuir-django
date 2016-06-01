import back.database
import postgresql.driver as pg_driver


class Finder():
    def __init__(self, request):
        base = back.database.InvertedDatabase()
        self.a = base.finding(request)


    def ranging(self):
        answer = {}

    def response(self):
        return self.a




def main():
    f = Finder("pleased")
    print(f.response())

if __name__ == '__main__':
    main()