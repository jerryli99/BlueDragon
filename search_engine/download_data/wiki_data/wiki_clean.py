'''
Assuming you have the wiki database dump file wiki_something.xml downloaded. 
I will not upload a 91 GB file to Github...
Where can you get it? See the design folder, design_v1.md, section "crawler"

Notes about wiki's xml:

A peek into the file (since the decompressed xml is 91 GB):

file_path = "F:\enwiki-20230820-pages-articles-multistream.xml\enwiki-20230820-pages-articles-multistream.xml"
batch_size = 100000  # Choose an appropriate batch size based on your requirements

# Open the file and read it in batches
with open(file_path, 'r', encoding='utf-8') as file:
    # Read a chunk of data
    chunk = file.read(batch_size)
    print(chunk)


we can see that the format is something like:


'''

