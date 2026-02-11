import requests
import os
import re # regular expression 
user = input("Enter the Image name : ")
user_agent = {
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"  
}
url = f"https://www.google.com/search?q={user}&tbm=isch&ved=2ahUKEwi99dbbsM78AhXU_jgGHYLwC0YQ2-cCegQIABAA&oq=moon&gs_lcp=CgNpbWcQAzIECCMQJzIHCAAQsQMQQzIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQMyBQgAEIAEOgcIIxDqAhAnOgQIABBDOggIABCxAxCDAVCNAliaEWCMFGgBcAB4BIAB8QWIAacfkgELMi0yLjIuMS4zLjGYAQCgAQGqAQtnd3Mtd2l6LWltZ7ABA8ABAQ&sclient=img&ei=WnbGY73gO9T94-EPguGvsAQ&bih=1007&biw=843"


response = requests.get(url = url, headers=user_agent).text
pattern = "\[\"https://.*\.jpg\",[0-9]+,[0-9]+\]"
# pattern = "\[\"https://\"]"
images = re.findall(pattern, response)
print(f"Total Images  : {len(images)}")
no_of_images = int(input("Number of images to be downloaded : "))

if images:
    if os.path.exists(user):
        os.mkdir(user)
        os.chdir(user)
    else:
        os.chdir(user)

    for image in images[:no_of_images]: 
        image_url = eval(image)[0]
        response = requests.get(url=image_url).content
        print(image_url)
