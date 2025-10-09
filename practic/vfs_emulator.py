import tkinter as tk

class VFSEmulator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("VFS")
        self.output = tk.Text(self.root)
        self.entry = tk.Entry(self.root)
        self.output.pack()
        self.entry.pack()
        self.entry.bind('<Return>', self.run_cmd)
        self.print_output("VFS Emulator\n")
        
    def print_output(self, text):
        self.output.insert('end', text)
        
    def run_cmd(self, event):
        cmd_line = self.entry.get()
        self.entry.delete(0, 'end')
        parts = cmd_line.split()
        cmd = parts[0] if parts else ""
        args = parts[1:] if len(parts) > 1 else []
        
        if cmd == "exit":
            self.root.quit()
        elif cmd == "ls":
            self.print_output(f"ls: {args}\n")
        elif cmd == "cd":
            self.print_output(f"cd: {args}\n" if args else "cd: missing arg\n")
        elif cmd:
            self.print_output(f"Error: {cmd} not found\n")
        self.print_output("$ ")

if __name__ == "__main__":
    VFSEmulator().root.mainloop()