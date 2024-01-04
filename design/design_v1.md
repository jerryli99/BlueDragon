## Design Version1
<strong>Aim: </strong>build a small search engine to help me get inspirations or ideas for doing research work. I major in Computer Science, so I would like to explore cs topics, and of course other topics as well, like biology, physics, philosophy, etc. In other words, I want to break my habit of one way of thinking. I can build a special search engine to help me with that. I learned that putting a lot of effort doesn't necessary give me the result I want because effort is almost independent from the desired result. I plan to put little effort, using the right method to achieve the ratio --> effort:result = 1:10 


### What does inspiration search mean?



### Simple Frontend:
I thought about using docker, but I am not going to even bother doing that for now. Might change (12/28/2023).

Need to have an input field, and then when I query, I will get back a list of results with titles, some descriptions, and links to the sites.

In Microsoft Edge, their search page has many news and weather data etc. I feel like doing something like that is cool. I can put hacker news or some other tech news in the search page to find the latest tech news! Good for research ideas. To do this, I would either call API or just do a real time web scrape. Maybe just the API calling is fine. So, what tech news publications should I have? Uhm, I will put a list here and then see what I can do...

Weather API: https://openweathermap.org/api (make an account...)1,000 API calls per day for free

Tech news publishers [hackernoon.com, wired.com, space.com, dev.to, technologyreview.com, marktechpost.com, quantamagazine.org, bigthink.com] 

I will only need like 3 news from each website. I actually want to make news its own small section. Anyway, this will be enough for the frontend.


### For the info query API we have:
Use Python Django for the backend.

Get /query<br>
params: search_query=user input, page number?<br>

returns: list of websites titles with short descriptions and associated URLs<br>


I would also like to query images, like a reverse image search. Why do that? Well because I just want to. (Just like in your system design interview people ask you to design stuff you would never actually build.)

This image look up functionality could be challenging because I would need to find a way to also store images and then figure out how to do image feature matching.

For user input: I will say I want to achieve something that can 

(Note: I didn't want to make things complicated (having a search engine no one but myself would use), so I would not even think about load balancers. This would be best for personal use. But I think adding it in the future is not hard if people like this.)

### For the Database:
My goal is to scrape 1 TB of website data. Why? Well, I never tried it, so I want to try it. Roast me what ever you like...

Assuming a web site is 2 MB as of the year 2023, then I would roughly need to scrape 1,048,576 MB / 2 MB = 524,288 websites UHmm, OK.

For research inspirations, I would like to gather useful information and not useless information so that I won't waste my money storing data. Thus, I would need to search some target websites to begin. By reverse thinking for now, I could probably come up a list of website that I don't want to store. Also, I don't want to have duplicated websites. 

So, what to store?<br>
Text data: 


Image data: 


The crawl database:


### For Data collection:

#### Crawler:
Uhm, so my data source doesn't always have to be from crawling web pages. I can also call a bunch of APIs of my interest. 

Anyways, to actually start getting some data, we need some seeders to start with the crawling. Ideally, the more links in the seeders we have that has value in them, the better. 

Seeder sites: [https://stackexchange.com/sites, https://arxiv.org, https://www.biorxiv.org, https://plato.stanford.edu/contents.html, https://www.quantamagazine.org, https://medium.com]

What kinds of file will I handle? html, xml, img (jpeg, jpg, png, webp...), pdf(maybe),...

Pagination handle:...

#### Crawling Strategy:



#### Download Data to Local Machine

So, I don't need to assume I have no information at the beginning. Like wikipidia has a lot of site data public to download as a bz2 file (https://en.wikipedia.org/wiki/Wikipedia:Database_download), so I will not just rely only on the web crawler. Wikipedia also mentioned that using web crawlers to download large number of htmls is not a good idea for me and them. I used the torrent to download the whole wikipedia (https://meta.wikimedia.org/wiki/Data_dump_torrents#English_Wikipedia). Should I upload this to the cloud? Uhm... I mean it is 91 GB of data in 1 xml file, so...we will see. Maybe not since I don't see the point of doing it, or I can just split the file in slices...

Uhm, perhaps I can also design a way for you to also add any pdf files(i.e books) you downloaded to your own local DB and then do the indexing for you of course...

#### A bunch of API calls:
Since there could be a lot of different API usages, I need to monitor the # of call times and used time stamps, and figure out where to store them. Maybe build a mini-api manager here. Then have a file to record the api meta data and a python scirpt to check. Will I ever include videos? Good question. I will probably not do that. Youtube is already fine. 


### For the Indexer: 