import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

app = tk.Tk()

style = ttk.Style()

#START SCREEN
app.title("SMART DOCTOR")
canvas = tk.Canvas(app, width=600, height=300)
canvas.grid(columnspan=3, rowspan=4)

#POSSIBLE HEALTH ISSUES
a1 = "Active Virus/Bacteria in System"
s1 = "Mild Hypothermia"
s2 = "Flu / Common Cold"
l1 = "Low Body Temperature"
h1 = "High Body Temperature"
e1 = "Lack of Exercise"
n1 = "Lack of Nutrition"
d1 = "Sleep Deprivation"

#DICTIONARY FOR POSSIBLE HEALTH ISSUES RESPONSE
Response_Dictionary = {
    ("32-34(Celsius)", "Fine", "Yes", "Yes", "Yes"): l1,
    ("32-34(Celsius)", "Fine", "Yes", "Yes", "No"): l1+" , "+d1,
    ("32-34(Celsius)", "Fine", "Yes", "No", "Yes"): l1+" , "+n1,
    ("32-34(Celsius)", "Fine", "Yes", "No", "No"): l1+" , "+n1+" , "+d1,
    ("32-34(Celsius)", "Fine", "No", "No", "No"): l1+" , "+e1+" , "+d1+" , "+n1,
    ("32-34(Celsius)", "Fine", "No", "Yes", "No"): l1+" , "+e1+" , "+d1,
    ("32-34(Celsius)", "Fine", "No", "No", "Yes"): l1+" , "+e1+" , "+n1,
    ("32-34(Celsius)", "Fine", "No", "Yes", "Yes"): l1+" , "+e1,
    ("32-34(Celsius)", "Sick", "Yes", "Yes", "Yes"): s1,
    ("32-34(Celsius)", "Sick", "Yes", "Yes", "No"): s1+" , "+d1,
    ("32-34(Celsius)", "Sick", "Yes", "No", "Yes"): s1+" , "+n1,
    ("32-34(Celsius)", "Sick", "Yes", "No", "No"): s1+" , "+n1+" , "+d1,
    ("32-34(Celsius)", "Sick", "No", "No", "No"): s1+" , "+e1+" , "+n1+" , "+d1,
    ("32-34(Celsius)", "Sick", "No", "Yes", "No"): s1+" , "+e1+" , "+d1,
    ("32-34(Celsius)", "Sick", "No", "No", "Yes"): s1+" , "+e1+" , "+n1,
    ("32-34(Celsius)", "Sick", "No", "Yes", "Yes"): s1+" , "+e1,

    ("35-37(Celsius)", "Fine", "Yes", "Yes", "No"): d1,
    ("35-37(Celsius)", "Fine", "Yes", "No", "Yes"): n1,
    ("35-37(Celsius)", "Fine", "Yes", "No", "No"): n1+" , "+d1,
    ("35-37(Celsius)", "Fine", "No", "No", "No"): e1+" , "+n1+" , "+d1,
    ("35-37(Celsius)", "Fine", "No", "Yes", "No"): e1+" , "+d1,
    ("35-37(Celsius)", "Fine", "No", "No", "Yes"): e1+" , "+n1,
    ("35-37(Celsius)", "Fine", "No", "Yes", "Yes"): e1,
    ("35-37(Celsius)", "Sick", "Yes", "Yes", "Yes"): a1,
    ("35-37(Celsius)", "Sick", "Yes", "Yes", "No"): a1+" , "+d1,
    ("35-37(Celsius)", "Sick", "Yes", "No", "Yes"): a1+" , "+n1,
    ("35-37(Celsius)", "Sick", "Yes", "No", "No"): a1+" , "+n1+" , "+d1,
    ("35-37(Celsius)", "Sick", "No", "No", "No"): a1+" , "+e1+" , "+n1+" , "+d1,
    ("35-37(Celsius)", "Sick", "No", "Yes", "No"): a1+" , "+e1+" , "+d1,
    ("35-37(Celsius)", "Sick", "No", "No", "Yes"): a1+" , "+e1+" , "+n1,
    ("35-37(Celsius)", "Sick", "No", "Yes", "Yes"): a1+" , "+e1,

    ("38-40(Celsius)", "Fine", "Yes", "Yes", "Yes"): h1,
    ("38-40(Celsius)", "Fine", "Yes", "Yes", "No"): h1+" , "+d1,
    ("38-40(Celsius)", "Fine", "Yes", "No", "Yes"): h1+" , "+n1,
    ("38-40(Celsius)", "Fine", "Yes", "No", "No"): h1+" , "+n1+" , "+d1,
    ("38-40(Celsius)", "Fine", "No", "No", "No"): h1+" , "+e1+" , "+n1+" , "+d1,
    ("38-40(Celsius)", "Fine", "No", "Yes", "No"): h1+" , "+e1+" , "+d1,
    ("38-40(Celsius)", "Fine", "No", "No", "Yes"): h1+" , "+e1+" , "+n1,
    ("38-40(Celsius)", "Fine", "No", "Yes", "Yes"): h1+" , "+e1,
    ("38-40(Celsius)", "Sick", "Yes", "Yes", "Yes"): s2,
    ("38-40(Celsius)", "Sick", "Yes", "Yes", "No"): s2+" , "+d1,
    ("38-40(Celsius)", "Sick", "Yes", "No", "Yes"): s2+" , "+n1,
    ("38-40(Celsius)", "Sick", "Yes", "No", "No"): s2+" , "+n1+" , "+d1,
    ("38-40(Celsius)", "Sick", "No", "No", "No"): s2+" , "+e1+" , "+n1+" , "+d1,
    ("38-40(Celsius)", "Sick", "No", "Yes", "No"): s2+" , "+e1+" , "+d1,
    ("38-40(Celsius)", "Sick", "No", "No", "Yes"): s2+" , "+e1+" , "+n1,
    ("38-40(Celsius)", "Sick", "No", "Yes", "Yes"): s2+" , "+e1,
}

#DICTIONARY FOR RECOMMENDED TREATMENT
Treatment_Dictionary = {
    a1: "In your system, there might be an active virus or bacteria. Try taking antibiotics, and consult with your local doctor if the symptoms start to worsen.",
    s1: "You might have mild hypothermia. Ensure you are adequately dressed for the temperature.",
    s2: "You may have symptoms of the flu or common cold. Rest and drink plenty of fluids, and consume suitable medicine if needed.",
    l1: "You might be experiencing low body temperature. Make sure to keep warm and wear additional clothing.",
    h1: "Your body temperature is high. Take fever reducers and consult with a doctor if the issue persists.",
    e1: "Your symptoms could be an effect of your lack of exercise. Try maintaining a good exercise routine.",
    n1: "Insufficient nutrition may be affecting your health. Try to eat a balanced diet and stay hydrated.",
    d1: "Proper amounts of sleep are very vital for your health. Make sure that you are getting enough rest for the day.",
    l1+" , "+d1: "You might be experiencing low body temperature. Make sure to keep warm and wear additional clothing.\n"
                 "Proper amounts of sleep are very vital for your health. Make sure that you are getting enough rest for the day.",
    l1+" , "+n1: "You might be experiencing low body temperature. Make sure to keep warm and wear additional clothing.\n"
                 "Insufficient nutrition may be affecting your health. Try to eat a balanced diet and stay hydrated.",
    l1+" , "+n1+" , "+d1:"You might be experiencing low body temperature. Make sure to keep warm and wear additional clothing.\n"
                         "Insufficient nutrition may be affecting your health. Try to eat a balanced diet and stay hydrated.\n"
                         "Proper amounts of sleep are very vital for your health. Make sure that you are getting enough rest for the day.",
    l1+" , "+e1+" , "+d1+" , "+n1: "You might be experiencing low body temperature. Make sure to keep warm and wear additional clothing.\n"
                                   "Your symptoms could be an effect of your lack of exercise. Try maintaining a good exercise routine.\n"
                                   "Proper amounts of sleep are very vital for your health. Make sure that you are getting enough rest for the day.\n"
                                   "Insufficient nutrition may be affecting your health. Try to eat a balanced diet and stay hydrated.",
    l1+" , "+e1+" , "+d1: "You might be experiencing low body temperature. Make sure to keep warm and wear additional clothing.\n"
                          "Your symptoms could be an effect of your lack of exercise. Try maintaining a good exercise routine.\n"
                          "Proper amounts of sleep are very vital for your health. Make sure that you are getting enough rest for the day.",
    l1+" , "+e1+" , "+n1: "You might be experiencing low body temperature. Make sure to keep warm and wear additional clothing.\n"
                          "Your symptoms could be an effect of your lack of exercise. Try maintaining a good exercise routine.\n"
                          "Insufficient nutrition may be affecting your health. Try to eat a balanced diet and stay hydrated.",
    l1+" , "+e1: "You might be experiencing low body temperature. Make sure to keep warm and wear additional clothing.\n"
                 "Your symptoms could be an effect of your lack of exercise. Try maintaining a good exercise routine.",
    s1+" , "+d1: "You might have mild hypothermia. Ensure you are adequately dressed for the temperature.\n"
                 "Proper amounts of sleep are very vital for your health. Make sure that you are getting enough rest for the day.",
    s1+" , "+n1: "You might have mild hypothermia. Ensure you are adequately dressed for the temperature.\n"
                 "Insufficient nutrition may be affecting your health. Try to eat a balanced diet and stay hydrated.",
    s1+" , "+n1+" , "+d1: "You might have mild hypothermia. Ensure you are adequately dressed for the temperature.\n"
                          "Insufficient nutrition may be affecting your health. Try to eat a balanced diet and stay hydrated.\n"
                          "Proper amounts of sleep are very vital for your health. Make sure that you are getting enough rest for the day.",
    s1+" , "+e1+" , "+n1+" , "+d1: "You might have mild hypothermia. Ensure you are adequately dressed for the temperature.\n"
                                   "Your symptoms could be an effect of your lack of exercise. Try maintaining a good exercise routine.\n"
                                   "Insufficient nutrition may be affecting your health. Try to eat a balanced diet and stay hydrated.\n"
                                   "Proper amounts of sleep are very vital for your health. Make sure that you are getting enough rest for the day.",
    s1+" , "+e1 + " , "+d1: "You might have mild hypothermia. Ensure you are adequately dressed for the temperature.\n"
                            "Your symptoms could be an effect of your lack of exercise. Try maintaining a good exercise routine.\n"
                            "Proper amounts of sleep are very vital for your health. Make sure that you are getting enough rest for the day.",
    s1+" , "+e1+" , "+n1: "You might have mild hypothermia. Ensure you are adequately dressed for the temperature.\n"
                          "Your symptoms could be an effect of your lack of exercise. Try maintaining a good exercise routine.\n"
                          "Insufficient nutrition may be affecting your health. Try to eat a balanced diet and stay hydrated.",
    s1+" , "+e1: "You might have mild hypothermia. Ensure you are adequately dressed for the temperature.\n"
                 "Your symptoms could be an effect of your lack of exercise. Try maintaining a good exercise routine.",
    e1+" , "+d1: "Your symptoms could be an effect of your lack of exercise. Try maintaining a good exercise routine.\n"
                 "Proper amounts of sleep are very vital for your health. Make sure that you are getting enough rest for the day.",
    e1+" , "+n1+" , "+d1: "Your symptoms could be an effect of your lack of exercise. Try maintaining a good exercise routine.\n"
                          "Insufficient nutrition may be affecting your health. Try to eat a balanced diet and stay hydrated.\n"
                          "Proper amounts of sleep are very vital for your health. Make sure that you are getting enough rest for the day.",
    n1+" , "+d1: "Insufficient nutrition may be affecting your health. Try to eat a balanced diet and stay hydrated.\n"
                 "Proper amounts of sleep are very vital for your health. Make sure that you are getting enough rest for the day.",
    e1+" , "+n1: "Your symptoms could be an effect of your lack of exercise. Try maintaining a good exercise routine.\n"
                 "Insufficient nutrition may be affecting your health. Try to eat a balanced diet and stay hydrated.",
    a1+" , "+d1: "In your system, there might be an active virus or bacteria. Try taking antibiotics, and consult with your local doctor if the symptoms start to worsen.\n"
                 "Proper amounts of sleep are very vital for your health. Make sure that you are getting enough rest for the day.",
    a1+" , "+n1: "In your system, there might be an active virus or bacteria. Try taking antibiotics, and consult with your local doctor if the symptoms start to worsen.\n"
                 "Insufficient nutrition may be affecting your health. Try to eat a balanced diet and stay hydrated.",
    a1+" , "+n1+" , "+d1: "In your system, there might be an active virus or bacteria. Try taking antibiotics, and consult with your local doctor if the symptoms start to worsen.\n"
                          "Insufficient nutrition may be affecting your health. Try to eat a balanced diet and stay hydrated.\n"
                          "Proper amounts of sleep are very vital for your health. Make sure that you are getting enough rest for the day.",
    a1+" , "+e1+" , "+n1+" , "+d1: "In your system, there might be an active virus or bacteria. Try taking antibiotics, and consult with your local doctor if the symptoms start to worsen.\n"
                                   "Your symptoms could be an effect of your lack of exercise. Try maintaining a good exercise routine.\n"
                                   "Insufficient nutrition may be affecting your health. Try to eat a balanced diet and stay hydrated.\n"
                                   "Proper amounts of sleep are very vital for your health. Make sure that you are getting enough rest for the day.",
    a1+" , "+e1+" , "+d1: "In your system, there might be an active virus or bacteria. Try taking antibiotics, and consult with your local doctor if the symptoms start to worsen.\n"
                          "Your symptoms could be an effect of your lack of exercise. Try maintaining a good exercise routine.\n"
                          "Proper amounts of sleep are very vital for your health. Make sure that you are getting enough rest for the day.",
    a1+" , "+e1+" , "+n1: "In your system, there might be an active virus or bacteria. Try taking antibiotics, and consult with your local doctor if the symptoms start to worsen.\n"
                          "Your symptoms could be an effect of your lack of exercise. Try maintaining a good exercise routine.\n"
                          "Insufficient nutrition may be affecting your health. Try to eat a balanced diet and stay hydrated.",
    a1+" , "+e1: "In your system, there might be an active virus or bacteria. Try taking antibiotics, and consult with your local doctor if the symptoms start to worsen.\n"
                 "Your symptoms could be an effect of your lack of exercise. Try maintaining a good exercise routine.",
    h1+" , "+d1: "Your body temperature is high. Take fever reducers and consult with a doctor if the issue persists.\n"
                 "Proper amounts of sleep are very vital for your health. Make sure that you are getting enough rest for the day.",
    h1+" , "+n1: "Your body temperature is high. Take fever reducers and consult with a doctor if the issue persists.\n"
                 "Insufficient nutrition may be affecting your health. Try to eat a balanced diet and stay hydrated.",
    h1+" , "+n1+" , "+d1: "Your body temperature is high. Take fever reducers and consult with a doctor if the issue persists.\n"
                          "Insufficient nutrition may be affecting your health. Try to eat a balanced diet and stay hydrated.\n"
                          "Proper amounts of sleep are very vital for your health. Make sure that you are getting enough rest for the day.",
    h1+" , "+e1+" , "+n1+" , "+d1: "Your body temperature is high. Take fever reducers and consult with a doctor if the issue persists.\n"
                                   "Your symptoms could be an effect of your lack of exercise. Try maintaining a good exercise routine.\n"
                                   "Insufficient nutrition may be affecting your health. Try to eat a balanced diet and stay hydrated.\n"
                                   "Proper amounts of sleep are very vital for your health. Make sure that you are getting enough rest for the day.",
    h1+" , "+e1+" , "+d1: "Your body temperature is high. Take fever reducers and consult with a doctor if the issue persists.\n"
                          "Your symptoms could be an effect of your lack of exercise. Try maintaining a good exercise routine.\n"
                          "Proper amounts of sleep are very vital for your health. Make sure that you are getting enough rest for the day.",
    h1+" , "+e1+" , "+n1: "Your body temperature is high. Take fever reducers and consult with a doctor if the issue persists.\n"
                          "Your symptoms could be an effect of your lack of exercise. Try maintaining a good exercise routine.\n"
                          "Insufficient nutrition may be affecting your health. Try to eat a balanced diet and stay hydrated.",
    h1+" , "+e1: "Your body temperature is high. Take fever reducers and consult with a doctor if the issue persists.\n"
                 "Your symptoms could be an effect of your lack of exercise. Try maintaining a good exercise routine.",
    s2+" , "+d1: "You may have symptoms of the flu or common cold. Rest and drink plenty of fluids, and consume suitable medicine if needed.\n"
                 "Proper amounts of sleep are very vital for your health. Make sure that you are getting enough rest for the day.",
    s2+" , "+n1: "You may have symptoms of the flu or common cold. Rest and drink plenty of fluids, and consume suitable medicine if needed.\n"
                 "Insufficient nutrition may be affecting your health. Try to eat a balanced diet and stay hydrated.",
    s2+" , "+n1+" , "+d1: "You may have symptoms of the flu or common cold. Rest and drink plenty of fluids, and consume suitable medicine if needed.\n"
                          "Insufficient nutrition may be affecting your health. Try to eat a balanced diet and stay hydrated.\n"
                          "Proper amounts of sleep are very vital for your health. Make sure that you are getting enough rest for the day.",
    s2+" , "+e1+" , "+n1+" , "+d1: "You may have symptoms of the flu or common cold. Rest and drink plenty of fluids, and consume suitable medicine if needed.\n"
                                   "Your symptoms could be an effect of your lack of exercise. Try maintaining a good exercise routine.\n"
                                   "Insufficient nutrition may be affecting your health. Try to eat a balanced diet and stay hydrated.\n"
                                   "Proper amounts of sleep are very vital for your health. Make sure that you are getting enough rest for the day.",
    s2+" , "+e1+" , "+d1: "You may have symptoms of the flu or common cold. Rest and drink plenty of fluids, and consume suitable medicine if needed.\n"
                          "Your symptoms could be an effect of your lack of exercise. Try maintaining a good exercise routine.\n"
                          "Proper amounts of sleep are very vital for your health. Make sure that you are getting enough rest for the day.",
    s2+" , "+e1+" , "+n1: "You may have symptoms of the flu or common cold. Rest and drink plenty of fluids, and consume suitable medicine if needed.\n"
                          "Your symptoms could be an effect of your lack of exercise. Try maintaining a good exercise routine.\n"
                          "Insufficient nutrition may be affecting your health. Try to eat a balanced diet and stay hydrated.",
    s2+" , "+e1: "You may have symptoms of the flu or common cold. Rest and drink plenty of fluids, and consume suitable medicine if needed.\n"
                 "Your symptoms could be an effect of your lack of exercise. Try maintaining a good exercise routine."

}

# LOGO
logo = Image.open("smart_doctor-removebg-preview (1) (1).png")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

# MAIN MENU
def open_window():
    new_window = tk.Toplevel(app)
    new_window.title("SMART DOCTOR")
    new_window.geometry("1920x1080")

    topics = tk.Listbox(new_window, selectmode=tk.SINGLE, bg="light blue")
    topics.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)

    information_frame = tk.Frame(new_window)
    information_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    #TEXT ONLY
    def show_info(info):
        for widget in information_frame.winfo_children():
            widget.destroy()

        label = tk.Label(information_frame, text=info, wraplength=600, justify=tk.LEFT, padx=10, pady=10)
        label.pack(fill=tk.BOTH, expand=True)

    #MULTIPLE WIDGETS
    def show_info2(info):
        for widget in information_frame.winfo_children():
            widget.destroy()

        label = tk.Label(information_frame, text=info, wraplength=600, justify=tk.LEFT, padx=10, pady=25)
        label.pack(fill=tk.BOTH, expand=False)

    def insert_widgets(widgets):
        for widget in widgets:
            widget.pack(pady=10, padx=10)

    def generalbutton1():
        info = ("What is SMART DOCTOR?\n\n"
                "SMART DOCTOR is an innovative app designed to assist individuals in analyzing their symptoms of sickness. \nBy inputting their symptoms into the app, users receive a comprehensive analysis that suggests \npotential diseases or conditions they may be experiencing. "
                "\nThis analysis is based on sophisticated algorithms that consider a wide range of symptoms and medical knowledge.\n"
                "\nWhat does SMART DOCTOR do? \n\n"
                "The app aims to provide users with valuable insights into their health, helping them understand possible health issues they might have. \nIt offers recommendations for medical treatments and next steps to take,\nsuch as visiting a healthcare professional for further evaluation or providing self-care tips."
                "\n\nWith SMART DOCTOR, users can gain a better understanding of their health status \nand make informed decisions about seeking appropriate medical attention. \nThis user-friendly interface empowers individuals to take control of their well-being by providing accurate and \ntimely information about potential health concerns.")
        show_info(info)

    general_info = tk.Button(master=topics, text="General Information", command=generalbutton1)
    general_info.pack(side=tk.TOP, fill="x", padx=5, pady=5)

    def generalbutton2():
        for widget in information_frame.winfo_children():
            widget.destroy()

        combo_frame = tk.Frame(information_frame)
        combo_frame.pack()

        labelbefore = tk.Label(combo_frame, text="Welcome to the Symptoms Page.\n\nHere, you can choose the options that best describe how you are feeling right now."
                "\nThis information will be processed to make a diagnosis \nfor your health and suggest some possible diseases that you might have."
                "\n\nPlease choose the options that are true about your current state of health\n(Choose at least one option)",pady=10)
        labelbefore.pack()

        combo_frame1 = tk.Frame(information_frame)
        combo_frame1.pack()

        label1 = tk.Label(combo_frame1, text="What is your temperature right now?",pady=5)
        label1.pack()

        new_window.effect_var1 = tk.StringVar()
        new_window.effect_var1.set("")
        symptomscombobox1 = ttk.Combobox(combo_frame1, textvariable=new_window.effect_var1,
                                                  values=["32-34(Celsius)","35-37(Celsius)","38-40(Celsius)"],width=60)
        symptomscombobox1.pack()

        combo_frame2 = tk.Frame(information_frame)
        combo_frame2.pack()

        label2 = tk.Label(combo_frame2, text="How do you feel?",pady=5)
        label2.pack()

        new_window.effect_var2 = tk.StringVar()
        new_window.effect_var2.set("")
        symptomscombobox2 = ttk.Combobox(combo_frame2, textvariable=new_window.effect_var2,
                                        values=["Fine", "Sick"],width=60)
        symptomscombobox2.pack()

        combo_frame3 = tk.Frame(information_frame)
        combo_frame3.pack()

        label3 = tk.Label(combo_frame3, text="Do you exercise on a consistent, regular basis?",pady=5)
        label3.pack()

        new_window.effect_var3 = tk.StringVar()
        new_window.effect_var3.set("")
        symptomscombobox3 = ttk.Combobox(combo_frame3, textvariable=new_window.effect_var3,
                                         values=["Yes", "No"],width=60)
        symptomscombobox3.pack()

        combo_frame4 = tk.Frame(information_frame)
        combo_frame4.pack()

        label4 = tk.Label(combo_frame4, text="Do you eat enough food and drink enough water?",pady=5)
        label4.pack()

        new_window.effect_var4 = tk.StringVar()
        new_window.effect_var4.set("")
        symptomscombobox4 = ttk.Combobox(combo_frame4, textvariable=new_window.effect_var4,
                                         values=["Yes","No"],width=60)
        symptomscombobox4.pack()

        combo_frame5 = tk.Frame(information_frame)
        combo_frame5.pack()

        label5 = tk.Label(combo_frame5, text="Do you sleep at least 6 hours a day?",pady=5)
        label5.pack()

        new_window.effect_var5 = tk.StringVar()
        new_window.effect_var5.set("")
        symptomscombobox5 = ttk.Combobox(combo_frame5, textvariable=new_window.effect_var5,
                                         values=["Yes","No"],width=60)
        symptomscombobox5.pack()

        combo_frame6 = tk.Frame(information_frame)
        combo_frame6.pack()

        labelafter = tk.Label(combo_frame6, text="After you have finished picking all the options,\n"
                 "press the button below to process the information and get a diagnosis.",pady=15)
        labelafter.pack()

        def ProcessPossibleHealthIssues():
            for widget in information_frame.winfo_children():
                widget.destroy()

            temperature = new_window.effect_var1.get()
            health = new_window.effect_var2.get()
            exercise = new_window.effect_var3.get()
            consumption = new_window.effect_var4.get()
            sleep = new_window.effect_var5.get()

            overall = (temperature,health,exercise,consumption,sleep)
            response = Response_Dictionary.get(overall, "There seems to be no health issues that were found for these symptoms."
                                                        "\nYou are definitely healthy.")

            labelpossiblediseases = tk.Label(master=information_frame,
                                             text=
                                             "\nSYMPTOMS DATA"
                                             "\n\n\nTemperature : " +temperature+
                                             "\n\nHealth : " +health+
                                             "\n\nExercise : " +exercise+
                                             "\n\nConsumption : " +consumption+
                                             "\n\nSleep : " +sleep+
                                             "\n\n\n\n\nPOSSIBLE HEALTH ISSUES : \n\n" +response, pady=10)
            labelpossiblediseases.pack(side=tk.TOP)

            combo_frame7 = tk.Frame(information_frame)
            combo_frame7.pack()

            labeltreatment = tk.Label(combo_frame7,
                                      text="\n\n\n\n\n\n\nPress the button below to search for the recommended treatment\n"
                                           "that is needed to medicate your possible health issues ", pady=15)
            labeltreatment.pack(side=tk.TOP,expand=True)

            def ProcessRecommendedTreatment():
                for widget in information_frame.winfo_children():
                    widget.destroy()

                labeltreatment = tk.Label(master=information_frame,
                                                     text="\n\n\n\n\nHEALTH ISSUES\n\n" +response+
                                          "\n\n\n\n\n\n\nRECOMMENDED TREATMENT : \n\n" +
                                          Treatment_Dictionary.get(response, "No specific treatment is recommended") + "\n\n\n\nDon't forget to check out the 'Review and Feedback' section to give us your thoughts on the app.\n"
                                                                                                                       "Thanks for using SMART DOCTOR!",
                                          pady=10)
                labeltreatment.pack(side=tk.TOP)


            searchtreatmentbutton = tk.Button(master=combo_frame7, text="Search for Recommended Treatment",command=ProcessRecommendedTreatment,padx=5,pady=5)
            searchtreatmentbutton.pack(side=tk.TOP)

        processbutton = tk.Button(combo_frame6, text="Process",command=ProcessPossibleHealthIssues,padx=5, pady=10)
        processbutton.pack()

        insert_widgets([combo_frame, combo_frame1, combo_frame2, combo_frame3, combo_frame4, combo_frame5,combo_frame6])


    symptoms = tk.Button(master=topics, text="Symptoms", command=generalbutton2)
    symptoms.pack(side=tk.TOP, fill="x", padx=5, pady=5)

    def generalbutton3():
        info = ("In order to create a diagnosis for possible health issues that you might have,\n"
                "you must pick the options that are in the 'Symptoms' section first.\n\n"
                "Please go to the Symptoms Section.")
        show_info(info)

    possible_diseases = tk.Button(master=topics, text="Possible Health Issues", command=generalbutton3)
    possible_diseases.pack(side=tk.TOP, fill="x", padx=5, pady=5)

    def generalbutton4():
        info = ("In order to get the recommended treatment for a possible health issue,\n"
                "you need to go to the 'Symptoms' section and pick the options that best suit your state of health.\n\n"
                "After that, process the information and you will get a list of possible health issues that you might have.\n"
                "Then, press the 'Search for Recommended Treatment' button.\n\n"
                "Please go to the Symptoms section first.")
        show_info(info)

    recommended_treatment = tk.Button(master=topics, text="Recommended Treatment", command=generalbutton4)
    recommended_treatment.pack(side=tk.TOP, fill="x", padx=5, pady=5)

    def generalbutton5():
        info = ("Thanks for using SMART DOCTOR!\n\n\nWe would love to hear more about your thoughts on this app.\n"
                "If you don't mind, please write your thoughts about the app in the text box below.")
        show_info2(info)


        feedbacktext = tk.Text(master=information_frame)
        feedbacktext.pack(side=tk.TOP, padx=10, pady=10)

        def submitfeedback():
            feedbacktext.get(1.0,tk.END)
            userfeedback = feedbacktext.get(1.0,tk.END)
            feedbacktext.delete(1.0,tk.END)
            feedbacktext.insert(tk.END, "Text Submitted")

            print("Feedback :\n\n" +
                  userfeedback)

        submitfeedbackbutton = tk.Button(master=information_frame,text="Submit",command=submitfeedback)
        submitfeedbackbutton.pack(side=tk.TOP, padx=10, pady=10)

    feedback = tk.Button(master=topics, text="Review and Feedback", command=generalbutton5)
    feedback.pack(side=tk.TOP, fill="x", padx=5, pady=5)

# START SCREEN
instructions1 = tk.Label(app, text="Press START to initiate the program", font="Raleway")
instructions1.grid(column=1, row=1, padx=10, pady=5)

start = tk.Button(app, text="START", font="Raleway", bg="blue", fg="white", command=open_window)
start.grid(column=1, row=2, padx=10, pady=20)

app.mainloop()