import requests

ACCESS_TOKEN = "여기에_티스토리_access_token"
BLOG_NAME = "블로그주소"

title = "자동 포스팅 테스트"

content = """
<h1>자동 포스팅 테스트</h1>
<p>GitHub Actions로 자동 포스팅 테스트입니다.</p>
"""

url = "https://www.tistory.com/apis/post/write"

params = {
    "access_token": ACCESS_TOKEN,
    "output": "json",
    "blogName": BLOG_NAME,
    "title": title,
    "content": content,
    "visibility": 3
}

response = requests.post(url, params=params)

print(response.text)
