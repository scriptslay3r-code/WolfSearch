import wolframalpha as wolf
from tkinter import * 




### Functions ###
def close():
	window.quit()

def wolf_search():
	search_text = input_txt.get()
	Label(window, text = "Search Results for: " + "\"" + search_text + "\"" ).pack(side="top")
	results_box = Text(window)
	
	res = client.query(search_text)
	answer = next(res.results).text
	print(res)
	print(answer)
	#everything = "This is res: " + res + "This is answer: " + answer
	results_box.insert('end', answer)
	results_box.pack(side = 'bottom')
	
### Variables ###
'''
	##Fonts & Widget Variables ## 
'''
header_font = ("Helvetica", 25)
text_font = ("Helvetica",15)
root = Tk()
window = Frame(root)
search_label= Label(window, text = "Search Here", font = header_font)
input_txt = Entry(window, font = text_font)
exit_button = Button(window, text = "Exit", command = close)
search_button = Button(window, text = "Search", command = wolf_search)
'''
	## WolframVariables ##
'''
app_id = 'REQ623-2JW2ET9K77'
client = wolf.Client(app_id)

### Page Design ###
root.title("Search with Wolfram")
window.pack()
search_label.pack()
input_txt.pack()
search_button.pack(side = "left")
exit_button.pack(side = "right")

root.mainloop()

