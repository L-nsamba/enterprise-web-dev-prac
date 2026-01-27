def simple_log_list(my_list):
    while len(my_list) > 1:
        half = len(my_list) // 2
        my_list = my_list[:half]  
        print(f"size : {len(my_list)}")

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
simple_log_list(data)