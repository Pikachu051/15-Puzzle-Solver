import PySimpleGUI as sg
import webbrowser

# - - - GUI Layout - - - #
layout = [
    [sg.Text("Input DNA data:"), sg.Input(key="-DNA-"), sg.Button("What is this?")],
    [sg.Button("Analyze")],
    [sg.Exit()],
]

window = sg.Window("DNA ID Analyzer", layout)

while True:
    event, values = window.read()
    print(event, values)
    if event in (sg.WINDOW_CLOSED, "Exit"):
        break
    if event == "Analyze":
        #dna_analyze() function here <<<<<---------
        sg.popup_error("Not ready yet") # remove when the function is ready.
    if event == "What is this?":
        webbrowser.open("https://github.com/Pikachu051/DNA-Identity-Analyzer")
window.close()
