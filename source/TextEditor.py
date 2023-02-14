import math
from tkinter import font
from tkinter.font import Font

from MsgLibrary import MsgLibrary


class TextEditor:

    @staticmethod
    def get_file_name_from_path(path):
        return path[path.rfind("/") + 1:]

    @staticmethod
    def write_file_loaded_msg(file_name, lbl):
        txt = MsgLibrary.file_loaded_msg_first_part() + file_name
        txt_font = Font(font=lbl.cget("font"))
        window_width = lbl.master.winfo_width()
        txt = TextEditor.truncate_as_far_as_necessary_or_possible_to_fit_in_window(txt, txt_font, window_width)
        return txt

    @staticmethod
    def truncate_as_far_as_necessary_or_possible_to_fit_in_window(txt, txt_font, window_width):
        while not TextEditor.text_would_fit_in_window(txt, txt_font, window_width) and\
                TextEditor.can_be_truncated_further(txt):
            txt = TextEditor.truncate(txt)
        return txt

    @staticmethod
    def can_be_truncated_further(txt):
        truncatable = TextEditor.get_truncatable_part(txt)
        truncated = TextEditor.truncate(truncatable)
        return len(truncatable) > len(truncated)

    @staticmethod
    def get_truncatable_part(txt):
        if MsgLibrary.file_loaded_msg_first_part() in txt:
            return txt[len(MsgLibrary.file_loaded_msg_first_part()):]
        else:
            return txt

    @staticmethod
    def resize_text(window_width, lbl):
        txt = lbl.cget("text")
        txt_font = font.nametofont(lbl.cget("font"))
        txt = TextEditor.truncate_as_far_as_necessary_or_possible_to_fit_in_window(txt, txt_font, window_width)
        lbl.config(text=txt)

    @staticmethod
    def text_would_fit_in_window(txt, txt_font, window_width):
        text_width = txt_font.measure(txt)
        return text_width + 2 < window_width

    @staticmethod
    def halve(s):
        i = len(s)
        if i % 2 == 0:
            return s[0:i//2], s[i//2:]
        return s[0:(i//2+1)], s[(i//2+1):]

    @staticmethod
    def truncate(s):
        halves = TextEditor.halve(s)
        dots = " ... "
        half_dots_len = math.ceil(len(dots)/2.0)
        return halves[0][:-half_dots_len] + dots + halves[1][half_dots_len:]
        # TODO: if filename is truncated, make it responsively less truncated as user increases window size
