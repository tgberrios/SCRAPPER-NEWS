import requests

API_KEY = "6a2a80a766184adfb618c1cd32c95734"

def importNews():
    url ="https://newsapi.org/v2/top-headlines"
    params = {
        "apiKey": API_KEY,
        "country": "us"
    }
    response = requests.get(url, params = params)
    
    if response.status_code == 200:
        data = response.json()
        articles = data.get("articles", [])
        return articles
    else:
        print("Error al obtenener noticias: ", response.status_code)
        return None
    

def showNews(articles):
    if articles:
        for idx, article in enumerate(articles,1):
            print(f"{idx}. {article['title']}")
            print(article['description'])
            print(article['url'])
            print()
    else:
        print("No se encontraron noticias.")


def main():
    articles = importNews()
    showNews(articles)


if __name__ == "__main__":
    main()