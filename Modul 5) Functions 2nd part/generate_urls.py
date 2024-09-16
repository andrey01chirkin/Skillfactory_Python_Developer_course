def generate_urls(url, low, high):
    for i in range(low, high+1):
        yield f"{url}{i}"


url_generator = generate_urls("/product/", 1, 3)
for url in url_generator:
    print(url)
# /product/1
# /product/2
# /product/3
