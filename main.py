import tkinter as tk
from tkinter import filedialog, messagebox

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Текстовый редактор")
        self.text_area = tk.Text(root, wrap='word')
        self.text_area.pack(expand=True, fill='both')
        self.filename = None

        self.menu = tk.Menu(root)
        self.root.config(menu=self.menu)

        file_menu = tk.Menu(self.menu, tearoff=0)
        file_menu.add_command(label="Создать", command=self.new_file)
        file_menu.add_command(label="Открыть", command=self.open_file)
        file_menu.add_command(label="Сохранить", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Выход", command=self.exit_app)

        settings_menu = tk.Menu(self.menu, tearoff=0)
        settings_menu.add_command(label="Настроить размер окна", command=self.set_window_size)

        self.menu.add_cascade(label="Файл", menu=file_menu)
        self.menu.add_cascade(label="Настройки", menu=settings_menu)

    def new_file(self):
        self.filename = None
        self.text_area.delete(1.0, tk.END)

    def open_file(self):
        try:
            file_path = filedialog.askopenfilename(defaultextension=".txt",
                                                   filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")])
            if file_path:
                with open(file_path, "r", encoding="utf-8") as file:
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(1.0, file.read())
                self.filename = file_path
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось открыть файл: {e}")

    def save_file(self):
        try:
            if self.filename:
                with open(self.filename, "w", encoding="utf-8") as file:
                    file.write(self.text_area.get(1.0, tk.END))
            else:
                self.filename = filedialog.asksaveasfilename(defaultextension=".txt",
                                                             filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")])
                if self.filename:
                    with open(self.filename, "w", encoding="utf-8") as file:
                        file.write(self.text_area.get(1.0, tk.END))
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сохранить файл: {e}")

    def exit_app(self):
        self.root.quit()

    def set_window_size(self):
        try:
            size_window = tk.Toplevel(self.root)
            size_window.title("Настройка размеров окна")
            size_window.geometry("350x200")

            tk.Label(size_window, text="Ширина:").pack(pady=5)
            width_entry = tk.Entry(size_window)
            width_entry.pack()

            tk.Label(size_window, text="Высота:").pack(pady=5)
            height_entry = tk.Entry(size_window)
            height_entry.pack()

            def apply_size():
                try:
                    width = int(width_entry.get())
                    height = int(height_entry.get())

                    if width <= 0 or height <= 0:
                        raise ValueError("размеры окна должны быть больше 0 :(")

                    self.root.geometry(f"{width}x{height}")
                    size_window.destroy()
                except ValueError as e:
                    messagebox.showerror("Ошибка", f"Некорректный ввод: {e}")

            tk.Button(size_window, text="Применить", command=apply_size).pack(pady=10)
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось изменить размеры окна: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditor(root)
    root.mainloop()
