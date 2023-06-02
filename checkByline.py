def checkByline(file):
    with open(file, encoding="utf8") as f:
        for line in f:
            if '<!-- <a href="https://www.econlib.org/' in line:
                return 'author/bcaplan/" class="author url fn" rel="author"> -->Bryan Caplan' in line