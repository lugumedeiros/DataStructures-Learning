def merge_sort(lst):
        """Θ(nlogn), Has recursion"""
        def sort(lst_a, lst_b):
            new_lst = []
            while len(lst_a) >= 1 and len(lst_b) >= 1:
                if lst_a[0] <= lst_b[0]:
                    new_lst.append(lst_a[0])
                    lst_a.pop(0)
                else:
                    new_lst.append(lst_b[0])
                    lst_b.pop(0)
            
            if len(lst_a) > 0:
                return new_lst + lst_a
            else:
                return new_lst + lst_b

        lst_size = len(lst)
        if lst_size == 1:
            return lst
        else:
            lst_a = lst[: lst_size//2]
            lst_b = lst[lst_size//2 :]
            return sort(merge_sort(lst_a), merge_sort(lst_b))
