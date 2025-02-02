class UrlManager:
    """
    url管理器
    """

    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):
        if url is None or len(url) == 0:
            return
        if url in self.new_urls or url in self.old_urls:
            return
        self.new_urls.add(url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return

        for url in urls:
            self.add_new_url(url)

    def get_url(self):
        if self.has_new_url():
            url = self.new_urls.pop()
            self.old_urls.add(url)
            return url
        else:
            return None

    def has_new_url(self):
        return len(self.new_urls) > 0


if __name__ == "__main__":
    url_manager = UrlManager()
# 第一次调用
    url_manager.add_new_url("url1")
    # set()集合自己有去重功能!
    url_manager.add_new_urls(["url1", "url2"])
    print(url_manager.new_urls, url_manager.old_urls)
# 第二次调用
    print("*" * 30)
    new_url1 = url_manager.get_url()
    print(new_url1, url_manager.new_urls, url_manager.old_urls)
# 第三次调用
    print("*" * 30)
    new_url2 = url_manager.get_url()
    print(new_url2, url_manager.new_urls, url_manager.old_urls)

    print("*" * 30)
    print(url_manager.has_new_url())
