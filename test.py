import lxml
from lxml import etree
import urllib
youtube = etree.HTML(urllib.urlopen("http://www.youtube.com/watch?v=KQEOBZLx-Z8").read()) 
video_title = youtube.xpath("//span[@id='eow-title']/@title") 
print (''.join(video_title))