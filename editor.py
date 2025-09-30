import tkinter as tk
from tkinter import filedialog, messagebox

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Простой Текстовый Редактор")
        self.text_area = tk.Text(self.root, wrap='word', undo=True)
        self.text_area.pack(expand=True, fill='both')
        self.current_file = None
        
        # Меню
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)
        
        self.file_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="Файл", menu=self.file_menu)
        self.file_menu.add_command(label="Открыть", command=self.open_file)
        self.file_menu.add_command(label="Сохранить", command=self.save_file)
        self.file_menu.add_command(label="Сохранить как...", command=self.save_as_file)
        self.file_menu.add_command(label="Выход", command=self.root.quit)

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(tk.END, file.read())
                self.current_file = file_path
                self.root.title(f"Простой Текстовый Редактор - {file_path}")
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось открыть файл: {e}")

    def save_file(self):
        if self.current_file:
            self._save_to_file(self.current_file)
        else:
            self.save_as_file()

    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            self._save_to_file(file_path)
            self.current_file = file_path
            self.root.title(f"Простой Текстовый Редактор - {file_path}")

    def _save_to_file(self, file_path):
        try:
            with open(file_path, 'w') as file:
                file.write(self.text_area.get(1.0, tk.END))
            messagebox.showinfo("Сохранение", "Файл успешно сохранён!")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сохранить файл: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()
