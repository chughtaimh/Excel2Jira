import pyperclip
import Tkinter as Tk 
import ttk



class App(ttk.Frame):

	def __init__(self, master=None):
		ttk.Frame.__init__(self, master)
		self.pack()

		self.master.title('Excel2Jira')
		self.master.resizable(width=False, height=False)

		style = ttk.Style()
		style.configure('TButton', font=('Serif', 10), bg="#ccc", fg='blue', 
			width=50, height=2, padding=20)
		style.configure('TLabel', font=('Serif', 10), justify='right', height=2,
			padding=20)
		style.configure('TEntry', font=('Serif', 10), justify='right', height=2, 
			padding=20, wraplength=200)

		self.label = ttk.Label(self, text="PASTE EXCEL TABLE BELOW")
		self.label.grid(column=0, row=0)

		self.text = Tk.StringVar()
		self.entry = Tk.Text(self, width=50, height=5)
		self.entry.grid(column=0, row=1)

		self.button = ttk.Button(self, text='COPY JIRA TABLE TO CLIPBOARD',
			command=self.copy_to_clipboard)
		self.button.grid(column=0, row=2)

	def copy_to_clipboard(self):
		text = self.entry.get("1.0", "end")
		jira_table = excel_to_jira(text)

		# Copy to clipboard
		pyperclip.copy(jira_table)

		# Set button text to "Copied!"
		self.button.config(text='Copied!')


# Helpers
def headers(text):
    header = text.split('\n')[0]
    header_columns = header.split('\t')
    return '||' + '||'.join(header_columns) + '||\n'


def columns(text):
    text = text.strip('\n')             # remove any leading/trailing \n chars
    non_headers = text.split('\n')[1:]  # split text by \n chars, take [1:]
    rtn = '|'                           # new string that will be returned
    for row in non_headers:
        for column in row.split('\t'):  # column values are separated by tabs
            rtn += column + '|'
        rtn += '\n|'
    return rtn.rstrip('|')              # rtn everything but the trailing "|"


def excel_to_jira(text):
    return str(headers(text) + columns(text))


if __name__ == '__main__':
    app = App()
    app.mainloop()
