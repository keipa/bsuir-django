from indexer.models import Forward, Inverted

class Result():
    def __init__(self, link, title, description):
        self.link = link
        self.title = title
        self.description = description

def get_results(request):
    results = []
    try:
        for word in request.split(" "):
            links = Inverted.objects.get(word = request).links
            for cur_link in links:
                link_info = Forward.objects.get(link = cur_link)
                results.append(Result(link_info.link, link_info.title, link_info.text[:100]))

    except Inverted.DoesNotExist:
        print ("nu da lando")

    return results


# class Finder():
#     def __init__(self, request):
#         self.req = request
#         ibase = back.database.InvertedDatabase()
#         self.fbase = back.database.ForwardDatabase()
#         self.response = ibase.finding(request)
#         self.response = self.ranging()
#         self.get_description()

#     def get_description(self):
#         for link in self.response:
#             text = self.fbase.get_text(link)
#             text = text[0].replace("\n", ""), text[1]
#             self.response[link] = (self.response[link], text[0][:200]+"...", text[1])

#     def ranging(self):
#         answer = {}
#         for each in self.response:
#             if each in answer:
#                 answer[each] += 1
#             else:
#                 answer[each] = 1
#         return answer




# def main():
#     f = Finder("postgres")
#     # print(f.response)
#     res = f.response



#     print("Searching for: \"", f.req, "\"")
#     for link in res:
#         print(link,"\n", res[link])

# if __name__ == '__main__':
#     main()


# # delete from inverted_index *;
# # delete from forward_index *;