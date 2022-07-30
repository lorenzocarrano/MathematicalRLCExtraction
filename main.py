from tkinter import *
frame_background_color = "light gray"
options_background_color = "light gray"
root_background_color = "light gray"

def parametersExtraction():
    
    return 0
def main():
    #main window settings
    root = Tk()
    root.title("Parameters Extraction")
    root.configure(background=root_background_color)
    #root.geometry("500x700")
    
    #input frame 
    InputFrame = LabelFrame(root, text="Input", font=("Helvetica", 10), background=frame_background_color)
    InputFrame.grid(row=0,column=0, sticky="n")
    #operating frequency
    InputParameterFrame = LabelFrame(InputFrame, text="Electrical Parameters", font=("Helvetica", 10), background=options_background_color)
    InputParameterFrame.grid(row=0, column=0)
    opFreqLabel = Label(InputParameterFrame, text="Op Frequency", font=("Helvetica", 10), background=options_background_color, justify='left')
    opFreqLabel.grid(row=0, column=0, sticky='w')
    chImpedanceLabel = Label(InputParameterFrame, text="Ch. Impedance", font=("Helvetica", 10), background=options_background_color, justify='left')
    chImpedanceLabel.grid(row=1, column=0, sticky='w')
    opFreqEntr = Entry(InputParameterFrame, font=("Helvetica", 10), width=7, justify="right")
    opFreqEntr.grid(row=0, column=1, sticky='w')
    chImpedanceEntr = Entry(InputParameterFrame, font=("Helvetica", 10), width=7, justify="right")
    chImpedanceEntr.grid(row=1, column=1, sticky='w')
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
    scatteringMatrixS11Entry = Entry(scatteringMatrixFrame, font=("Helvetica", 10), width=7, justify="right")
    scatteringMatrixS11Entry.grid(row=0, column=1, sticky="w")
    scatteringMatrixS12Entry = Entry(scatteringMatrixFrame, font=("Helvetica", 10), width=7, justify="right")
    scatteringMatrixS12Entry.grid(row=0, column=3, sticky="e")
    scatteringMatrixS21Entry = Entry(scatteringMatrixFrame, font=("Helvetica", 10), width=7, justify="right")
    scatteringMatrixS21Entry.grid(row=1, column=1, sticky="w")
    scatteringMatrixS22Entry = Entry(scatteringMatrixFrame, font=("Helvetica", 10), width=7, justify="right")
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
    C1Entry = Entry(OutputParameterFrame, font=("Helvetica", 10), width=7, justify="right", state="disabled")
    C1Entry.grid(row=0, column=1, sticky="w")
    C2Entry = Entry(OutputParameterFrame, font=("Helvetica", 10), width=7, justify="right", state="disabled")
    C2Entry.grid(row=1, column=1, sticky="w")
    C3Entry = Entry(OutputParameterFrame, font=("Helvetica", 10), width=7, justify="right", state="disabled")
    C3Entry.grid(row=2, column=1, sticky="w")
    Y1Entry = Entry(OutputParameterFrame, font=("Helvetica", 10), width=7, justify="right", state="disabled")
    Y1Entry.grid(row=3, column=1, sticky="w")
    Y2Entry = Entry(OutputParameterFrame, font=("Helvetica", 10), width=7, justify="right", state="disabled")
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
    abcdMatrixAEntry = Entry(abcdMatrixFrame, font=("Helvetica", 10), width=7, justify="right", state="disabled")
    abcdMatrixAEntry.grid(row=0, column=1, sticky="w")
    abcdMatrixBEntry = Entry(abcdMatrixFrame, font=("Helvetica", 10), width=7, justify="right", state="disabled")
    abcdMatrixBEntry.grid(row=0, column=3, sticky="e")
    abcdMatrixCEntry = Entry(abcdMatrixFrame, font=("Helvetica", 10), width=7, justify="right", state="disabled")
    abcdMatrixCEntry.grid(row=1, column=1, sticky="w")
    abcdMatrixDEntry = Entry(abcdMatrixFrame, font=("Helvetica", 10), width=7, justify="right", state="disabled")
    abcdMatrixDEntry.grid(row=1, column=3, sticky="e")
    
    calculateBtn = Button(root, text="Extraction", font=("Helvetica", 10), background="light gray", command=lambda:parametersExtraction())
    calculateBtn.grid(row=2, column=0)
    
    root.mainloop()
    
if __name__ == "__main__":
    main()