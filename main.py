from tkinter import *
frame_background_color = "light gray"
options_background_color = "light gray"
root_background_color = "light gray"
def main():
    #main window settings
    root = Tk()
    root.title("Parameters Extraction")
    root.configure(background=root_background_color)
    root.geometry("500x700")
    
    #input frame 
    InputFrame = LabelFrame(root, text="Input", font=("Helvetica", 10), background=frame_background_color)
    InputFrame.grid(row=0,column=0)
    #operating frequency
    ParameterFrame = LabelFrame(InputFrame, text="Electrical Parameters", font=("Helvetica", 10), background=options_background_color)
    ParameterFrame.grid(row=0, column=0)
    opFreqLabel = Label(ParameterFrame, text="Op Frequency", font=("Helvetica", 10), background=options_background_color, justify='left')
    opFreqLabel.grid(row=0, column=0, sticky='w')
    chImpedanceLabel = Label(ParameterFrame, text="Ch. Impedance", font=("Helvetica", 10), background=options_background_color, justify='left')
    chImpedanceLabel.grid(row=1, column=0, sticky='w')
    opFreqEntr = Entry(ParameterFrame, font=("Helvetica", 10), width=7, justify="right")
    opFreqEntr.grid(row=0, column=1, sticky='w')
    chImpedanceEntr = Entry(ParameterFrame, font=("Helvetica", 10), width=7, justify="right")
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
    abcdMatrixAEntry = Entry(abcdMatrixFrame, font=("Helvetica", 10), width=7, justify="right")
    abcdMatrixAEntry.grid(row=0, column=1, sticky="w")
    abcdMatrixBEntry = Entry(abcdMatrixFrame, font=("Helvetica", 10), width=7, justify="right")
    abcdMatrixBEntry.grid(row=0, column=3, sticky="e")
    abcdMatrixCEntry = Entry(abcdMatrixFrame, font=("Helvetica", 10), width=7, justify="right")
    abcdMatrixCEntry.grid(row=1, column=1, sticky="w")
    abcdMatrixDEntry = Entry(abcdMatrixFrame, font=("Helvetica", 10), width=7, justify="right")
    abcdMatrixDEntry.grid(row=1, column=3, sticky="e")
    
    root.mainloop()
    
if __name__ == "__main__":
    main()