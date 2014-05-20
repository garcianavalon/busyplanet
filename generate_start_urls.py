f = open("urls.txt", 'w')
f.truncate()
base_url = "http://www.tripadvisor.com/ShowForum-g187147-i14-Paris_Ile_de_France.html\n"
f.write(base_url)
for i in range(20,99320,20):
    new_url = "http://www.tripadvisor.com/ShowForum-g187147-i14-o"+str(i)+"-Paris_Ile_de_France.html\n"
    f.write(new_url)
f.close()