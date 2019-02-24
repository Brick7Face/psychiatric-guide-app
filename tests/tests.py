from unittest import TestCase
from application.models import Step, Treatment, Medication, Prescriber, Patient, Phq9
from application.questionnaire_evaluations import PHQ9

class PHQ9TestCase(TestCase):
    phq9 = None

    def setUp(self):
        self.phq9 = PHQ9()

    def test_diagnosis_one(self):
        a1 = {1: 2, 2: 0}
        a2 = {1: 3, 2: 0}
        a3 = {1: 0, 2: 2}
        a4 = {1: 0, 2: 3}
        a5 = {1: 0, 2: 0}
        a6 = {1: 2, 2: 3}
        a7 = None
        self.assertTrue(self.phq9.diagnosis_one(a1))
        self.assertTrue(self.phq9.diagnosis_one(a2))
        self.assertTrue(self.phq9.diagnosis_one(a3))
        self.assertTrue(self.phq9.diagnosis_one(a4))
        self.assertFalse(self.phq9.diagnosis_one(a5))
        self.assertTrue(self.phq9.diagnosis_one(a6))
        self.assertFalse(self.phq9.diagnosis_one(a7))

    def test_diagnosis_two(self):
        # none
        a1 = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        # four
        a2 = {1: 2, 2: 2, 3: 2, 4: 2, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        # five
        a3 = {1: 2, 2: 2, 3: 2, 4: 2, 5: 0, 6: 0, 7: 0, 8: 0, 9: 2}
        # six
        a4 = {1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 0, 7: 0, 8: 0, 9: 2}
        self.assertFalse(self.phq9.diagnosis_two(a1))
        self.assertFalse(self.phq9.diagnosis_two(a2))
        self.assertTrue(self.phq9.diagnosis_two(a3))
        self.assertTrue(self.phq9.diagnosis_two(a4))

    def test_diagnosis_three(self):
        a1 = {10: 0}
        a2 = {10: 1}
        a3 = {10: 2}
        self.assertFalse(self.phq9.diagnosis_three(a1))
        self.assertFalse(self.phq9.diagnosis_three(a2))
        self.assertTrue(self.phq9.diagnosis_three(a3))

    def test_diagnosis(self):
        self.assertTrue(self.phq9.diagnosis(True, True, True))
        self.assertFalse(self.phq9.diagnosis(True, True, False))

    def test_change_treatment(self):
        self.assertTrue(self.phq9.change_treatment(True, True))
        self.assertTrue(self.phq9.change_treatment(True, False))
        self.assertFalse(self.phq9.change_treatment(False, False))

    def test_suicide_risk(self):
        a1 = {9: 0}
        a2 = {9: 1}
        a3 = {9: 2}
        self.assertFalse(self.phq9.suicide_risk(a1))
        self.assertTrue(self.phq9.suicide_risk(a2))
        self.assertTrue(self.phq9.suicide_risk(a3))

    def test_treatment_and_monitoring(self):
        a1 = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
        a2 = {1: 0, 2: 0, 3: 2, 4: 0, 5: 3, 6: 0, 7: 1, 8: 0, 9: 0, 10: 0}
        a3 = {1: 1, 2: 0, 3: 0, 4: 0, 5: 3, 6: 0, 7: 0, 8: 0, 9: 0, 10: 2}
        self.assertEqual(0, self.phq9.treatment_and_monitoring(a1))
        self.assertEqual(6, self.phq9.treatment_and_monitoring(a2))
        self.assertEqual(6, self.phq9.treatment_and_monitoring(a3))


    def test_convert_results(self):
        a1 = {'1':['2'], '2':['1']}
        a1_expected = {1:2, 2:1}
        self.assertEqual(self.phq9.convert_results(a1), a1_expected)

    def test_phq9_evaluation(self):
        # TODO: a change in the Severity Score of 5 or more
        pass


class ModelsTestCase(TestCase):
    
    def test_step_string(self):
        step = Step(name="Test Step", description="Testing...")
        self.assertEqual(str(step), step.name)

    def test_treatment_string(self):
        treatment = Treatment(name="Test Treatment")
        self.assertEqual(str(treatment), treatment.name)

    def test_medication_string(self):
        medication = Medication(name="Test Medication", category="Test", titration="NA", comments="NA")
        self.assertEqual(str(medication), medication.name)

    def test_patient_string(self):
        patient = Patient(last_name="Testson", address="NA", email="test@test.com", phone=5555555555, notes="NA")
        self.assertEqual(str(patient), patient.last_name)

         

#
#
# class MDQTestCase(TestCase):
#     def test_logic_for_questions_two_and_three(self):
#         pass
#
#     def test_evaluation_question_one(self):
#         pass
#
#     def test_evaluation_question_two(self):
#         pass
#
#     def test_evaluation_question_three(self):
#         pass
#
#     def test_mdq_diagnosis(self):
#         pass


