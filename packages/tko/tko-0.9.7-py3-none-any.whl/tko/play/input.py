from .frame import Frame
from ..util.sentence import Sentence
from .fmt import Fmt
import time

class Input:
    def __init__(self):
        self.frame = Frame(0, 0)
        self.content = Sentence()
        self.ending = 0
        self.total_time = 0
        self.type = ""

    def set_header(self, text: Sentence, align: str = ''):
        self.frame.set_header(text, align)
        return self

    def __setup_frame(self):
        lines, cols = Fmt.get_size()
        dx = self.content.len() + 2
        dy = 3
        x = (cols - dx) // 2
        y = (lines - dy) // 2
        self.frame.set_pos(y, x).set_inner(dy, dx)
        self.frame.set_fill()
        if self.type == "timer":
            delta = dx - 4
            percent = (self.ending - time.time()) / self.total_time
            footer = (delta - int(delta * percent)) * "─" + int(delta * percent) * "━"
            self.frame.set_footer(Sentence().addt(footer), "^")



    def timer(self, content: str, delta: int):
        self.type = "timer"
        self.content = Sentence().addt(content)
        self.frame.set_border_rounded()
        self.frame.set_header(Sentence().addf("/", " Aviso "))
        self.enable = True
        self.total_time = delta
        self.ending = time.time() + delta

        return self

    def warning(self, content: str):
        self.type = "warning"
        self.content = Sentence().addt(content)
        self.frame.set_border_bold()
        self.frame.set_header(Sentence().addf("/", " Aviso "))
        self.frame.set_footer(Sentence().addf("/", " Apente enter "))
        self.enable = True
        return self
        
    def draw(self):
        self.__setup_frame()
        self.frame.draw()
        self.frame.write(1, 1, self.content)
        time.sleep(0.1)
        Fmt.refresh()

    def get_input(self):
        self.draw()
        key = Fmt.getch()
        if key == ord('\n'):
            self.enable = False
        if self.ending - time.time() < 0:
            self.enable = False
        return key
            


        