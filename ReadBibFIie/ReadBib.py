# https://bibtexparser.readthedocs.io/en/v0.6.2/tutorial.html#preparing-a-bibtex-file
import bibtexparser
# remark
# 1. the data exported should be cleaned and checked first


with open('bibtex.bib','r',encoding='utf-8') as bibtex_file:
    bibtex_str = bibtex_file.read()

bib_database = bibtexparser.loads(bibtex_str)
# print(bib_database.entries[1]['abstract'])
# print(bib_database.entries[1]['title'])
# print(bib_database.entries[1]['year'])
# print(bib_database.entries[1]['author'])
# print(bib_database.entries[1]['keywords'])

earlist  = 2000
for i in range(0, len(bib_database.entries)):
    print(i)
    if int(bib_database.entries[i]['year']) < int(earlist):
        earlist = int(bib_database.entries[i]['year'])
print("the earliest publication is {0}".format(earlist))

abstract = []
year = []
title = []
year = 1971
with open("abstract.md","w+") as f:
    for i in range(0, len(bib_database.entries)):
        print("## {0}".format(bib_database.entries[i]['title']),file=f)
        print("## {0}".format(bib_database.entries[i]['title']))
        print("### {0}".format(bib_database.entries[i]['year']),file=f)
        print("### {0}".format(bib_database.entries[i]['year']))
        if 'abstract' in bib_database.entries[i]:
            print("> {0}".format(bib_database.entries[i]['abstract']))
            print("> {0}".format(bib_database.entries[i]['abstract']),file=f)


