from tkinter import *
from math import pi
frame_background_color = "light gray"
options_background_color = "light gray"
root_background_color = "light gray"
entry_width = 16
round_digits = 5

def parametersExtraction(inputList, outputList):
    
    opFreq = inputList[0]
    chImped = inputList[1]
    SRF = inputList[2]
    S11 = inputList[3]
    S12 = inputList[4]
    S21 = inputList[5]
    S22 = inputList[6]
    
    A = outputList[0]
    B = outputList[1]
    C = outputList[2]
    D = outputList[3]
    C1 = outputList[4]
    C2 = outputList[5]
    C3 = outputList[6]
    Y1 = outputList[7]
    Y2 = outputList[8]
    
    paramA = ((1+complex(S11.get()))*(1-complex(S22.get()))+complex(S12.get())*complex(S21.get()))/(2*complex(S21.get()));
    paramB = ((1+complex(S11.get()))*(1+complex(S22.get()))-complex(S12.get())*complex(S21.get()))/(2*complex(S21.get()));
    paramC = ((1-complex(S11.get()))*(1-complex(S22.get()))-complex(S12.get())*complex(S21.get()))/(2*complex(S21.get()));
    paramD = ((1-complex(S11.get()))*(1+complex(S22.get()))+complex(S12.get())*complex(S21.get()))/(2*complex(S21.get()));
    #rounding results
    paramArealRounded = round(paramA.real, round_digits)
    paramAimagRounded = round(paramA.imag, round_digits)
    paramA = complex(paramArealRounded, paramAimagRounded)
    paramBrealRounded = round(paramB.real, round_digits)
    paramBimagRounded = round(paramB.imag, round_digits)
    paramB = complex(paramBrealRounded, paramBimagRounded)
    paramCrealRounded = round(paramC.real, round_digits)
    paramCimagRounded = round(paramC.imag, round_digits)
    paramC = complex(paramCrealRounded, paramCimagRounded)
    paramDrealRounded = round(paramD.real, round_digits)
    paramDimagRounded = round(paramD.imag, round_digits)
    paramD = complex(paramDrealRounded, paramDimagRounded)
    
    #ABCD parameters update
    A.configure(state="normal")
    A.delete(0, END) #deletes the current value
    A.insert(0, paramA) #inserts new value assigned by 2nd parameter
    A.configure(state="disabled")
    B.configure(state="normal")
    B.delete(0, END) #deletes the current value
    B.insert(0, paramB) #inserts new value assigned by 2nd parameter
    B.configure(state="disabled")
    C.configure(state="normal")
    C.delete(0, END) #deletes the current value
    C.insert(0, paramC) #inserts new value assigned by 2nd parameter
    C.configure(state="disabled")
    D.configure(state="normal")
    D.delete(0, END) #deletes the current value
    D.insert(0, paramD) #inserts new value assigned by 2nd parameter
    D.configure(state="disabled")
    
    #parameters evaluation
    Z = complex(chImped.get())*paramB;
    Inductance = Z.imag/(2*pi*int(opFreq.get()))
    
    valueY1 = (paramD-1)/Z;
    valueY1Rounded = complex(round(valueY1.real, round_digits), round(valueY1.imag, round_digits))
    Y1.configure(state="normal")
    Y1.delete(0, END)
    Y1.insert(0, valueY1Rounded)
    Y1.configure(state="disabled")
    valueY2 = (paramA-1)/Z;
    valueY2Rounded = complex(round(valueY2.real, round_digits), round(valueY2.imag, round_digits))
    Y2.configure(state="normal")
    Y2.delete(0, END)
    Y2.insert(0, valueY2Rounded)
    Y2.configure(state="disabled")
    commonDen = (2*pi*int(opFreq.get()))
    valueC1 = valueY1.imag/commonDen
    valueC1Rounded = complex(round(valueC1.real, round_digits), round(valueC1.imag, round_digits))
    C1.configure(state="normal")
    C1.delete(0, END)
    C1.insert(0, valueC1Rounded)
    C1.configure(state="normal")
    valueC2 = valueY2.imag/commonDen
    valueC2Rounded = complex(round(valueC2.real, round_digits), round(valueC2.imag, round_digits))
    C2.configure(state="normal")
    C2.delete(0, END)
    C2.insert(0, valueC2Rounded)
    C2.configure(state="normal")
    valueC3 = 1/(Inductance*((2*pi)*int(SRF.get()))*((2*pi)*int(SRF.get())))
    valueC3Rounded = complex(round(valueC3.real, round_digits), round(valueC3.imag, round_digits))
    C3.configure(state="normal")
    C3.delete(0, END)
    C3.insert(0, valueC3Rounded)
    C3.configure(state="normal")
    
    
def reset(inputList, outputList):
    
    for i in range(0, len(inputList)):
        inputList[i].delete(0, END)
    
    for i in range(0, len(outputList)):
        outputList[i].configure(state="normal")
        outputList[i].delete(0, END)
        outputList[i].configure(state="disabled")

def main():
    #main window settings
    root = Tk()
    root.title("Parameters Extraction")
    root.configure(background=root_background_color)
    #root.geometry("500x700")
    
    #input frame 
    InputFrame = LabelFrame(root, text="Input", font=("Helvetica", 10), background=frame_background_color)
    InputFrame.grid(row=0,column=0, sticky="n")
    InputParameterFrame = LabelFrame(InputFrame, text="Electrical Parameters", font=("Helvetica", 10), background=options_background_color)
    InputParameterFrame.grid(row=0, column=0, sticky="w")
    opFreqLabel = Label(InputParameterFrame, text="Op Frequency", font=("Helvetica", 10), background=options_background_color, justify='left')
    opFreqLabel.grid(row=0, column=0, sticky='w')
    chImpedanceLabel = Label(InputParameterFrame, text="Ch. Impedance", font=("Helvetica", 10), background=options_background_color, justify='left')
    chImpedanceLabel.grid(row=1, column=0, sticky='w')
    SRFLabel = Label(InputParameterFrame, text="SRF", font=("Helvetica", 10), background=options_background_color, justify='left')
    SRFLabel.grid(row=2, column=0, sticky='w')
    opFreqEntr = Entry(InputParameterFrame, font=("Helvetica", 10), width=entry_width, justify="right")
    opFreqEntr.grid(row=0, column=1, sticky='w')
    chImpedanceEntr = Entry(InputParameterFrame, font=("Helvetica", 10), width=entry_width, justify="right")
    chImpedanceEntr.grid(row=1, column=1, sticky='w')
    SRFEntr = Entry(InputParameterFrame, font=("Helvetica", 10), width=entry_width, justify="right")
    SRFEntr.grid(row=2, column=1, sticky='w')
    #scattering matrix
    #labels
    scatteringMatrixFrame = LabelFrame(InputFrame, text="Scattering Matrix", font=("Helvetica", 10), background=options_background_color)
    scatteringMatrixFrame.grid(row=1, column=0)
    scatteringMatrixS11Label = Label(scatteringMatrixFrame, text="S11", font=("Helvetica", 10), background=options_background_color, justify='left')
    scatteringMatrixS11Label.grid(row=0, column=0)
    scatteringMatrixS12Label = Label(scatteringMatrixFrame, text="S12", font=("Helvetica", 10), background=options_background_color, justify='left')
    scatteringMatrixS12Label.grid(row=0, column=2)
    scatteringMatrixS21Label = Label(scatteringMatrixFrame, text="S21", font=("Helvetica", 10), background=options_background_color, justify='left')
    scatteringMatrixS21Label.grid(row=1, column=0)
    scatteringMatrixS22Label = Label(scatteringMatrixFrame, text="S22", font=("Helvetica", 10), background=options_background_color, justify='left')
    scatteringMatrixS22Label.grid(row=1, column=2)
    #parameter entries
    scatteringMatrixS11Entry = Entry(scatteringMatrixFrame, font=("Helvetica", 10), width=entry_width, justify="right")
    scatteringMatrixS11Entry.grid(row=0, column=1, sticky="w")
    scatteringMatrixS12Entry = Entry(scatteringMatrixFrame, font=("Helvetica", 10), width=entry_width, justify="right")
    scatteringMatrixS12Entry.grid(row=0, column=3, sticky="e")
    scatteringMatrixS21Entry = Entry(scatteringMatrixFrame, font=("Helvetica", 10), width=entry_width, justify="right")
    scatteringMatrixS21Entry.grid(row=1, column=1, sticky="w")
    scatteringMatrixS22Entry = Entry(scatteringMatrixFrame, font=("Helvetica", 10), width=entry_width, justify="right")
    scatteringMatrixS22Entry.grid(row=1, column=3, sticky="e")
    
    #output frame
    OutputFrame = LabelFrame(root, text="Output", font=("Helvetica", 10), background=frame_background_color)
    OutputFrame.grid(row=0,column=1)
    OutputParameterFrame = LabelFrame(OutputFrame, text="Components", font=("Helvetica", 10), background=options_background_color)
    OutputParameterFrame.grid(row=0, column=0, sticky="w")
    C1Label = Label(OutputParameterFrame, text="C1", font=("Helvetica", 10), background=options_background_color, justify='left')
    C1Label.grid(row=0, column=0, sticky='w')
    C2Label = Label(OutputParameterFrame, text="C2", font=("Helvetica", 10), background=options_background_color, justify='left')
    C2Label.grid(row=1, column=0, sticky='w')
    C3Label = Label(OutputParameterFrame, text="C3", font=("Helvetica", 10), background=options_background_color, justify='left')
    C3Label.grid(row=2, column=0, sticky='w')
    Y1Label = Label(OutputParameterFrame, text="Y1", font=("Helvetica", 10), background=options_background_color, justify='left')
    Y1Label.grid(row=3, column=0, sticky='w')
    Y2Label = Label(OutputParameterFrame, text="Y2", font=("Helvetica", 10), background=options_background_color, justify='left')
    Y2Label.grid(row=4, column=0, sticky='w')
    C1Entry = Entry(OutputParameterFrame, font=("Helvetica", 10), width=entry_width, justify="right", state="disabled")
    C1Entry.grid(row=0, column=1, sticky="w")
    C2Entry = Entry(OutputParameterFrame, font=("Helvetica", 10), width=entry_width, justify="right", state="disabled")
    C2Entry.grid(row=1, column=1, sticky="w")
    C3Entry = Entry(OutputParameterFrame, font=("Helvetica", 10), width=entry_width, justify="right", state="disabled")
    C3Entry.grid(row=2, column=1, sticky="w")
    Y1Entry = Entry(OutputParameterFrame, font=("Helvetica", 10), width=entry_width, justify="right", state="disabled")
    Y1Entry.grid(row=3, column=1, sticky="w")
    Y2Entry = Entry(OutputParameterFrame, font=("Helvetica", 10), width=entry_width, justify="right", state="disabled")
    Y2Entry.grid(row=4, column=1, sticky="w")
    
    #ABCD matrix
    #labels    
    abcdMatrixFrame = LabelFrame(OutputFrame, text="ABCD Matrix", font=("Helvetica", 10), background=options_background_color)
    abcdMatrixFrame.grid(row=1, column=0)
    abcdMatrixALabel = Label(abcdMatrixFrame, text="A", font=("Helvetica", 10), background=options_background_color, justify='left')
    abcdMatrixALabel.grid(row=0, column=0)
    abcdMatrixBLabel = Label(abcdMatrixFrame, text="B", font=("Helvetica", 10), background=options_background_color, justify='left')
    abcdMatrixBLabel.grid(row=0, column=2)
    abcdMatrixCLabel = Label(abcdMatrixFrame, text="C", font=("Helvetica", 10), background=options_background_color, justify='left')
    abcdMatrixCLabel.grid(row=1, column=0)
    abcdMatrixDLabel = Label(abcdMatrixFrame, text="D", font=("Helvetica", 10), background=options_background_color, justify='left')
    abcdMatrixDLabel.grid(row=1, column=2)
    #parameter entries
    abcdMatrixAEntry = Entry(abcdMatrixFrame, font=("Helvetica", 10), width=entry_width, justify="right", state="disabled")
    abcdMatrixAEntry.grid(row=0, column=1, sticky="w")
    abcdMatrixBEntry = Entry(abcdMatrixFrame, font=("Helvetica", 10), width=entry_width, justify="right", state="disabled")
    abcdMatrixBEntry.grid(row=0, column=3, sticky="e")
    abcdMatrixCEntry = Entry(abcdMatrixFrame, font=("Helvetica", 10), width=entry_width, justify="right", state="disabled")
    abcdMatrixCEntry.grid(row=1, column=1, sticky="w")
    abcdMatrixDEntry = Entry(abcdMatrixFrame, font=("Helvetica", 10), width=entry_width, justify="right", state="disabled")
    abcdMatrixDEntry.grid(row=1, column=3, sticky="e")
    
    #precharging default values in entries
    chImpedanceEntr.insert(0, "50")
    opFreqEntr.insert(0, "200000000")
    SRFEntr.insert(0, "3350000000")
    scatteringMatrixS11Entry.insert(0, "(0.0246+0.1411j)")
    scatteringMatrixS12Entry.insert(0, "(0.9751-0.1644j)")
    scatteringMatrixS21Entry.insert(0, "(0.9751-0.1644j)")
    scatteringMatrixS22Entry.insert(0, "(0.0246+0.1411j)")
    
    #packaging of input and output parameters
    inputParameters = [opFreqEntr, chImpedanceEntr, SRFEntr, scatteringMatrixS11Entry, scatteringMatrixS12Entry, scatteringMatrixS21Entry, scatteringMatrixS22Entry]
    outputParameters = [abcdMatrixAEntry, abcdMatrixBEntry, abcdMatrixCEntry, abcdMatrixDEntry, C1Entry, C2Entry, C3Entry, Y1Entry, Y2Entry]
    
    #calculation button
    calculateBtn = Button(root, text="Extraction", font=("Helvetica", 10), background="light gray", command=lambda:parametersExtraction(inputParameters, outputParameters))
    calculateBtn.grid(row=2, column=0)
    #reset button
    resetBtn = Button(root, text="Reset", font=("Helvetica", 10), background="light gray", command=lambda:reset(inputParameters, outputParameters))
    resetBtn.grid(row=2, column=1)
    
    root.mainloop()
    
if __name__ == "__main__":
    main()