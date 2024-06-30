import readchar
import sys
from typing import Callable

text_color_code = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'reset': '\033[10m'
    }

bg_color_code = {
        'black': '\033[40m',
        'red': '\033[41m',
        'green': '\033[42m',
        'yellow': '\033[43m',
        'blue': '\033[44m',
        'magenta': '\033[45m',
        'cyan': '\033[46m',
        'white': '\033[47m',
        'reset': '\033[10m'
}

txt_color: Callable[[str], str] = lambda c: text_color_code[c]
bgd_color: Callable[[str], str] = lambda c: bg_color_code[c]
reset_code = '\033[0m'

def log_message(message: str, text_color: str | None = None, bg_color: str | None = None, end: str | None = None):
        """Log message with custom colors

        Available color:

        - black
        - red
        - green
        - yellow
        - blue
        - magenta
        - cyan
        - white
        - reset
        
        Arguments: 
        -----------------
            - message: str
                String to print
            - text_color: str
                Color of the text
            - bg_color: str
                Color of the background
            - end: str
                Suffix (value is put on print function)
        """
        if text_color not in text_color_code:
            text_color = 'reset'
        if bg_color not in bg_color_code:
            bg_color = 'reset'
        print(f"{bg_color_code[bg_color]}{text_color_code[text_color]}{message}{reset_code}", end='\n' if end is None else end)

class Menu():
    def __init__(self, options: list[str]) -> None:
        self.selected_index = 0
        self.options = options
        self._n_lines = None
        pass

    def print_menu(self, pad: int = 0):
        longest = 0
        for option in self.options:
            if len(option) > longest:
                longest = len(option)

        longest += pad

        prefix = ""

        for _ in range(pad):
            prefix += " "

        self._n_lines = 0
        for idx, option in enumerate(self.options):
            txt_color = None if idx != self.selected_index else 'white'
            bg_color = None if idx != self.selected_index else "blue"
            log_message(f"{prefix}{option.ljust(longest)}",
                        text_color=txt_color, bg_color=bg_color)
            self._n_lines += 1

        for _ in range(self._n_lines):
            sys.stdout.write("\033[F")

    def __get_choice(self):
        try:
            while True:
                key = readchar.readkey()
                if key == '\x1b[A':
                    return -1
                if key == '\x1b[B':
                    return 1
                if key.lower() == 'q':
                    exit(0)
                if key == '\n':
                    return 2
                return 0
        except KeyboardInterrupt:
            exit(0)

    def run_menu(self, title: str | None = None, get_index: bool = False, help: bool = True) -> str | int:
        if help:
            print("Press Q key or CTRL+C combination to quit\n")
        if title is not None:
            print(title)
        while True:
            self.print_menu()
            input = self.__get_choice()

            if input == 0:
                continue

            if input == 2:
                break
            self.selected_index += input
            self.selected_index = max(0, min(self.selected_index, len(self.options) - 1))

        if self._n_lines is not None:
            for _ in range(self._n_lines):
                sys.stdout.write("\n")

        sys.stdout.write("\n")

        if get_index == True:
            return self.selected_index

        return self.options[self.selected_index]

