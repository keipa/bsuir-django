from back.finder import Finder


def clean_file(file):
    f = open(file, "r")
    lines = f.readlines()
    f.close()
    f = open(file, "w")
    for line in lines:

        if line != "<div class=\"lborder\"> </div>" + "\n":
            f.write(line)
        else:
            f.write(line)
            f.close()
            break


def add_result(file, link, title, desc):
    f = open(file, "a")
    f.write("<div class=\"container\">")
    f.write("<a href=\""+link+"\">"+title+"</a>\n")
    f.write("<div class=\"description\">"+desc+"</div>\n</div>\n\n")

def close_file(file):
    f = open(file, "a")
    f.write("</body>\n</html>\n{% endblock content %}")


def modify_html(request):
    req = request.GET["request"]
    clean_file("D:/LABS/bsuir-django/search/finder/templates/finder/base.html")
    f = Finder(req)
    res = f.response
    while len(res) != 0:
        max_link = ""
        max_range = 0
        for link in res:
            if res[link][0] > max_range:
                max_range = res[link][0]
                max_link = link
        add_result("D:/LABS/bsuir-django/search/finder/templates/finder/base.html", max_link, res[max_link][2], res[max_link][1])

        # res[max_link][1] - inser intead of content without unicode
        del res[max_link]
    close_file("D:/LABS/bsuir-django/search/finder/templates/finder/base.html")
    # print("ready")


def main():
    pass


if __name__ == '__main__':
    main()