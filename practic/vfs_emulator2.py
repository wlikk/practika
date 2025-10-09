import tkinter as tk
import sys
import os

class VFSEmulator:
    def __init__(self, vfs_path=None, script_path=None):
        self.root = tk.Tk()
        self.root.title("VFS")
        self.output = tk.Text(self.root)
        self.entry = tk.Entry(self.root)
        self.output.pack()
        self.entry.pack()
        self.entry.bind('<Return>', self.run_cmd)
        
        # Вывод параметров конфигурации
        self.print_output(f"VFS Emulator\nVFS path: {vfs_path or 'None'}\n")
        self.print_output(f"Startup script: {script_path or 'None'}\n")
        
        # Запуск стартового скрипта
        if script_path:
            if os.path.exists(script_path):
                self.print_output(f"Executing startup script: {script_path}\n")
                self.run_script(script_path)
            else:
                self.print_output(f"ERROR: Script not found - {script_path}\n")
        
        self.print_output("$ ")
        
    def print_output(self, text):
        self.output.insert('end', text)
        
    def run_script(self, script_path):
        try:
            with open(script_path, 'r', encoding='utf-8') as f:
                for line_num, line in enumerate(f, 1):
                    cmd = line.strip()
                    # Пропускаем пустые строки и комментарии
                    if cmd and not cmd.startswith('#') and not cmd.startswith('REM'):
                        self.print_output(f"$ {cmd}\n")
                        self.execute_cmd(cmd)
        except Exception as e:
            self.print_output(f"SCRIPT ERROR at line {line_num}: {str(e)}\n")
        
    def execute_cmd(self, cmd_line):
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
            
    def run_cmd(self, event):
        cmd_line = self.entry.get()
        self.entry.delete(0, 'end')
        self.print_output(f"$ {cmd_line}\n")
        self.execute_cmd(cmd_line)
        self.print_output("$ ")

if __name__ == "__main__":
    # Парсинг аргументов командной строки
    vfs_path = sys.argv[1] if len(sys.argv) > 1 else None
    script_path = sys.argv[2] if len(sys.argv) > 2 else None
    
    VFSEmulator(vfs_path, script_path).root.mainloop()