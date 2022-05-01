import wolfsearch
from tkinter import * 

### Functions ###
def search():
	search_text = input_txt.get()
	print(search_text)
	Label(window, text = "Search Results for: " + "\"" + search_text + "\"" ).pack()
	results_box = Text(window)
	results_box.insert('end', search_text)
	results_box.pack(side = 'bottom')
	#text = wolframsearch.search.answer()
def close():
	window.quit()
	#wolfsearch.search(test)	
	
### Variables ###
##Fonts & Widgets ##
header_font = ("Helvetica", 25)
text_font = ("Helvetica",15)
root = Tk()
window = Frame(root)
search_label= Label(window, text = "Search Here", font = header_font)
input_txt = Entry(window, font = text_font)
exit_button = Button(window, text = "Exit", command = close)
search_button = Button(window, text = "Search", command = search)

### Page Design ###
root.title("Search with Wolfram")
window.pack()
search_label.pack()
input_txt.pack()
search_button.pack(side = "left")
exit_button.pack(side = "right")

root.mainloop()

