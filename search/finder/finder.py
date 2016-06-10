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
    
    words = request.strip().split(" ")
    for cur_word in words:
        links.update([obj.link for obj in Inverted.objects.filter(word = cur_word)])
    # links = links[:50]
    common_number_of_words = sum([Forward.objects.get(link = cur_link).number_of_words for cur_link in links])
    average_number_of_words = common_number_of_words / len(links)

    print len(links)
    for cur_link in links:
        print(cur_link)
        link_info = Forward.objects.get(link = cur_link)


        results.append(
            Result(cur_link, link_info.title,
                link_info.text[:500],
                get_score_bm25(words, len(links), link_info, average_number_of_words))
            )
    results = ranging(results)    

    return results

def ranging(results):
    return sorted(results, key=lambda res: res.score, reverse=True)


def get_score_bm25(words, size_of_collection, link_info, average_number_of_words):
    k = 2.0
    b = 0.75

    score = 0

    for cur_word in words:
        try:
            entries = len(Inverted.objects.filter(word = cur_word))
            entries = float(entries)
            kek = (size_of_collection - entries + 0.5) / (entries + 0.5)
            idf = log((size_of_collection - entries + 0.5) / (entries + 0.5))
            term_frequency = entries / link_info.number_of_words
            word_score = idf * ((term_frequency * (k + 1)) / (term_frequency + k * (1 - b + b * (link_info.number_of_words / average_number_of_words))))
            if word_score > 0:
                score += word_score
        except Inverted.DoesNotExist:
            print ("word does not exist")
    return score
