from requests import get, post
import json

headers = {
  "Content-Type": "application/json",
  "Accept": "application/json"
}

def search_book(book_title):
  url = f"https://www.googleapis.com/books/v1/volumes?q={book_title}"
  result = get(url, headers=headers)
  # print(result)
  json_result = json.loads(result.content)
  # print(json_result)
  # print(json_result.keys())
  json_result = json_result['items']
  # print(f"data: {json_result}\nlen: {len(json_result)}")

  return json_result

# search_book('El monje que vendio su ferrari')