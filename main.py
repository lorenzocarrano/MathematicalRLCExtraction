from tkinter import *
from math import pi
from utils import matrixProduct
frame_background_color = "light blue"
options_background_color = "light blue"
root_background_color = "light blue"
button_background_color = "white"
entry_width = 16
entry_width_extended = 30
entry_width_reduced = 9
entry_width_short = 3
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
    Y = outputList[9]
    
    paramA = ((1+complex(S11.get()))*(1-complex(S22.get()))+complex(S12.get())*complex(S21.get()))/(2*complex(S21.get()))
    paramB = ((1+complex(S11.get()))*(1+complex(S22.get()))-complex(S12.get())*complex(S21.get()))/(2*complex(S21.get()))
    paramC = ((1-complex(S11.get()))*(1-complex(S22.get()))-complex(S12.get())*complex(S21.get()))/(2*complex(S21.get()))
    paramD = ((1-complex(S11.get()))*(1+complex(S22.get()))+complex(S12.get())*complex(S21.get()))/(2*complex(S21.get()))
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
    A.configure(state="readonly")
    B.configure(state="normal")
    B.delete(0, END) #deletes the current value
    B.insert(0, paramB) #inserts new value assigned by 2nd parameter
    B.configure(state="readonly")
    C.configure(state="normal")
    C.delete(0, END) #deletes the current value
    C.insert(0, paramC) #inserts new value assigned by 2nd parameter
    C.configure(state="readonly")
    D.configure(state="normal")
    D.delete(0, END) #deletes the current value
    D.insert(0, paramD) #inserts new value assigned by 2nd parameter
    D.configure(state="readonly")
    
    #parameters evaluation
    Z = complex(chImped.get())*paramB;
    Inductance = Z.imag/(2*pi*int(opFreq.get()))
    Y.configure(state="normal")
    Y.delete(0, END)
    Y.insert(0, Inductance)
    Y.configure(state="readonly")
    valueY1 = (paramD-1)/Z;
    valueY1Rounded = complex(round(valueY1.real, round_digits), round(valueY1.imag, round_digits))
    Y1.configure(state="normal")
    Y1.delete(0, END)
    Y1.insert(0, valueY1Rounded)
    Y1.configure(state="readonly")
    valueY2 = (paramA-1)/Z;
    valueY2Rounded = complex(round(valueY2.real, round_digits), round(valueY2.imag, round_digits))
    Y2.configure(state="normal")
    Y2.delete(0, END)
    Y2.insert(0, valueY2Rounded)
    Y2.configure(state="readonly")
    commonDen = (2*pi*int(opFreq.get()))
    valueC1 = valueY1.imag/commonDen
    valueC1Rounded = complex(round(valueC1.real, round_digits), round(valueC1.imag, round_digits))
    C1.configure(state="normal")
    C1.delete(0, END)
    C1.insert(0, valueC1)
    C1.configure(state="readonly")
    valueC2 = valueY2.imag/commonDen
    valueC2Rounded = complex(round(valueC2.real, round_digits), round(valueC2.imag, round_digits))
    C2.configure(state="normal")
    C2.delete(0, END)
    C2.insert(0, valueC2)
    C2.configure(state="readonly")
    valueC3 = 1/(Inductance*((2*pi)*int(SRF.get()))*((2*pi)*int(SRF.get())))
    valueC3Rounded = complex(round(valueC3.real, round_digits), round(valueC3.imag, round_digits))
    C3.configure(state="normal")
    C3.delete(0, END)
    C3.insert(0, valueC3)
    C3.configure(state="readonly")
    
    
def reset(inputList, outputList):
    
    for i in range(0, len(inputList)):
        inputList[i].delete(0, END)
    
    for i in range(0, len(outputList)):
        outputList[i].configure(state="normal")
        outputList[i].delete(0, END)
        outputList[i].configure(state="readonly")

#def unknownNetworkDecomposition(mt1, mt2):
def unknownNetworkDecomposition(root, inputList, outputList):
    #Original ABCD frame
    newConfigWindow = Toplevel(root)
    newConfigWindow.configure(background=root_background_color)
    OriginalABCDFrame = LabelFrame(newConfigWindow, text="Original ABCD matrix", font=("Helvetica", 10), background=frame_background_color)
    OriginalABCDFrame.grid(row=0, column=1, sticky='nw')
    #labels
    ABCDmtALabel = Label(OriginalABCDFrame, text="A", font=("Helvetica", 10), background=options_background_color, justify='left')
    ABCDmtALabel.grid(row=0, column=0)
    ABCDmtBLabel = Label(OriginalABCDFrame, text="B", font=("Helvetica", 10), background=options_background_color, justify='left')
    ABCDmtBLabel.grid(row=0, column=2)
    ABCDmtCLabel = Label(OriginalABCDFrame, text="C", font=("Helvetica", 10), background=options_background_color, justify='left')
    ABCDmtCLabel.grid(row=1, column=0)
    ABCDmtDLabel = Label(OriginalABCDFrame, text="D", font=("Helvetica", 10), background=options_background_color, justify='left')
    ABCDmtDLabel.grid(row=1, column=2)
    #parameter entries
    ABCDmtAEntry = Entry(OriginalABCDFrame, font=("Helvetica", 10), width=entry_width, justify="right")
    ABCDmtAEntry.grid(row=0, column=1, sticky="w")
    ABCDmtBEntry = Entry(OriginalABCDFrame, font=("Helvetica", 10), width=entry_width, justify="right")
    ABCDmtBEntry.grid(row=0, column=3, sticky="e")
    ABCDmtCEntry = Entry(OriginalABCDFrame, font=("Helvetica", 10), width=entry_width, justify="right")
    ABCDmtCEntry.grid(row=1, column=1, sticky="w")
    ABCDmtDEntry = Entry(OriginalABCDFrame, font=("Helvetica", 10), width=entry_width, justify="right")
    ABCDmtDEntry.grid(row=1, column=3, sticky="e")
    #Network model selection
    NetworkModelSelectionFrame = LabelFrame(newConfigWindow, text="Network Model Selection", font=("Helvetica", 10), background=frame_background_color)
    NetworkModelSelectionFrame.grid(row=0, column=0, sticky='nw')
    #Selected Model Matrix Frame
    InnerFrame = LabelFrame(NetworkModelSelectionFrame, text="Premult Matrix", font=("Helvetica", 10), background=frame_background_color)
    InnerFrame.grid(row=0, column=1, sticky='ne')
    #labels
    p1Label = Label(InnerFrame, text="", font=("Helvetica", 10), background=options_background_color, justify='left')
    p1Label.grid(row=1, column=0)
    p2Label = Label(InnerFrame, text="Z", font=("Helvetica", 10), background=options_background_color, justify='left')
    p2Label.grid(row=1, column=2)
    p3Label = Label(InnerFrame, text="", font=("Helvetica", 10), background=options_background_color, justify='left')
    p3Label.grid(row=2, column=0)
    p4Label = Label(InnerFrame, text="", font=("Helvetica", 10), background=options_background_color, justify='left')
    p4Label.grid(row=2, column=2)
    
    #parameter entries
    p1Entry = Entry(InnerFrame, font=("Helvetica", 10), width=entry_width_short, justify="right")
    p1Entry.grid(row=1, column=1, sticky="w")
    p1Entry.configure(state="normal")
    p1Entry.insert(0, "1")
    p1Entry.configure(state="readonly")
    p2Entry = Entry(InnerFrame, font=("Helvetica", 10), width=entry_width_short, justify="right")
    p2Entry.grid(row=1, column=3, sticky="e")
    p2Entry.configure(state="normal")
    p3Entry = Entry(InnerFrame, font=("Helvetica", 10), width=entry_width_short, justify="right")
    p3Entry.grid(row=2, column=1, sticky="w")
    p3Entry.configure(state="normal")
    p3Entry.insert(0, "0")
    p3Entry.configure(state="readonly")
    p4Entry = Entry(InnerFrame, font=("Helvetica", 10), width=entry_width_short, justify="right")
    p4Entry.grid(row=2, column=3, sticky="e")
    p4Entry.configure(state="normal")
    p4Entry.insert(0, "1")
    p4Entry.configure(state="readonly")
    #Selected Network Label and Entry
    SelectedNetworkModelLabel = Label(NetworkModelSelectionFrame, text="Selected Model", font=("Helvetica", 10), background=frame_background_color)
    SelectedNetworkModelLabel.grid(row=2, column=0, sticky='w')
    SelectedNetworkModelEntry = Entry(NetworkModelSelectionFrame, font=("Helvetica", 10), width=entry_width_reduced, justify="left")
    SelectedNetworkModelEntry.grid(row=2, column=1)
    SelectedNetworkModelEntry.configure(state="normal")
    SelectedNetworkModelEntry.insert(0, "Pi-Model")
    SelectedNetworkModelEntry.configure(state="readonly")
    
    #Computation of new ABCD matrix frame
    ComputationFrame = LabelFrame(newConfigWindow, text="ABCD' matrix", font=("Helvetica", 10), background=frame_background_color)
    ComputationFrame.grid(row=1, column=1)
    #labels and entries of the ABCD' matrix
    #labels
    ABCDmtALabel_ = Label(ComputationFrame, text="A'", font=("Helvetica", 10), background=options_background_color, justify='left')
    ABCDmtALabel_.grid(row=0, column=0)
    ABCDmtBLabel_ = Label(ComputationFrame, text="B'", font=("Helvetica", 10), background=options_background_color, justify='left')
    ABCDmtBLabel_.grid(row=0, column=2)
    ABCDmtCLabel_ = Label(ComputationFrame, text="C'", font=("Helvetica", 10), background=options_background_color, justify='left')
    ABCDmtCLabel_.grid(row=1, column=0)
    ABCDmtDLabel_ = Label(ComputationFrame, text="D'", font=("Helvetica", 10), background=options_background_color, justify='left')
    ABCDmtDLabel_.grid(row=1, column=2)
    #parameter entries
    ABCDmtAEntry_ = Entry(ComputationFrame, font=("Helvetica", 10), width=entry_width, justify="right")
    ABCDmtAEntry_.grid(row=0, column=1, sticky="w")
    ABCDmtAEntry_.config(state="readonly")
    ABCDmtBEntry_ = Entry(ComputationFrame, font=("Helvetica", 10), width=entry_width, justify="right")
    ABCDmtBEntry_.grid(row=0, column=3, sticky="e")
    ABCDmtBEntry_.config(state="readonly")
    ABCDmtCEntry_ = Entry(ComputationFrame, font=("Helvetica", 10), width=entry_width, justify="right")
    ABCDmtCEntry_.grid(row=1, column=1, sticky="w")
    ABCDmtCEntry_.config(state="readonly")
    ABCDmtDEntry_ = Entry(ComputationFrame, font=("Helvetica", 10), width=entry_width, justify="right")
    ABCDmtDEntry_.grid(row=1, column=3, sticky="e")
    ABCDmtDEntry_.config(state="readonly")
    
    #evaluation of original ABCD parameters
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
    Y = outputList[9]
    
    paramA = ((1+complex(S11.get()))*(1-complex(S22.get()))+complex(S12.get())*complex(S21.get()))/(2*complex(S21.get()))
    paramB = ((1+complex(S11.get()))*(1+complex(S22.get()))-complex(S12.get())*complex(S21.get()))/(2*complex(S21.get()))
    paramC = ((1-complex(S11.get()))*(1-complex(S22.get()))-complex(S12.get())*complex(S21.get()))/(2*complex(S21.get()))
    paramD = ((1-complex(S11.get()))*(1+complex(S22.get()))+complex(S12.get())*complex(S21.get()))/(2*complex(S21.get()))
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
    ABCDmtAEntry.configure(state="normal")
    ABCDmtAEntry.delete(0, END) #deletes the current value
    ABCDmtAEntry.insert(0, paramA) #inserts new value assigned by 2nd parameter
    ABCDmtAEntry.configure(state="readonly")
    ABCDmtBEntry.configure(state="normal")
    ABCDmtBEntry.delete(0, END) #deletes the current value
    ABCDmtBEntry.insert(0, paramB) #inserts new value assigned by 2nd parameter
    ABCDmtBEntry.configure(state="readonly")
    ABCDmtCEntry.configure(state="normal")
    ABCDmtCEntry.delete(0, END) #deletes the current value
    ABCDmtCEntry.insert(0, paramC) #inserts new value assigned by 2nd parameter
    ABCDmtCEntry.configure(state="readonly")
    ABCDmtDEntry.configure(state="normal")
    ABCDmtDEntry.delete(0, END) #deletes the current value
    ABCDmtDEntry.insert(0, paramD) #inserts new value assigned by 2nd parameter
    ABCDmtDEntry.configure(state="readonly")        
    
    #Equivalent Pi-Model
    #output frame
    OutputFrame = LabelFrame(newConfigWindow, text="Equivalent Pi-Model", font=("Helvetica", 10), background=frame_background_color)
    OutputFrame.grid(row=0,column=2)
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
    YLabel = Label(OutputParameterFrame, text="Y", font=("Helvetica", 10), background=options_background_color, justify='left')
    YLabel.grid(row=5, column=0, sticky='w')
    C1Entry = Entry(OutputParameterFrame, font=("Helvetica", 10), width=entry_width_extended, justify="right", state="readonly")
    C1Entry.grid(row=0, column=1, sticky="w")
    C2Entry = Entry(OutputParameterFrame, font=("Helvetica", 10), width=entry_width_extended, justify="right", state="readonly")
    C2Entry.grid(row=1, column=1, sticky="w")
    C3Entry = Entry(OutputParameterFrame, font=("Helvetica", 10), width=entry_width_extended, justify="right", state="readonly")
    C3Entry.grid(row=2, column=1, sticky="w")
    Y1Entry = Entry(OutputParameterFrame, font=("Helvetica", 10), width=entry_width_extended, justify="right", state="readonly")
    Y1Entry.grid(row=3, column=1, sticky="w")
    Y2Entry = Entry(OutputParameterFrame, font=("Helvetica", 10), width=entry_width_extended, justify="right", state="readonly")
    Y2Entry.grid(row=4, column=1, sticky="w")
    YEntry = Entry(OutputParameterFrame, font=("Helvetica", 10), width=entry_width_extended, justify="right", state="readonly")
    YEntry.grid(row=5, column=1, sticky="w")
    
    #lists declaration
    changeModelParametersList = [SelectedNetworkModelEntry, p1Label, p2Label, p3Label, p4Label, p1Entry, p2Entry, p3Entry, p4Entry]
    inputEntriesList = [p1Entry, p2Entry, p3Entry, p4Entry, ABCDmtAEntry, ABCDmtBEntry, ABCDmtCEntry, ABCDmtDEntry]
    outputEntriesList = [ABCDmtAEntry_, ABCDmtBEntry_, ABCDmtCEntry_, ABCDmtDEntry_, C1Entry, C2Entry, C3Entry, Y1Entry, Y2Entry, YEntry]
    #Selection Buttons
    piModelButton = Button(NetworkModelSelectionFrame, text="Pi-Model", font=("Helvetica", 10), background=button_background_color, command=lambda:NetworkModelSelection("P", changeModelParametersList))
    TModelButton = Button(NetworkModelSelectionFrame, text="T-Model", font=("Helvetica", 10), background=button_background_color, command=lambda:NetworkModelSelection("T", changeModelParametersList))
    piModelButton.grid(row=3, column=0)
    TModelButton.grid(row=3, column=1)
    #Compute Button
    EvaluateModifiedABCDMatrix = Button(newConfigWindow, text="Calculate", font=("Helvetica", 10), background=button_background_color, command=lambda:EvaluateABCD_(inputList, inputEntriesList, outputEntriesList, SelectedNetworkModelEntry.get()))
    EvaluateModifiedABCDMatrix.grid(row=1, column=0)
    
def EvaluateABCD_(inputParameters, inputEntriesList, outputEntriesList, selection):
    if selection == "Pi-Model":
        if len(inputEntriesList[1].get()) == 0:
            return
    elif selection == "T-Model":
        if len(inputEntriesList[2].get()) == 0:
            return
            
    m1 = [complex(inputEntriesList[0].get()), complex(inputEntriesList[1].get()), complex(inputEntriesList[2].get()), complex(inputEntriesList[3].get())]
    m2 = [complex(inputEntriesList[4].get()), complex(inputEntriesList[5].get()), complex(inputEntriesList[6].get()), complex(inputEntriesList[7].get())]
    if selection == "Pi-Model":
        m1[1] = -1 * m1[1]
    elif selection == "T-Model":
        m1[2] = -1 * m1[2]
    
    res = matrixProduct(m1, m2)
    
    for i in range(0, 4):
        outputEntriesList[i].configure(state="normal")
        outputEntriesList[i].delete(0, END)
        outputEntriesList[i].insert(0, res[i])
        outputEntriesList[i].configure(state="readonly")
        
    evalPiModelUnknownNetwork(inputParameters, res, outputEntriesList)

def evalPiModelUnknownNetwork(inputParams, ABCDParams_, outputEntriesList):
    paramA = ABCDParams_[0]
    paramB = ABCDParams_[1]
    paramC = ABCDParams_[2]
    paramD = ABCDParams_[3]
    opFreq = inputParams[0]
    chImped = inputParams[1]
    SRF = inputParams[2]
    C1 = outputEntriesList[4]
    C2 = outputEntriesList[5]
    C3 = outputEntriesList[6]
    Y1 = outputEntriesList[7]
    Y2 = outputEntriesList[8]
    Y = outputEntriesList[9]
    #parameters evaluation
    Z = complex(chImped.get())*paramB;
    Inductance = Z.imag/(2*pi*int(opFreq.get()))
    Y.configure(state="normal")
    Y.delete(0, END)
    Y.insert(0, Inductance)
    Y.configure(state="readonly")
    valueY1 = (paramD-1)/Z;
    valueY1Rounded = complex(round(valueY1.real, round_digits), round(valueY1.imag, round_digits))
    Y1.configure(state="normal")
    Y1.delete(0, END)
    Y1.insert(0, valueY1Rounded)
    Y1.configure(state="readonly")
    valueY2 = (paramA-1)/Z;
    valueY2Rounded = complex(round(valueY2.real, round_digits), round(valueY2.imag, round_digits))
    Y2.configure(state="normal")
    Y2.delete(0, END)
    Y2.insert(0, valueY2Rounded)
    Y2.configure(state="readonly")
    commonDen = (2*pi*int(opFreq.get()))
    valueC1 = valueY1.imag/commonDen
    valueC1Rounded = complex(round(valueC1.real, round_digits), round(valueC1.imag, round_digits))
    C1.configure(state="normal")
    C1.delete(0, END)
    C1.insert(0, valueC1)
    C1.configure(state="readonly")
    valueC2 = valueY2.imag/commonDen
    valueC2Rounded = complex(round(valueC2.real, round_digits), round(valueC2.imag, round_digits))
    C2.configure(state="normal")
    C2.delete(0, END)
    C2.insert(0, valueC2)
    C2.configure(state="readonly")
    valueC3 = 1/(Inductance*((2*pi)*int(SRF.get()))*((2*pi)*int(SRF.get())))
    valueC3Rounded = complex(round(valueC3.real, round_digits), round(valueC3.imag, round_digits))
    C3.configure(state="normal")
    C3.delete(0, END)
    C3.insert(0, valueC3)
    C3.configure(state="readonly")

def NetworkModelSelection(selection, parametersList):
    if selection == 'P':
        #Update selected network entry
        parametersList[0].configure(state="normal")
        parametersList[0].delete(0, END)
        parametersList[0].insert(0, "Pi-Model")
        parametersList[0].configure(state="readonly")
        #Change matrix configuration
        parametersList[1].configure(text="")
        parametersList[2].configure(text="Z")
        parametersList[3].configure(text="")
        parametersList[4].configure(text="")
        parametersList[5].configure(state="normal")
        parametersList[5].delete(0,END)
        parametersList[5].insert(0,"1")
        parametersList[5].configure(state="readonly")
        parametersList[6].configure(state="normal")
        parametersList[6].delete(0, END)
        parametersList[7].configure(state="normal")
        parametersList[7].delete(0,END)
        parametersList[7].insert(0,"0")
        parametersList[7].configure(state="readonly")
        parametersList[8].configure(state="normal")
        parametersList[8].delete(0,END)
        parametersList[8].insert(0,"1")
        parametersList[8].configure(state="readonly")      
        
    elif selection == 'T':
        #Update selected network entry
        parametersList[0].configure(state="normal")
        parametersList[0].delete(0, END)
        parametersList[0].insert(0, "T-Model")
        parametersList[0].configure(state="readonly")
        #Change matrix configuration
        parametersList[1].configure(text="")
        parametersList[2].configure(text="")
        parametersList[3].configure(text="Y")
        parametersList[4].configure(text="")
        parametersList[5].configure(state="normal")
        parametersList[5].delete(0,END)
        parametersList[5].insert(0,"1")
        parametersList[5].configure(state="readonly")
        parametersList[6].configure(state="normal")
        parametersList[6].delete(0, END)
        parametersList[6].insert(0, "0")
        parametersList[6].configure(state="readonly")
        parametersList[7].configure(state="normal")
        parametersList[7].delete(0,END)
        parametersList[8].configure(state="normal")
        parametersList[8].delete(0,END)
        parametersList[8].insert(0,"1")
        parametersList[8].configure(state="readonly")
    
    else:
        pass

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
    OutputParameterFrame = LabelFrame(OutputFrame, text="Parasitic Parameters and Equivalent Inductance", font=("Helvetica", 10), background=options_background_color)
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
    YLabel = Label(OutputParameterFrame, text="Y", font=("Helvetica", 10), background=options_background_color, justify='left')
    YLabel.grid(row=5, column=0, sticky='w')
    C1Entry = Entry(OutputParameterFrame, font=("Helvetica", 10), width=entry_width_extended, justify="right", state="readonly")
    C1Entry.grid(row=0, column=1, sticky="w")
    C2Entry = Entry(OutputParameterFrame, font=("Helvetica", 10), width=entry_width_extended, justify="right", state="readonly")
    C2Entry.grid(row=1, column=1, sticky="w")
    C3Entry = Entry(OutputParameterFrame, font=("Helvetica", 10), width=entry_width_extended, justify="right", state="readonly")
    C3Entry.grid(row=2, column=1, sticky="w")
    Y1Entry = Entry(OutputParameterFrame, font=("Helvetica", 10), width=entry_width_extended, justify="right", state="readonly")
    Y1Entry.grid(row=3, column=1, sticky="w")
    Y2Entry = Entry(OutputParameterFrame, font=("Helvetica", 10), width=entry_width_extended, justify="right", state="readonly")
    Y2Entry.grid(row=4, column=1, sticky="w")
    YEntry = Entry(OutputParameterFrame, font=("Helvetica", 10), width=entry_width_extended, justify="right", state="readonly")
    YEntry.grid(row=5, column=1, sticky="w")
    
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
    abcdMatrixAEntry = Entry(abcdMatrixFrame, font=("Helvetica", 10), width=entry_width, justify="right", state="readonly")
    abcdMatrixAEntry.grid(row=0, column=1, sticky="w")
    abcdMatrixBEntry = Entry(abcdMatrixFrame, font=("Helvetica", 10), width=entry_width, justify="right", state="readonly")
    abcdMatrixBEntry.grid(row=0, column=3, sticky="e")
    abcdMatrixCEntry = Entry(abcdMatrixFrame, font=("Helvetica", 10), width=entry_width, justify="right", state="readonly")
    abcdMatrixCEntry.grid(row=1, column=1, sticky="w")
    abcdMatrixDEntry = Entry(abcdMatrixFrame, font=("Helvetica", 10), width=entry_width, justify="right", state="readonly")
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
    outputParameters = [abcdMatrixAEntry, abcdMatrixBEntry, abcdMatrixCEntry, abcdMatrixDEntry, C1Entry, C2Entry, C3Entry, Y1Entry, Y2Entry, YEntry]
    
    #calculation button
    calculateBtn = Button(root, text="Extraction", font=("Helvetica", 10), background=button_background_color, command=lambda:parametersExtraction(inputParameters, outputParameters))
    calculateBtn.grid(row=3, column=0, sticky="w")
    #reset button
    resetBtn = Button(root, text="Reset", font=("Helvetica", 10), background=button_background_color, command=lambda:reset(inputParameters, outputParameters))
    resetBtn.grid(row=4, column=0)
    #unknown network decomposition button
    UnknownNetworkDecompBtn = Button(root, text="Unknown Network", font=("Helvetica", 10), background=button_background_color, command=lambda: unknownNetworkDecomposition(root, inputParameters, outputParameters))
    UnknownNetworkDecompBtn.grid(row=3, column=1, sticky='w')
    root.bind('<Return>', lambda eff: parametersExtraction(inputParameters, outputParameters))
    
    root.mainloop()
    
if __name__ == "__main__":
    main()
