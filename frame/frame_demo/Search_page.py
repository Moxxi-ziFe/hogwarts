from frame.frame_demo.Base_page import BasePage


class SearchPage(BasePage):
    def search(self):
        self.parse_yaml('./search.yml', 'search')
