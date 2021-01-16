from frame.frame_demo.Main_page import MainPage


class TestMain:
    def test_main(self):
        main = MainPage()
        main.goto_market().goto_search().search()
