'''

Author: Robert Ferdinand (2021)

This PYTHON 3.7 program parses a BibTex file called 'source.bib' and outputs a large CSV file called 'out.csv'.

To run this program, please note the following:

1. The file 'source.bib' needs to be present in the local folder or a path to the file needs to be provided in OUTFILE.
2. From the command prompt, one can run the program using the command 'python py SIL-Task1&2.py'.


'''

from pybtex.database.input import bibtex

INFILE = 'source.bib'
OUTFILE = 'out.csv'

fh = open(OUTFILE, "w")
fh.write("ID"+","+"TITLE"+","+"LGCODE"+","+"YEAR"+"\n")


parser = bibtex.Parser()

bibdata = parser.parse_file(INFILE)


for bib_id in bibdata.entries:
    b = bibdata.entries[bib_id].fields
    try:
        TITLE = str(b['title'])
        TITLE = TITLE.replace(',','')
        TITLE = TITLE.replace('"','')
        LGCODE = str(b['lgcode'])
        LGCODE = LGCODE.replace(',','')
        LGCODE = LGCODE.replace('"','')
        YEAR = str(b['year'])
        YEAR = YEAR.replace(',','')
        YEAR = YEAR.replace('"','')
        fh.write(str(bib_id)+","+TITLE+","+LGCODE+","+YEAR+"\n")
    except(KeyError, UnicodeEncodeError):
        fh.write(str(bib_id)+","+" "+","+" "+","+" "+"\n")
        
 
fh.close()
     
