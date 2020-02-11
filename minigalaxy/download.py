from typing import List


class Download:
    def __init__(self, url, save_location, finish_func, progress_func=None, cancel_func=None, number=1, out_of_amount=1):
        self.url = url
        self.save_location = save_location
        self.__finish_func = finish_func
        self.__progress_func = progress_func
        self.__cancel_func = cancel_func
        self.number = number
        self.out_of_amount = out_of_amount
        self.done = False

    def set_progress(self, percentage: int) -> None:
        if self.__progress_func:
            if self.out_of_amount > 1:
                # Change the percentage based on which number we are
                progress_start = 100/self.out_of_amount*(self.number-1)
                percentage = progress_start + percentage/self.out_of_amount
            self.__progress_func(percentage)

    def finish(self):
        self.done = True
        self.__finish_func()

    def cancel(self):
        self.done = True
        if self.__cancel_func:
            self.__cancel_func()
