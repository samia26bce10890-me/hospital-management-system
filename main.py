hospitals = []
doctors = []
patients = []
appointments = []
def add_hospital():
  print("\n--- Add Hospital Details ---")
  name = input("Enter hospital name: ")
  location = input("Enter location: " )
  contact = input("Enter contact number: ")
  beds = int(input("Enter number of beds: "))
  departments = input("Enter departments: ")

  hospital = {
    "name": name,
    "location": location,
    "contact": contact,
    "beds": beds,
    "departments": departments
  }

  hospitals.append(hospital)
print("Hospital added successfully!")

def display_hospitals():
 print("\n--- Hospital Details ---")

 if len(hospitals) == 0:
  print("No hospital details available.")
 return

for i, hospital in enumerate(hospitals, 1):
 print("\nHospital", i)
 print("Name:", hospital["name"])
 print("Location:", hospital["location"])
 print("Contact:", hospital["contact"])
 print("Beds:", hospital["beds"])
 print("Departments:", hospital["departments"])

def add_doctor():
 print("\n--- Add Doctor Details ---")
 doctor_id = input("Enter doctor ID: ")
 name = input("Enter doctor name: ")
 specialization = input("Enter specialization: ")
 phone = input("Enter phone number: ")
 experience = input("Enter years of experience: ")

 doctor = {
    "id": doctor_id,
    "name": name,
    "specialization": specialization,
    "phone": phone,
    "experience": experience
  }

 doctors.append(doctor)
print("Doctor added successfully!")

def display_doctors():
 print("\n--- Doctor Details ---")

 if len(doctors) == 0:
  print("No doctor details available.")
  return

for doctor in doctors:
 print("\nDoctor ID:", doctor["id"])
 print("Name:", doctor["name"])
 print("Specialization:", doctor["specialization"])
 print("Phone:", doctor["phone"])
 print("Experience:", doctor["experience"], "years")

def add_patient():
 print("\n--- Add Patient Details ---")
 patient_id = input("Enter patient ID: ")
 name = input("Enter patient name: ")
 age = int(input("Enter age: "))
 gender = input("Enter gender: ")
 disease = input("Enter disease/problem: ")
 phone = input("Enter phone number: ")

 patient = {
  "id": patient_id,
  "name": name,
  "age": age,
  "gender": gender,
  "disease": disease,
  "phone": phone
}

 patients.append(patient)
print("Patient added successfully!")

def display_patients():
 print("\n--- Patient Details ---")

 if len(patients) == 0:
  print("No patient details available.")
  return

for patient in patients:
 print("\nPatient ID:", patient["id"])
 print("Name:", patient["name"])
 print("Age:", patient["age"])
 print("Gender:", patient["gender"])
 print("Disease:", patient["disease"])
 print("Phone:", patient["phone"])

def book_appointment():
 print("\n--- Book Appointment ---")
 patient_id = input("Enter patient ID: ")
 doctor_id = input("Enter doctor ID: ")
 date = input("Enter appointment date: ")
 time = input("Enter appointment time: ")

 appointment = {
 "patient_id": patient_id,
 "doctor_id": doctor_id,
 "date": date,
 "time": time
}

 appointments.append(appointment)
print("Appointment booked successfully!")

def display_appointments():
 print("\n--- Appointment Details ---") 

 if len(appointments) == 0:
  print("No appointments available.")
  return

for i, appointment in enumerate(appointments, 1):
 print("\nAppointment", i)
 print("Patient ID:", appointment["patient_id"])
 print("Doctor ID:", appointment["doctor_id"])
 print("Date:", appointment["date"])
 print("Time:", appointment["time"])

def search_hospital():
 print("\n--- Search Hospital ---")
 search = input("Enter hospital name: ")

 for hospital in hospitals:
  if hospital["name"].lower() == search.lower():
   print("\nHospital Found!")
   print("Name:", hospital["name"])
   print("Location:", hospital["location"])
   print("Contact:", hospital["contact"])
   print("Beds:", hospital["beds"])
   print("Departments:", hospital["departments"])
   return

print("Hospital not found.")
choice=''
print("\n====================================")
print("     HOSPITAL MANAGEMENT SYSTEM")
print("====================================")
print("1. Add Hospital")
print("2. Display Hospitals")
print("3. Search Hospital")
print("4. Add Doctor")
print("5. Display Doctors")
print("6. Add Patient")
print("7. Display Patients")
print("8. Book Appointment")
print("9. Display Appointments")
print("10. Exit")

choice = input("Enter your choice: ").strip()

if choice == "1":
  add_hospital()
elif choice == "2":
  display_hospitals()
elif choice == "3":
  search_hospital()
elif choice == "4":
  add_doctor()
elif choice == "5":
  display_doctors()
elif choice == "6":
  add_patient()
elif choice == "7":
  display_patients()
elif choice == "8":
  book_appointment()
elif choice == "9":
  display_appointments()
elif choice == "10":
  print("\nThank you for using the Hospital Management System!")
else:
 print("\nInvalid choice. Please try again.")
