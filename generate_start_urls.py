f = open("urls.txt", 'w')
base_url = "http://www.tripadvisor.com/ShowForum-g186338-i17-London_England.html\n"
f.write(base_url)
for i in range(20,93180,20):
    new_url = "http://www.tripadvisor.com/ShowForum-g186338-i17-o"+str(i)+"-London_England.html\n"
    f.write(new_url)
f.close()