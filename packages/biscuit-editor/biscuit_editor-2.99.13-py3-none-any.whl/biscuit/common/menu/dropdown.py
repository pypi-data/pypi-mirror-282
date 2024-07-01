import tkinter as tk
from turtle import width

from ..codicon import get_codicon
from ..ui.icons import IconButton
from ..ui.native import Frame
from .menu import Menu


class _DropdownMenu(Menu):
    def get_coords(self, e) -> tuple:
        return (
            self.master.winfo_rootx(),
            self.master.winfo_rooty() + self.master.winfo_height(),
        )


class Dropdown(Frame):
    """For implementing a dropdown menu."""

    def __init__(
        self,
        master,
        selected: str = None,
        items: list = None,
        icon=None,
        callback=lambda *_: None,
        iconside=tk.LEFT,
        padx=5,
        pady=1,
        fg=None,
        bg=None,
        hfg=None,
        hbg=None,
        *args,
        **kwargs
    ) -> None:
        super().__init__(master, padx=padx, pady=pady, *args, **kwargs)
        self.callback = callback

        self.bg, self.fg, self.hbg, self.hfg = (
            self.base.theme.utils.iconlabelbutton.values()
        )
        if fg:
            self.fg = fg
        if bg:
            self.bg = bg
        if hfg:
            self.hfg = hfg
        if hbg:
            self.hbg = hbg

        self.config(bg=self.bg)
        self.text = selected
        self.icon = icon

        self.icon_label = None
        self.text_label = None

        self.selected = None
        self.menu = _DropdownMenu(self)
        for i in items:
            self.add_command(i)

        if icon:
            self.icon_label = tk.Label(
                self,
                text=get_codicon(self.icon),
                anchor=tk.CENTER,
                bg=self.bg,
                fg=self.fg,
                font=("codicon", 12),
            )
            self.icon_label.pack(side=iconside, fill=tk.BOTH)

        if selected:
            self.text_label = tk.Label(
                self,
                text=self.text,
                anchor=tk.CENTER,
                pady=2,
                bg=self.bg,
                fg=self.fg,
                font=("Segoe UI", 10),
            )
            self.text_label.pack(side=iconside, fill=tk.BOTH, expand=True)

        self.close_btn = IconButton(self, "chevron-down", self.menu.show)
        self.close_btn.config(bg=self.bg, fg=self.fg)
        self.close_btn.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.config_bindings()
        self.visible = False

    def add_command(self, text) -> None:
        """Add a command to the dropdown menu"""

        self.menu.add_command(text, lambda: self.choose(text))

    def set_items(self, items: list[str]) -> None:
        self.menu.clear()
        for i in items:
            self.add_command(i)

    def config_bindings(self) -> None:
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

        self.bind("<Button-1>", self.menu.show)
        if self.text:
            self.text_label.bind("<Button-1>", self.menu.show)
        if self.icon:
            self.icon_label.bind("<Button-1>", self.menu.show)

    def on_enter(self, *_) -> None:
        self.config(bg=self.hbg)
        if self.text:
            self.text_label.config(bg=self.hbg, fg=self.hfg)
        if self.icon:
            self.icon_label.config(bg=self.hbg, fg=self.hfg)
        self.close_btn.config(bg=self.hbg, fg=self.hfg)

    def on_leave(self, *_) -> None:
        self.config(bg=self.bg)
        if self.text:
            self.text_label.config(bg=self.bg, fg=self.fg)
        if self.icon:
            self.icon_label.config(bg=self.bg, fg=self.fg)
        self.close_btn.config(bg=self.bg, fg=self.fg)

    def change_text(self, text) -> None:
        """Change the text of the item"""

        self.text_label.config(text=text)

    def change_icon(self, icon) -> None:
        """Change the icon of the item"""

        self.icon_label.config(text=icon)

    def set_pack_data(self, **kwargs) -> None:
        self.pack_data = kwargs

    def get_pack_data(self):
        return self.pack_data

    def choose(self, text) -> None:
        """Choose an item from the dropdown menu"""

        self.selected = text
        self.text_label.config(text=text)
        self.callback(text)

    def show(self) -> None:
        """Show the item"""

        if not self.visible:
            self.visible = True
            self.pack(**self.get_pack_data())

    def hide(self) -> None:
        """Hide the item"""

        if self.visible:
            self.visible = False
            self.pack_forget()
