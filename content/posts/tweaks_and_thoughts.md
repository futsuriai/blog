Title: Minor Updates + Tests
Date: 2013-03-26 00:55
Author: Andres Franceschi
Category: blogging
Tags: blogging, pelican
Keywords: blogging, pelican  

<!-- PELICAN_BEGIN_SUMMARY -->
My pre-trip thoughts to start off the "travel blog" proper will have to wait. If you are interested and use RSS you can now subscribe to a feed specific to posts relating to a particular category using the sidebar. You can also subscribe to a general feed using the link in the header or just inputting any url on the site on [Google Reader][] while you still can (note to people reading in the future, this was a wonderful way to read feeds that is set to die soon).

The main reason for this post is to test how well inserting albums of pictures will work. As a sample I'll use some I took during my trip to Lebanon in September of 2011. Warning, the album is extremely uncurated. I hid the tests behind the more button just because it'd be annoying to see them on the index so click ahead if interested.

<!-- PELICAN_END_SUMMARY -->

##Album embed

<table style="width:194px;"><tr><td align="center" style="height:194px;background:url(https://picasaweb.google.com/s/c/transparent_album_background.gif) no-repeat left"><a href="https://picasaweb.google.com/109314153461120302310/Lebanon2011ByMe?authuser=0&authkey=Gv1sRgCLeA-oiCmvyawAE&feat=embedwebsite"><img src="https://lh6.googleusercontent.com/-8u95mTGbDl8/ToY_ztvi6CE/AAAAAAAAA8o/KNyl9OEnDaU/s160-c/Lebanon2011ByMe.jpg" width="160" height="160" style="margin:1px 0 0 4px;"></a></td></tr><tr><td style="text-align:center;font-family:arial,sans-serif;font-size:11px"><a href="https://picasaweb.google.com/109314153461120302310/Lebanon2011ByMe?authuser=0&authkey=Gv1sRgCLeA-oiCmvyawAE&feat=embedwebsite" style="color:#4D4D4D;font-weight:bold;text-decoration:none;">Lebanon 2011 - by Me</a></td></tr></table>

##Slideshow embed

<embed type="application/x-shockwave-flash" src="https://picasaweb.google.com/s/c/bin/slideshow.swf" width="400" height="267" flashvars="host=picasaweb.google.com&hl=en_US&feat=flashalbum&RGB=0x000000&feed=https%3A%2F%2Fpicasaweb.google.com%2Fdata%2Ffeed%2Fapi%2Fuser%2F109314153461120302310%2Falbumid%2F5658280139522500641%3Falt%3Drss%26kind%3Dphoto%26authkey%3DGv1sRgCLeA-oiCmvyawAE%26hl%3Den_US" pluginspage="http://www.macromedia.com/go/getflashplayer"></embed>

## Weird JS Technique
<div id="slideShow">Loading...</div>
<script type="text/javascript" src="http://www.google.com/jsapi"></script><script type="text/javascript" src="http://www.google.com/uds/solutions/slideshow/gfslideshow.js"></script>

<script type="text/javascript"> function LoadSlideShow() { var feed = "https://picasaweb.google.com/data/feed/base/user/109314153461120302310/albumid/5658280139522500641?alt=rss&kind=photo&authkey=Gv1sRgCLeA-oiCmvyawAE&hl=en_US"; var options = {displayTime:2000, transistionTime:600, scaleImages:true,  fullControlPanelSmallIcons : true,  fullControlPanel : true, linkTarget : google.feeds.LINK_TARGET_BLANK}; var ss = new GFslideShow(feed, "slideShow", options); } /** * Use google.load() to load the AJAX Feeds API * Use google.setOnLoadCallback() to call LoadSlideShow once the page loads */ google.load("feeds", "1"); google.setOnLoadCallback(LoadSlideShow); </script>

My guess is I'll opt for the last one because it'll work on phones/Flash-less devices... we'll see how it goes.

[Google Reader]: http://www.google.com/reader/