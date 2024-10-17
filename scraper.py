import requests
from bs4 import BeautifulSoup

def scrape_prose_blogs(username):
    url = f'https://www.theprose.com/Tahmidwrites'  # URL to your profile
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code != 200:
        print("Failed to retrieve the page.")
        return []

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all blog post links (adjust the selector based on the actual HTML structure)
    posts = soup.find_all('a', class_='post-title')  # Update with actual class name

    # Extract titles and links
    blog_links = []
    for post in posts:
        title = post.get_text()
        link = post['href']
        blog_links.append((title, link))

    return blog_links

if __name__ == "__main__":
    username = "Tahmidwrites"  # Replace with your TheProse username
    blogs = scrape_prose_blogs(username)

    # Print or format the blog links for your website
    for title, link in blogs:
        print(f"{title}: {link}")
def save_blogs_to_html(blogs, filename='blogs.html'):
    with open(filename, 'w') as f:
        f.write("<ul>\n")
        for title, link in blogs:
            f.write(f"<li><a href='{link}' target='_blank'>{title}</a></li>\n")
        f.write("</ul>")

if __name__ == "__main__":
    username = "Tahmidwrites"  # Replace with your TheProse username
    blogs = scrape_prose_blogs(username)
    save_blogs_to_html(blogs)

