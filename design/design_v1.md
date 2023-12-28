## Design Version1
<strong>Aim: </strong>build a small search engine to help me get inspirations or ideas for doing research work. Intended to use this in America, so English. I major in Computer Science, so I would like to explore cs topics, and ofcourse other topics as well, like biology, physics, etc. 

### Simple Frontend:
Need to have an input field, and then when I query, I will get back a list of results with titles, some descriptions, and links to the sites.

In Microsoft Edge, their search page has many news and weather data etc. I feel like doing something like that is cool. I can put hacker news or some other tech news in the search page to find the latest tech news! Good for research ideas. To do this, I would either call API or just do a real time web scrape. Maybe just the API calling is fine. So, what tech news publications should I have? Uhm, I will put a list here and then see what I can do...

Weather API: https://openweathermap.org/api (make an account...)1,000 API calls per day for free

Tech news publishers [hackernoon.com, wired.com, space.com, technologyreview.com, marktechpost.com] 
I will only need like at most 15 tech news showing to me, so 3 news from each website. I actually want to make news its own small section. Anyway, this will be enough for the frontend.


### For the info query API we have:

Get /query<br>
params: search_query=user input, page number?<br>

returns: list of websites titles with short descriptions and associated URLs<br>


I would also like to query images, like a reverse image search. Why do that? Well because I just want to. (Just like in your system design interview people ask you to design stuff you would never actually build.)

This image look up functionality could be challenging because I would need to find a way to also store images and then figure out how to do image feature matching.

For user input: I will say I want to achieve something that can 

(Note:<br>
I didn't want to make things complicated (having a search engine no one but myself would use), so I would not even think about load balancers. This would be best for personal use. But I think adding it in the future is not hard if people like this.)

### For the Database:
My goal is to scrape 1 TB of website data. Why? Well, I never tried it, so I want to try it. Roast me what ever you like...

Assuming a web site is 2 MB as of the year 2023, then I would roughly need to scrape 1,048,576 MB / 2 MB = 524,288 websites UHmm, OK.

For research inspirations, I would like to gather useful information and not useless information so that I won't waste my money storing data. Thus, I would need to search some target websites to begin. By reverse thinking for now, I could probably come up a list of website that I don't want to store. Also, I don't want to have duplicated websites. 

So, what to store?<br>
Text data: 


Image data: 


### For Data collection:

#### Crawler:
Uhm, so my data source doesn't always have to be from crawling web pages. I can also call a bunch of APIs of my interest. 

Anyways, to actually start getting some data, we need some seeders to start with the crawling. Ideally, the more links in the seeders we have that has value in them, the better. Since I only want about 1 TB of useful data, 

seeder sites: [https://stackexchange.com/sites, ]



#### A bunch of API calls:
Since there could be a lot of different API usages, I need to monitor the # of call times and used time stamps, and figure out where to store them. Will I ever include videos? Good question. I will probably not do that. Youtube is already fine. 


### For the Indexer: 