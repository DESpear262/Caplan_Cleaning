def checkByline(file):
    with open(file, encoding="utf8") as f:
        for line in f:
            if '<!-- <a href="https://www.econlib.org/' in line:                                            #Unique identifier for byline code. Also appears in recommended articles but main article byline always appears first
                return 'author/bcaplan/" class="author url fn" rel="author"> -->Bryan Caplan' in line       #Unique identifier for Bryan's articles in byline code line
