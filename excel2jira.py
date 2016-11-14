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
def format_row(row, sep='|'):
	"""Replaces tabs with :sep: and returns string containing new row with
	leading and trailing :sep:, ending with new line character.

	Example: format_row('Name\tAge', sep='|') = '|Name|Age|\n'"""
	row = row.replace('\t', sep)
	return '{s}{r}{s}\n'.format(s=sep, r=row)


def excel_to_jira(text):
	"""Converts an excel table into jira table format."""
	head, rows = split_table(text.strip('\n'))

	head = format_row(head, sep='||')
	rows = map(format_row, rows)
	rows = ''.join(rows)

	return str(head + rows)


def split_table(text, sep='\n'):
	"""Takes a string containing excel table, and returns a list of rows (str)
	from that table."""
	table = text.split(sep)
	if not table:
		return ''
	elif len(table) > 1:
		return table[0], table[1:]
	else:
		return table[0], ''


if __name__ == '__main__':
	app = App()
	app.mainloop()
