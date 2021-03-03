import http.client

conn = http.client.HTTPSConnection("google-news1.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "824460c9femsh55e500e823adb60p1ff0e9jsnba59e997ceeb",
    'x-rapidapi-host': "google-news1.p.rapidapi.com"
    }

conn.request("GET", "/topic-headlines?topic=WORLD&country=US&lang=en", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))