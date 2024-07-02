from __future__ import annotations
from typing import List, Tuple


class Token:
    def __init__(self, fmt: str, text: str):
        self.fmt = fmt
        self.text = text
    
    def __len__(self):
        return len(self.text)

class Sentence:
    def __init__(self):
        self.data: List[Token] = []
    
    def addf(self, fmt: str, text: str):
        self.data.append(Token(fmt, text))
        return self
    
    def addt(self, text: str):
        self.data.append(Token("", text))
        return self

    def adds(self, fmt, sentence):
        for _, t in sentence.data:
            self.data.append(Token(fmt, t))
        return self
    
    def concat(self, sentence: Sentence):
        self.data += sentence.data
        return self
    
    def ljust(self, width: int, fillchar: str = " ", fmt = ""):
        total = self.len()
        if total < width:
            self.addt(fillchar * (width - total))
        return self
    
    def rjust(self, width: int, fillchar: str = " ", fmt = ""):
        total = self.len()
        if total < width:
            self.data = [Token("", fillchar * (width - total))] + self.data
        return self
    
    def center(self, width: int, fillchar: str = " ", fmt = ""):
        total = self.len()
        if total < width:
            left = (width - total) // 2
            right = width - total - left
            self.data = [Token("", fillchar * left)] + self.data + [Token("", fillchar * right)]
        return self
    
    def len(self):
        total = 0
        for t in self.data:
            total += len(t.text)
        return total
    
    def get(self):
        return self.data
