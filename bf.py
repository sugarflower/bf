import sys

class BF:
    def __init__(self, code=None):

        self.funcs = {
            "<": self.pdec,
            ">": self.pinc,
            "+": self.inc,
            "-": self.dec,
            ".": self.out,
            ",": self.inp,
            "[": self.wst,
            "]": self.wend
            }

    def reset(self):
        self.mem = [0,] * 0x1f
        self.cp = 0
        self.mp = 0
        self.code = ""

    def exec(self, code):
        self.reset()
        self.code = code

        while self.cp < len(self.code):
            c = self.code[self.cp]
            if c in self.funcs.keys():
                self.funcs[c]()
            self.cp = self.cp + 1
            #print(self.mem)

    def pinc(self):
        self.mp = (self.mp + 1) % len(self.mem)

    def pdec(self):
        self.mp = (self.mp - 1) % len(self.mem)

    def inc(self):
        self.mem[self.mp] = (self.mem[self.mp] + 1) % 0xff

    def dec(self):
        self.mem[self.mp] = (self.mem[self.mp] - 1) % 0xff

    def out(self):
        print(chr(self.mem[self.mp]), end="")

    def inp(self):
        a = ord(sys.stdin.read(1))
        self.mem[self.mp] = a

    def wst(self):
        if self.mem[self.mp] == 0:
            depth = 0
            while True:
                self.cp = (self.cp + 1) % len(self.code)
                if self.code[self.cp] == "[":
                    depth += 1
                if self.code[self.cp] == "]":
                    if depth == 0:
                        break
                    else:
                        depth -= 1

    def wend(self):
        if self.mem[self.mp] != 0:
            depth = 0
            while True:
                self.cp = (self.cp - 1) % len(self.code)
                if self.code[self.cp] == "]":
                    depth += 1
                if self.code[self.cp] == "[":
                    if depth == 0:
                        break
                    else:
                        depth -= 1


code = """
++++++++++[>+++++++>++++++++++>+++++++++++>+++>+++++++++>
+<<<<<<-]>++.>+.>--..+++.>++.>---.<<.+++.------.<-.>>+.>>.
"""

bf = BF()
bf.exec(code)
