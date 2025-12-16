import tkinter as tk
import tkinter.messagebox as msg


class Todo(tk.Tk):
    def __init__(self, tasks=None):
        super().__init__()

        # 1) Window title = LastName-ToDo ---
        self.title("Moracchini-ToDo")
        self.geometry("300x400")

        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks

        # --- Scrolling layout (from Listing 2.2) ---
        self.tasks_canvas = tk.Canvas(self)
        self.tasks_frame = tk.Frame(self.tasks_canvas)
        self.text_frame = tk.Frame(self)

        self.scrollbar = tk.Scrollbar(
            self.tasks_canvas, orient="vertical", command=self.tasks_canvas.yview
        )
        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)

        self.tasks_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas_frame = self.tasks_canvas.create_window(
            (0, 0), window=self.tasks_frame, anchor="n"
        )

        # --- Task entry box ---
        self.task_create = tk.Text(self.text_frame, height=3, bg="white", fg="black")
        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.text_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_create.focus_set()

        # --- Requirement: instructions in label for deleting ---
        todo1 = tk.Label(
            self.tasks_frame,
            text="--- Add Items Here ---\nRight-click a task to delete it.",
            bg="lightgrey",
            fg="black",
            pady=10,
            justify="center",
        )
        self._bind_delete(todo1)

        self.tasks.append(todo1)
        for task in self.tasks:
            task.pack(side=tk.TOP, fill=tk.X)

        # --- Binds from Listing 2.2 ---
        self.bind("<Return>", self.add_task)
        self.bind("<Configure>", self.on_frame_configure)
        self.bind_all("<MouseWheel>", self.mouse_scroll)  # Windows/macOS
        self.bind_all("<Button-4>", self.mouse_scroll)    # Linux
        self.bind_all("<Button-5>", self.mouse_scroll)    # Linux
        self.tasks_canvas.bind("<Configure>", self.task_width)

        # Alternate task colors (from Listing 2.2)
        self.colour_schemes = [
            {"bg": "lightblue", "fg": "blue"},
            {"bg": "blue", "fg": "white"},
        ]

        # --- Requirement: File -> Exit menu + colored menu items ---
        # (Menu pattern shown in the book)  [oai_citation:1‡Tkinter-By-Example.pdf](sediment://file_00000000537c722fa15eca8d005d0190)
        menu_bg = "#1B4F72"   # deep blue
        menu_fg = "#FAD7A0"   # soft orange (complementary)

        self.menubar = tk.Menu(self, bg=menu_bg, fg=menu_fg)
        self.file_menu = tk.Menu(self.menubar, tearoff=0, bg=menu_bg, fg=menu_fg)
        self.file_menu.add_command(label="Exit", command=self.exit_app)
        self.menubar.add_cascade(label="File", menu=self.file_menu)
        self.config(menu=self.menubar)

    # --- Requirement: Exit ends program cleanly ---
    def exit_app(self):
        self.quit()
        self.destroy()

    # --- Requirement: right-click deletes (not left-click) ---
    def _bind_delete(self, label_widget: tk.Label):
        # Windows/Linux right-click is usually Button-3.
        # Some macOS trackpad “two-finger click” may come through as Button-2.
        label_widget.bind("<Button-3>", self.remove_task)
        label_widget.bind("<Button-2>", self.remove_task)

    def add_task(self, event=None):
        task_text = self.task_create.get(1.0, tk.END).strip()

        if len(task_text) > 0:
            new_task = tk.Label(self.tasks_frame, text=task_text, pady=10)
            self.set_task_colour(len(self.tasks), new_task)

            self._bind_delete(new_task)
            new_task.pack(side=tk.TOP, fill=tk.X)

            self.tasks.append(new_task)

        self.task_create.delete(1.0, tk.END)

    def remove_task(self, event):
        task = event.widget
        if msg.askyesno("Really Delete?", "Delete " + task.cget("text") + "?"):
            if task in self.tasks:
                self.tasks.remove(task)
            task.destroy()
            self.recolour_tasks()

    def recolour_tasks(self):
        for index, task in enumerate(self.tasks):
            self.set_task_colour(index, task)

    def set_task_colour(self, position, task):
        _, task_style_choice = divmod(position, 2)
        my_scheme_choice = self.colour_schemes[task_style_choice]
        task.configure(bg=my_scheme_choice["bg"])
        task.configure(fg=my_scheme_choice["fg"])

    def on_frame_configure(self, event=None):
        self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox("all"))

    def task_width(self, event):
        canvas_width = event.width
        self.tasks_canvas.itemconfig(self.canvas_frame, width=canvas_width)

    def mouse_scroll(self, event):
        if event.delta:
            self.tasks_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        else:
            move = 1 if event.num == 5 else -1
            self.tasks_canvas.yview_scroll(move, "units")


if __name__ == "__main__":
    todo = Todo()
    todo.mainloop()