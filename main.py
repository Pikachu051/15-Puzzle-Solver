from pathlib import Path

import time
import webbrowser
import PySimpleGUI as sg #'pip install pysimplegui' first na

def time_pos_set(sec):
    mins = sec // 60
    sec = sec % 60
    hrs = mins // 60
    mins = mins % 60
    if hrs == 0 and mins > 0:
        timelapsed = '%02d:%.2f' % mins, sec
    elif hrs == 0 and mins == 0:
        timelapsed = '%.2f' % sec
    else:
        timelapsed = '%02d:%02d:%02d' % hrs, mins, sec
    return timelapsed

def dna_analyze(raw_dna):
    start_time = time.time()
    #insert dna function here
    end_time = time.time()
    elapsed = end_time - start_time
    elapsed = time_pos_set(elapsed)
    return elapsed

#def export_to_txt(dna, output_folder, time_taken): #trying to convert results to a txt file
    #dna = 


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
        dna_analyze(values["-DNA-"])
        sg.popup_error("Not ready yet") # remove when the function is ready.
    if event == "What is this?":
        webbrowser.open("https://github.com/Pikachu051/DNA-Identity-Analyzer")
window.close()
