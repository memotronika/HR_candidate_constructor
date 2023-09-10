import tkinter as tk
from tkinter import Checkbutton, messagebox
import json


def next_field(event):
    current_input = event.widget
    next_input = None

    all_widgets = window.winfo_children()
    for i, widget in enumerate(all_widgets):
        if widget == current_input:
            if i + 2 < len(all_widgets):
                next_input = all_widgets[i + 2]
                break

    if next_input:
        next_input.focus_set()


def add_to_db():
    name = input_name.get()
    if name == "":
        warning("NAME")
        return 'unvalid input"'
    surname = input_surname.get()
    if surname == "":
        warning("SURNAME")
        return 'unvalid input"'
    passport = input_passport.get()
    if passport == "":
        warning("passport")
        return 'unvalid input"'
    dateOfIssue = input_dateOfIssue.get()
    validTill = input_validTill.get()
    placeOfBirth = input_placeOfBirth.get()
    pesel = input_pesel.get()
    if valid_number(pesel, 11) == False:
        warning("PESEL")
        return 'unvalid input"'
    citizenship = input_citizenship.get()
    companyName = input_companyName.get()
    phone = input_phone.get()
    bankAccountNumber = input_bankAccountNumber.get()
    if valid_number(bankAccountNumber, 26) == False:
        warning("bank account number")
        return 'unvalid input"'
    cityOfLive = input_cityOfLive.get()
    street = input_street.get()
    building = input_building.get()
    postalCode = input_postalCode.get()
    client = input_client.get()
    role = input_role.get()
    salary = input_salary.get()
    info = input_info.get()
    inPoland = input_inPoland.get()
    ourAccomodation = input_ourAccomodation.get()
    dateOfBirth = input_dateOfBirth.get()

    candidate_data["name"] = name
    candidate_data["surname"] = surname
    candidate_data["passport"] = passport
    candidate_data["dateOfIssue"] = dateOfIssue
    candidate_data["validTill"] = validTill
    candidate_data["placeOfBirth"] = placeOfBirth
    candidate_data["dateOfBirth"] = dateOfBirth
    candidate_data["citizenship"] = citizenship
    candidate_data["companyName"] = companyName
    candidate_data["phone"] = phone
    candidate_data["bankAccountNumber"] = bankAccountNumber
    candidate_data["pesel"] = pesel
    candidate_data["cityOfLive"] = cityOfLive
    candidate_data["street"] = street
    candidate_data["building"] = building
    candidate_data["postalCode"] = postalCode
    candidate_data["client"] = client
    candidate_data["role"] = role
    candidate_data["salary"] = salary
    candidate_data["info"] = info
    candidate_data["inPoland"] = inPoland
    candidate_data["ourAccomodation"] = ourAccomodation

    with open(f'database/{surname.capitalize()} {name.capitalize()} {passport.upper()}.json', 'w') as json_file:
        json.dump(candidate_data, json_file)

    messagebox.showinfo("Approved", "Candidate has been added to database")


def warning(param):
    messagebox.showwarning("Warning", f"Data can't be saved due to unvalid input ({param})")


def valid_number(number: str, maxlen: int):
    if (number.isdigit() and len(number) == maxlen) or len(number) == 0:
        return True
    return False


def clear_data():
    global notification_window
    notification_window = tk.Toplevel(window)
    notification_window.geometry(f"{int(window.winfo_screenwidth() / 4)}x{int(window.winfo_screenheight() / 10 * 2)}+"
                                 f"{int(window.winfo_screenwidth() / 8 * 3)}+{int(window.winfo_screenheight() / 2.5)}")
    notification_window.grid_columnconfigure(0, weight=1)
    notification_window.grid_columnconfigure(1, weight=1)
    notification_label = tk.Label(notification_window, text="This will delete current data, are you sure you saved it?",
                                  height=6)
    notification_label.grid(row=0, column=0, columnspan=2)

    accept_button = tk.Button(notification_window, text="ACCEPT", command=accept_action, width=15)
    cancel_button = tk.Button(notification_window, text="CANCEL", command=cancel_action, width=15)
    cancel_button.grid(row=1, column=0, pady=10, padx=10)
    accept_button.grid(row=1, column=1, pady=10, padx=10)


def accept_action():
    input_name.delete(0, tk.END)
    input_surname.delete(0, tk.END)
    input_passport.delete(0, tk.END)
    input_dateOfIssue.delete(0, tk.END)
    input_validTill.delete(0, tk.END)
    input_placeOfBirth.delete(0, tk.END)
    input_dateOfBirth.delete(0, tk.END)
    input_citizenship.delete(0, tk.END)
    input_companyName.delete(0, tk.END)
    input_phone.delete(0, tk.END)
    input_bankAccountNumber.delete(0, tk.END)
    input_pesel.delete(0, tk.END)
    input_cityOfLive.delete(0, tk.END)
    input_street.delete(0, tk.END)
    input_building.delete(0, tk.END)
    input_postalCode.delete(0, tk.END)
    input_client.delete(0, tk.END)
    input_role.delete(0, tk.END)
    input_salary.delete(0, tk.END)
    input_info.delete(0, tk.END)
    input_inPoland.set(False)
    input_ourAccomodation.set(False)
    notification_window.destroy()


def cancel_action():
    notification_window.destroy()


def send_mail():
    global notification_window
    notification_window = tk.Toplevel(window)
    notification_window.geometry(f"{int(window.winfo_screenwidth() / 4)}x{int(window.winfo_screenheight() / 10 * 3)}+"
                                 f"{int(window.winfo_screenwidth() / 8 * 3)}+{int(window.winfo_screenheight() / 2.5)}")
    notification_window.grid_columnconfigure(0, weight=1)
    notification_window.grid_columnconfigure(1, weight=1)
    notification_window.grid_columnconfigure(2, weight=1)

    notification_label = tk.Label(notification_window, text="Choose recepient(s) of mail, containing workers's data.",
                                  height=7)
    notification_label.grid(row=0, column=0, columnspan=3)
    toHR_button = tk.Button(notification_window, text="HR", command=mailto_HR, width=15)
    toLegalize_button = tk.Button(notification_window, text="Legalization", command=mailto_legalize, width=15)
    toBoth_button = tk.Button(notification_window, text="To both", command=mailto_both, width=15)
    toHR_button.grid(row=1, column=0, pady=10, padx=10)
    toLegalize_button.grid(row=1, column=1, pady=10, padx=10)
    toBoth_button.grid(row=1, column=2, pady=10, padx=10)


def mailto_HR():
    notification_window.destroy()
    pass


def mailto_legalize():
    notification_window.destroy()
    pass


def mailto_both():
    notification_window.destroy()
    pass


# Creating main wimdow
window = tk.Tk()
window.title("HR Profile Constructor")
window.geometry(f"{int(window.winfo_screenwidth() / 2)}x{int(window.winfo_screenheight() / 5 * 3)}+"
                f"{int(window.winfo_screenwidth() / 4)}+{int(window.winfo_screenheight() / 5)}")

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_columnconfigure(3, weight=1)

candidate_data = {}
# Creating labels and input fields

label_name = tk.Label(window, text="Name:")
label_name.grid(row=0, column=0, padx=10, pady=5, sticky="e")
input_name = tk.Entry(window, width=26)
input_name.grid(row=0, column=1, padx=10, pady=5, sticky="w")
input_name.bind("<Return>", next_field)

label_surname = tk.Label(window, text="Surname:")
label_surname.grid(row=1, column=0, padx=10, pady=5, sticky="e")
input_surname = tk.Entry(window, width=26)
input_surname.grid(row=1, column=1, padx=10, pady=5, sticky="w")
input_surname.bind("<Return>", next_field)

label_passport = tk.Label(window, text="Passport nr.:")
label_passport.grid(row=2, column=0, padx=10, pady=5, sticky="e")
input_passport = tk.Entry(window, width=26)
input_passport.grid(row=2, column=1, padx=10, pady=5, sticky="w")
input_passport.bind("<Return>", next_field)

label_dateOfIssue = tk.Label(window, text="Date of issue:")
label_dateOfIssue.grid(row=3, column=0, padx=10, pady=5, sticky="e")
input_dateOfIssue = tk.Entry(window, width=26)
input_dateOfIssue.grid(row=3, column=1, padx=10, pady=5, sticky="w")
input_dateOfIssue.bind("<Return>", next_field)

label_validTill = tk.Label(window, text="Valid till:")
label_validTill.grid(row=4, column=0, padx=10, pady=5, sticky="e")
input_validTill = tk.Entry(window, width=26)
input_validTill.grid(row=4, column=1, padx=10, pady=5, sticky="w")
input_validTill.bind("<Return>", next_field)

label_placeOfBirth = tk.Label(window, text="Place of birth:")
label_placeOfBirth.grid(row=5, column=0, padx=10, pady=5, sticky="e")
input_placeOfBirth = tk.Entry(window, width=26)
input_placeOfBirth.grid(row=5, column=1, padx=10, pady=5, sticky="w")
input_placeOfBirth.bind("<Return>", next_field)

label_dateOfBirth = tk.Label(window, text="Date of birth:")
label_dateOfBirth.grid(row=6, column=0, padx=10, pady=5, sticky="e")
input_dateOfBirth = tk.Entry(window, width=26)
input_dateOfBirth.grid(row=6, column=1, padx=10, pady=5, sticky="w")
input_dateOfBirth.bind("<Return>", next_field)

label_citizenship = tk.Label(window, text="Obywatelstwo:")
label_citizenship.grid(row=7, column=0, padx=10, pady=5, sticky="e")
input_citizenship = tk.Entry(window, width=26)
input_citizenship.grid(row=7, column=1, padx=10, pady=5, sticky="w")
input_citizenship.bind("<Return>", next_field)

label_companyName = tk.Label(window, text="Spółka:")
label_companyName.grid(row=8, column=0, padx=10, pady=5, sticky="e")
input_companyName = tk.Entry(window, width=26)
input_companyName.grid(row=8, column=1, padx=10, pady=5, sticky="w")
input_companyName.bind("<Return>", next_field)

label_phone = tk.Label(window, text="Nr.tel:")
label_phone.grid(row=9, column=0, padx=10, pady=5, sticky="e")
input_phone = tk.Entry(window, width=26)
input_phone.grid(row=9, column=1, padx=10, pady=5, sticky="w")
input_phone.bind("<Return>", next_field)

label_bankAccountNumber = tk.Label(window, text="Nr. Konta bankowego:")
label_bankAccountNumber.grid(row=10, column=0, padx=10, pady=5, sticky="e")
input_bankAccountNumber = tk.Entry(window, width=26)
input_bankAccountNumber.grid(row=10, column=1, padx=10, pady=5, sticky="w")
input_bankAccountNumber.bind("<Return>", next_field)

label_pesel = tk.Label(window, text="PESEL:")
label_pesel.grid(row=11, column=0, padx=10, pady=5, sticky="e")
input_pesel = tk.Entry(window, width=26)
input_pesel.grid(row=11, column=1, padx=10, pady=5, sticky="w")
input_pesel.bind("<Return>", next_field)

label_cityOfLive = tk.Label(window, text="Miejcowość zamieszkania:")
label_cityOfLive.grid(row=0, column=2, padx=10, pady=5, sticky="e")
input_cityOfLive = tk.Entry(window, width=26)
input_cityOfLive.grid(row=0, column=3, padx=10, pady=5, sticky="w")
input_cityOfLive.bind("<Return>", next_field)

label_street = tk.Label(window, text="Ulica:")
label_street.grid(row=1, column=2, padx=10, pady=5, sticky="e")
input_street = tk.Entry(window, width=26)
input_street.grid(row=1, column=3, padx=10, pady=5, sticky="w")
input_street.bind("<Return>", next_field)

label_building = tk.Label(window, text="Nr. domu i mieszkania:")
label_building.grid(row=2, column=2, padx=10, pady=5, sticky="e")
input_building = tk.Entry(window, width=26)
input_building.grid(row=2, column=3, padx=10, pady=5, sticky="w")
input_building.bind("<Return>", next_field)

label_postalCode = tk.Label(window, text="Kod pocztowy:")
label_postalCode.grid(row=3, column=2, padx=10, pady=5, sticky="e")
input_postalCode = tk.Entry(window, width=26)
input_postalCode.grid(row=3, column=3, padx=10, pady=5, sticky="w")
input_postalCode.bind("<Return>", next_field)

label_client = tk.Label(window, text="Klient:")
label_client.grid(row=4, column=2, padx=10, pady=5, sticky="e")
input_client = tk.Entry(window, width=26)
input_client.grid(row=4, column=3, padx=10, pady=5, sticky="w")
input_client.bind("<Return>", next_field)

label_role = tk.Label(window, text="Stanowisko:")
label_role.grid(row=5, column=2, padx=10, pady=5, sticky="e")
input_role = tk.Entry(window, width=26)
input_role.grid(row=5, column=3, padx=10, pady=5, sticky="w")
input_role.bind("<Return>", next_field)

label_salary = tk.Label(window, text="Stawka:")
label_salary.grid(row=6, column=2, padx=10, pady=5, sticky="e")
input_salary = tk.Entry(window, width=26)
input_salary.grid(row=6, column=3, padx=10, pady=5, sticky="w")
input_salary.bind("<Return>", next_field)

label_info = tk.Label(window, text="Informacje dodatkowe:")
label_info.grid(row=7, column=2, padx=10, pady=5, sticky="e")
input_info = tk.Entry(window, width=26)
input_info.grid(row=7, column=3, padx=10, pady=5, sticky="w")
input_info.bind("<Return>", next_field)

label_inPoland = tk.Label(window, text="Kandydat przebywa w Polsce")
label_inPoland.grid(row=8, column=2, padx=10, pady=5, sticky="e")
input_inPoland = tk.BooleanVar(window)
checkbox_inPoland = Checkbutton(window, text="", variable=input_inPoland)
checkbox_inPoland.grid(row=8, column=3, padx=10, pady=5, sticky="w")

label_ourAccomodation = tk.Label(window, text="Kandydat wyn. mieszkanie Pago")
label_ourAccomodation.grid(row=9, column=2, padx=10, pady=5, sticky="e")
input_ourAccomodation = tk.BooleanVar(window)
checkbox_ourAccomodation = Checkbutton(window, text="", variable=input_ourAccomodation)
checkbox_ourAccomodation.grid(row=9, column=3, padx=10, pady=5, sticky="w")

# Сreating button, which adds json profile to database
button_add = tk.Button(window, text="Add candidate to database", command=add_to_db, width=20, height=2)
button_add.grid(row=12, column=0, padx=10, pady=15)

# Creating button, which clears all fields
button_clear = tk.Button(window, text="Clear data", command=clear_data, width=20, height=2)
button_clear.grid(row=12, column=1, padx=10, pady=15)

button_sendMail = tk.Button(window, text="Send Mail", command=send_mail, width=20, height=2)
button_sendMail.grid(row=12, column=2, padx=10, pady=15)

window.mainloop()
