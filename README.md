# Twitter-Wordcloud-Generator
A little Python script to generate and post a wordcloud with any user's mentions.

The script is less than a hundred lines of code (comments included), and does as follows:
1. Asks for any Twitter's account name on an input promt.
2. Scrapes over the said user's timeline fetching the mentions.
3. Makes a wordcloud of the mentions retrieved on the previous step.
4. Post the resulting image tagging the provided user.

It's a very simple script, although it does implement the following modules: Tweepy, collections, Pillow and wordcloud.

Notice that by mistake I imported the path module. This is due I had the intention of adding the posibility of deleting the wordcloud after being tweeted.

This could be the starter point for a full Twitter bot that replies the wordcloud to anyone that tweets a given hashtag or anything of the sort.
I may end up scaling this to that point although I'm not sure If I'm gonna go on that road or move to some other project altogether.

Anyway, I hope you like it.
Thanks!
