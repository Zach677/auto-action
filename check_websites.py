import requests
from datetime import datetime

def check_website_status(name, url):
    try:
        response = requests.get(url, timeout=30, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
            'Reference': url,
        })
        return response.status_code == 200
    except Exception as e:
        print(f"Error checking {name}: {e}")
        return False

def update_readme(name, status):
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status_text = "没关门" if status else "关门了"
    big_head = f"# 今天{name}关门了吗\n\n"
    content = f"{big_head}{current_datetime} {status_text}\n\n"

    with open('README.md', 'a') as readme_file:
        readme_file.write(content)

if __name__ == "__main__":
    websites = [("腾讯", "https://www.qq.com"),
                ("微博", "https://weibo.com"),
                ("谷歌", "https://www.google.com")]

    # 清空 README.md 文件
    open('README.md', 'w').close()

    for name, url in websites:
        status = check_website_status(name, url)
        update_readme(name, status)