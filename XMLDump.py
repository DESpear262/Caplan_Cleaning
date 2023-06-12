from bs4 import BeautifulSoup


def XMLDump(infile, outfile):
    try:
        # Open the html file and Parse it
        # using Beautiful soup's html.parser.
        with open(infile, 'r', encoding='utf-8') as inp:
            soup = BeautifulSoup(inp, 'html.parser')

        # Split the document by lines and join the lines
        # from index 1 to remove the doctype Html as it is
        # present in index 0 from the parsed document.
        title = str(soup.find("title"))
        title = title[:-18] + title[-8:]
        header = str(soup.find("section", {"class": "article-single-page jumbotron main-banner econlog-logo-wide-center"}))
        date = ""
        for p in header.splitlines(True):
            for month in ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]:
                if month in p:
                    date = p
        date = date[7: -9] +date[3: 7] + date[-9:-5]
        if len(date) == 10:
            date = f"0{date}"
        link = "https:/"
        for subdir in infile.split("\\")[2:]:
            link = f'{link}/{subdir}'

        content = str(soup.find("div", {"class": "post-content"}))[26: -7]

        # Open a output.xml file and write the modified content.
        with open(outfile, 'a', encoding='utf-8') as out:
            out.write( f'''
            <item>
                {str(title)}
                <link>{link}</link>
                <pubDate>{date}</pubDate>
                    <content:encoded><![CDATA[{content} 
                    <p>The post <a rel="nofollow" href="{link}">{title}</a> appeared first on <a rel="nofollow" href="https://www.econlib.org">Econlib</a>.</p>
                ]]></content:encoded>
            </item>
            ''')

    except Exception as e:
        print(f"{infile}:\n{e}\n\n")
