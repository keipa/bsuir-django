from indexer.models import Forward, Inverted
from math import log


class Result():
    def __init__(self, link, title, description, score):
        self.link = link
        self.title = title
        self.description = description
        self.score = score

def get_results(request):
    results = []
    links = set()
    # words = []
    # words.append(request)
    # words.extend(request.strip().split(" "))
    words = request.strip().split(" ")
    try:
        for cur_word in words:
            links.update([obj.link for obj in Inverted.objects.filter(word = cur_word)])
            # for cur_link in links:
            #     link_info = Forward.objects.get(link = cur_link)
            #     results.append(Result(link_info.link, link_info.title, link_info.text[:100]))
        # print links
        common_number_of_words = sum([Forward.objects.get(link = cur_link).number_of_words for cur_link in links])
        average_number_of_words = common_number_of_words / len(links)

        print links
        for cur_link in links:
            print(cur_link)
            link_info = Forward.objects.get(link = cur_link)
            results.append(
                Result(cur_link, link_info.title,
                    link_info.text[:100],
                    get_score_bm25(words, len(links), link_info, average_number_of_words))
                )
        results = ranging(results)    

    except ValueError: #Inverted.DoesNotExist:
        print ("word does not exist")

    return results

def ranging(results):
    return sorted(results, key=lambda res: res.score, reverse=True)


def get_score_bm25(words, size_of_collection, link_info, average_number_of_words):
    k = 2.0
    b = 0.75

    score = 0

    for cur_word in words:
        try:
            entries = Inverted.objects.get(word = cur_word, link = link_info.link).entries
            entries = float(entries)
            idf = log((size_of_collection - entries + 0.5) / (entries + 0.5))
            term_frequency = entries / link_info.number_of_words
            word_score = idf * ((term_frequency * (k + 1)) / (term_frequency + k * (1 - b + b * (link_info.number_of_words / average_number_of_words))))
            if word_score > 0:
                score += word_score
        except Inverted.DoesNotExist:
            print ("word does not exist")
    return score


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