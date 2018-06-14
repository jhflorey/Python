class Patient(object):
    def __init__(self, id, name, allergies, bed_number=None):
        """

        :param int id: the id of patient
        :param str name: the name of patient
        :param str allergies: the name of allergies
        :param int bed_number: the number of bed number
        """
        self.id = id
        self.name = name
        self.allergies = allergies
        self.bed_number = bed_number


class Hospital(object):
    def __init__(self, hospital_name, capacity):
        """

        :param str hospital_name: the name of the hospital
        :param int capacity: the maximum number of the bed
        """
        self.patients = []
        self.hospital_name = hospital_name
        self.capacity = capacity
        self.beds = []
        self.current_bed_number = 0
    def admit(self, patient):
        if len(self.patients) >= self.capacity:
            print(("The capacity of this %s hospital is reached to %s maximum capacity, we no longer admit patient") % (self.hospital_name, self.capacity))
            return self
        else:
            patient.bed_number = self.current_bed_number
            self.patients.append(patient)
            self.current_bed_number += 1
    def discharge(self, patient_id):
        for i in range(0,len(self.patients)):
            if self.patients[i].id == patient_id:
                self.patients[i].bed_number =None
                del self.patients[i]