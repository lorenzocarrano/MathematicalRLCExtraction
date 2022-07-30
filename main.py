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
    opFreqLabel = Label(InputFrame, text="Op Frequency", font=("Helvetica", 10), background=options_background_color, justify='left')
    opFreqLabel.grid(row=0, column=0)
    opFreqEntr = Entry(InputFrame, font=("Helvetica", 10), width=7, justify="right")
    opFreqEntr.grid(row=0, column=1)
    #scattering matrix
    #labels
    scatteringMatrixLabel = Label(InputFrame, text="Scattering Matrix", font=("Helvetica", 10), background=options_background_color, justify='left')
    scatteringMatrixLabel.grid(row=1, column=0)
    scatteringMatrixS11Label = Label(InputFrame, text="S11", font=("Helvetica", 10), background=options_background_color, justify='left')
    scatteringMatrixS11Label.grid(row=2, column=0)
    scatteringMatrixS12Label = Label(InputFrame, text="S12", font=("Helvetica", 10), background=options_background_color, justify='left')
    scatteringMatrixS12Label.grid(row=2, column=2)
    scatteringMatrixS21Label = Label(InputFrame, text="S21", font=("Helvetica", 10), background=options_background_color, justify='left')
    scatteringMatrixS21Label.grid(row=3, column=0)
    scatteringMatrixS22Label = Label(InputFrame, text="S22", font=("Helvetica", 10), background=options_background_color, justify='left')
    scatteringMatrixS22Label.grid(row=3, column=2)
    #parameter entries
    scatteringMatrixS11Entry = Entry(InputFrame, font=("Helvetica", 10), width=7, justify="right")
    scatteringMatrixS11Entry.grid(row=2, column=1, sticky="w")
    scatteringMatrixS12Entry = Entry(InputFrame, font=("Helvetica", 10), width=7, justify="right")
    scatteringMatrixS12Entry.grid(row=2, column=3, sticky="e")
    scatteringMatrixS21Entry = Entry(InputFrame, font=("Helvetica", 10), width=7, justify="right")
    scatteringMatrixS21Entry.grid(row=3, column=1, sticky="w")
    scatteringMatrixS22Entry = Entry(InputFrame, font=("Helvetica", 10), width=7, justify="right")
    scatteringMatrixS22Entry.grid(row=3, column=3, sticky="e")
    
    root.mainloop()
    
if __name__ == "__main__":
    main()