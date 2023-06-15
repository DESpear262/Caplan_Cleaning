# Caplan_Cleaning
A repo for the code used to scrape and clean old blog posts from EconLog for export to Substack. Non-cooperation from EconLog made it necessary to scrape all of EconLog and then refine and process the mirror by hand.

main.py is the primary control code, with both the main code and test code for the individual modules. It uses os.walk to loop through all files in a directory containing a mirror of econlog.org

checkByline.py takes in an html file, identifies the line which corresponds to the post byline, and then checks it for the code which uniquely identifies Bryan as the author. Lack of standardization in EconLog codebase made it necessary to manually check the files line-by-line instead of using linecache to directly access the byline

XMLDump.py takes in an html file and reprocesses it into an XML file which is compatible with Substack's import feature. Currently produces output which fails to upload to Substack, despite being recognized by Substack as a valid XML. Debugging help from Substack tech support pending.

Correcting the problems from this version of the project required considerable reworking, plus it gave me the opportunity to make some quality-of-life updates which weren't viable in this phase of the project. Version 2.0 is available here: https://github.com/DESpear262/caplan-cleaning-2.0
