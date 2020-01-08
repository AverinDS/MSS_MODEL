from windows.MainWindow import ROUTE_TAG as MAIN_WINDOW_TAG, MainWindow


class Router:
    def go_to_window(self, window_tag):
        if window_tag == MAIN_WINDOW_TAG:
            app = MainWindow()
            app.show()
            return app
        else:
            print("Unknown screen")
