"""
Question:
The API: int read4(char *buf) reads 4 characters at a time from a file.
The return value is the actual number of characters read. For example, it
returns 3 if there is only 3 characters left in the file.
By using the read4 API, implement the function int read(char *buf, int n) that
reads n characters from the file.
Note: The read function will only be called once for each test case.
"""


class Solution:
    def read_n(self, buf, n):
        write = 0

        temp_buf = [None] * 4
        end_reached = False
        while write < n and not end_reached:
            this_size = read4(temp_buf)
            if this_size < 4:
                end_reached = True

            for i in range(this_size):
                buf[write] = temp_buf[i]
                write += 1
                if write == n:
                    break

        return write

