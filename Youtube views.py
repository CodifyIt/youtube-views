from bs4 import BeautifulSoup
import requests
import sys
search = raw_input('Enter the video to search  ').split()

# TO search the video on youtube

link = requests.get('https://www.youtube.com/results',params={'search_query' : " ".join(search)})

soup = BeautifulSoup(link.text,'html.parser')

# TO get the href of the first video displayed on results

first_link = soup.find('div',{'class' : 'yt-lockup-content'})
# print first_link.h3.a['href'][9:]
print ''
print "          ",first_link.h3.a.string
print "          ",first_link.h3.span.string[3:-1]
print "          ",first_link.div.a.string
# TO go to the first video
link = requests.get('https://www.youtube.com/watch',params={'v' : first_link.h3.a['href'][9:]})
soup = BeautifulSoup(link.text,'html.parser')
# f = open('out.txt','w')
# f.write(soup.prettify().encode('utf-8'))
# f.close()
print "          ",
views = soup.find('div',{'class' : 'watch-view-count'})
print views.string
likes = soup.find('div',{'class' : 'video-extras-sparkbar-likes'})
like_per = int(round(float(likes.attrs['style'][7:-1])/10.0))
print "          ",
for i in range(like_per*2):
	sys.stdout.write(u'\N{WHITE UP-POINTING TRIANGLE}')
sys.stdout.write(' ')
for i in range(20-like_per*2):
	sys.stdout.write(u'\N{BLACK DOWN-POINTING TRIANGLE}')
print ''
print "          ",
like_count = soup.find('button',{'title' : 'I like this'})
print like_count.span.string,
print '  ',	
dislike_count = soup.find('button',{'title' : 'I dislike this'})
print dislike_count.span.string
