---
layout: page
title: Random Song
permalink: /random-song
---

# Random Song Recommendation
I figure just about everyone loves music and I wanted to add some additional functionality to this site. So I built a quick way to share a song with anyone visiting. Click the "Get a random song!" button below to get a random song recommendation from a database of songs I created with this site. One of the songs in the list is the song I took the domain name from as well. If you have a song to share with me send me an email or reach out on my other socials! (And maybe I'll get around to adding a feature to directly share a song with me on this site in the future.)
  

### How It Works
As a cloud computing enthusiast I wanted to build something I'm passionate about while using several different AWS Services together. This site (which is hosted on CloudFront and S3 - very original I know) hits API Gateway to communicate with a Lambda function. The Lambda fucntion selects a random song from the DynamoDB table with a single query operation rather than scanning the whole table (not that it matters with a table of this size). The result is sent back to this page and loaded in with the button press.
  
If that all sounds like gibberish, the ELI5 version is: This page sends a message to a different computer which then sends a return message that includes a random song from a list of songs I provided it. 
