class MedicalRecord:
    def __init__(self, user, icd_code, treatment, test_results):
        self.user = user
        self.icd_code = icd_code
        self.treatment = treatment
        self.test_results = test_results