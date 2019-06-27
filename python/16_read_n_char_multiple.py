"""
Question:
Similar to Question [15. Read N Characters Given Read4], but the read function
may be called multiple times.
"""
import collections


class Solution:
    def read_n_char_multiple(self):
        pass

    def __init__(self):
        self.queue = collections.deque()
        self.eof = False

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """

        idx = 0

        while n > 0:
            if len(self.queue) < 4 and len(self.queue) < n and not self.eof:
                tmp_buff = [""] * 4
                read_byte = read4(tmp_buff)
                if read_byte < 4:
                    self.eof = True

                for i in range(read_byte):
                    self.queue.append(tmp_buff[i])

            for i in range(min(n, 4, len(self.queue))):
                buf[idx] = self.queue.popleft()
                idx += 1
                n -= 1

            if self.eof and len(self.queue) == 0:
                return idx

        return idx
