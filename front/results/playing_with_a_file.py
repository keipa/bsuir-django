




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


def add_result(file,link, desc):
    f = open(file, "a")
    f.write("<a href=\""+link+"\">"+link+"</a>")
    f.write("<div class=\"description\">"+desc+"</div>")

def close_file(file):
    f = open(file, "a")
    f.write("</body>\n</html>")

def main():
    clean_file("base.html")
    add_result("base.html", "kekek.com", "ololololololol")
    add_result("base.html", "kekek.com", "ololololololol")
    add_result("base.html", "keek.com", "ololololololol")
    close_file("base.html")



if __name__ == '__main__':
    main()