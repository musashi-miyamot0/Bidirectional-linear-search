import threading

res = None


class TwoTheardSearch:

    def __init__(self, massive: list = None, true_num: int = None):
        self.massive = massive
        self.true_num = true_num
        self.__flag_lock = False

    def __check_none_var(self):
        if self.massive is None or self.true_num is None:
            return False
        return True

    def __left_search(
        self,
    ):

        for num in self.massive:
            if self.__flag_lock:
                return
            elif not self.__flag_lock:
                if num == self.true_num:
                    global res
                    self.__flag_lock = True
                    res = num
                continue

    def __right_search(
        self,
    ):
        __copy_massive: list = self.massive.copy().reverse()

        for num in self.massive:
            if self.__flag_lock:
                return
            elif not self.__flag_lock:
                if num == self.true_num:
                    global res
                    self.__flag_lock = True
                    res = num
                continue

    def enter_point(self):
        if self.__check_none_var():
            t1 = threading.Thread(target=self.__left_search, name="th-left")
            t2 = threading.Thread(target=self.__right_search, name="th-right")
            t1.start()
            t2.start()
            t1.join()
            t2.join()
        elif not self.__check_none_var():
            return


isinstance_search = TwoTheardSearch(list(range(100000000)), true_num=0)
isinstance_search.enter_point()
print(res)
