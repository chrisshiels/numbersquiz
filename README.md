# numbersquiz

    host$ # https://www.youtube.com/watch?v=_JQYYz92-Uk
    host$ ./numbersquiz.py 25 50 75 100 1 10 813
    [75, '-', 10, '*', 25, '+', 1, '*', 50, '/', 100]


    host$ # https://www.youtube.com/watch?v=z_GpTDPQDS8
    host$ ./numbersquiz.py 100 1 3 10 4 2 975
    [100, '+', 1, '-', 4, '*', 10, '+', 3, '+', 2]
    [100, '+', 1, '-', 4, '*', 10, '+', 2, '+', 3]
    [100, '-', 3, '*', 10, '-', 1, '+', 4, '+', 2]
    [100, '-', 3, '*', 10, '-', 1, '+', 2, '+', 4]
    ...


    host$ # https://www.youtube.com/watch?v=3h2G7gA3AE4
    host$ ./numbersquiz.py 25 3 7 10 1 8 649
    [25, '*', 10, '-', 7, '/', 3, '*', 8, '+', 1]
    [25, '*', 10, '-', 7, '*', 8, '/', 3, '+', 1]
    [25, '-', 1, '*', 3, '+', 10, '*', 8, '-', 7]
    [7, '*', 10, '+', 8, '*', 25, '/', 3, '-', 1]
    ...