import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

search_ele = input("Enter product name:").strip().replace(" ", "")
search_url = f"https://www.flipkart.com/search?q={search_ele}"

df = pd.DataFrame([], columns=[
    'Search Product',
    'Obtained product',
    'Rating', 
    'Comment Header',
    'Comment Body',
    'Reviewer',
    'Location',
    'Review_ago'
])

try:
    headers = {"User-Agent": "Mozilla/5.0"}
    req = requests.get(search_url, headers=headers)
    web = bs(req.text, 'html.parser')
    products = web.find_all("div", {"class": "cPHDOP col-12-12"})

    for product_link in products:
        try:
            link = "https://www.flipkart.com" + product_link.div.div.div.a['href']        
            product_req = requests.get(link, headers=headers)   # FIXED here
            product_web = bs(product_req.text, 'html.parser')

            # product name fallback
            try:
                obtained_product = product_web.text[:30]
            except:
                obtained_product = "No product name"

            comment_boxes = product_web.find_all('div', {'class': 'RcXBOT'})

            for comment_box in comment_boxes:
                try:
                    rating = comment_box.div.div.div.find('div', {'class':'XQDdHH Ga3i8K'}).text
                except:
                    rating = "no rating"

                try:
                    comment_header = comment_box.div.div.div.find('p', {'class':'z9E0IG'}).text
                except:
                    comment_header = "No comment header"

                try:
                    comment_body = comment_box.div.div.find_all('div', {'class':'row'})[1].text
                except:
                    comment_body = "No comment body"

                try:
                    user_name = comment_box.div.div.find_all('div', {'class':'row gHqwa8'})[0].p.text
                except:
                    user_name = "No user name"

                try:
                    location = comment_box.div.div.find_all('div', {'class':'row'})[2].div.find_all('span')[1].text.strip().strip(',')
                except:
                    location = "No location"

                try:
                    review_ago = comment_box.div.div.find_all('div', {'class':'row'})[2].div.find_all('p', {'class':'_2NsDsF'})[1].text
                except:
                    review_ago = "no time"

                review = {
                    'Search Product': search_ele,
                    'Obtained product': obtained_product,
                    'Rating': rating,
                    'Comment Header': comment_header,
                    'Comment Body': comment_body,
                    'Reviewer': user_name,
                    'Location': location,
                    'Review_ago': review_ago
                }

                df.loc[len(df.index)] = list(review.values())
                # print("review saved")

        except Exception as e:
            print("Product error:", e)

    df.to_csv(f"{search_ele}.csv", index=False, header=True)
    print("Table saved")

except Exception as e:
    print("Something went wrong:", e)