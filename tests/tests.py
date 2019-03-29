from unittest import TestCase
from application.models import Step, Treatment, Medication, Prescriber, Patient, Phq9
from application.questionnaire_evaluations import PHQ9
<<<<<<< HEAD
from application.questionnaire_evaluations import MDQ

=======
from application.apps import ApplicationConfig
from django.urls import reverse
from django.apps import apps
>>>>>>> development

class PHQ9TestCase(TestCase):
    phq9 = None

    def setUp(self):
        self.phq9 = PHQ9()

    def test_diagnosis_one_one(self):
        a1 = {1: 2, 2: 0}
        self.assertTrue(self.phq9.diagnosis_one(a1))
		
    def test_diagnosis_one_two(self):
        a2 = {1: 3, 2: 0}
        self.assertTrue(self.phq9.diagnosis_one(a2))
	
    def test_diagnosis_one_three(self):
        a3 = {1: 0, 2: 2}
        self.assertTrue(self.phq9.diagnosis_one(a3))
		
    def test_diagnosis_one_four(self):
        a4 = {1: 0, 2: 3}
        self.assertTrue(self.phq9.diagnosis_one(a4))
	
    def test_diagnosis_one_five(self):
        a5 = {1: 0, 2: 0}
        self.assertFalse(self.phq9.diagnosis_one(a5))
		
    def test_diagnosis_one_six(self):
        a6 = {1: 2, 2: 3}
        self.assertTrue(self.phq9.diagnosis_one(a6))
		
    def test_diagnosis_one_seven(self):
        a7 = None
        self.assertFalse(self.phq9.diagnosis_one(a7))

    def test_diagnosis_two_one(self):
        # none
        a1 = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        self.assertFalse(self.phq9.diagnosis_two(a1))
		
    def test_diagnosis_two_two(self):
        # four
        a2 = {1: 2, 2: 2, 3: 2, 4: 2, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        self.assertFalse(self.phq9.diagnosis_two(a2))
		
    def test_diagnosis_two_three(self):
        # five
        a3 = {1: 2, 2: 2, 3: 2, 4: 2, 5: 0, 6: 0, 7: 0, 8: 0, 9: 2}
        self.assertTrue(self.phq9.diagnosis_two(a3))
		
    def test_diagnosis_two_four(self):
        # six
        a4 = {1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 0, 7: 0, 8: 0, 9: 2}
        self.assertTrue(self.phq9.diagnosis_two(a4))

    def test_diagnosis_three_one(self):
        a1 = {10: 0}
        self.assertFalse(self.phq9.diagnosis_three(a1))
		
    def test_diagnosis_three_two(self):
        a2 = {10: 1}
        self.assertFalse(self.phq9.diagnosis_three(a2))
		
    def test_diagnosis_three_three(self):
        a3 = {10: 2}
        self.assertTrue(self.phq9.diagnosis_three(a3))

    def test_diagnosis_one(self):
        self.assertTrue(self.phq9.diagnosis(True, True, True))
		
    def test_diagnosis_two(self):
        self.assertFalse(self.phq9.diagnosis(True, True, False))

    def test_change_treatment_one(self):
        self.assertTrue(self.phq9.change_treatment(True, True))
		
    def test_change_treatment_two(self):
        self.assertTrue(self.phq9.change_treatment(True, False))
		
    def test_change_treatment_three(self):
        self.assertFalse(self.phq9.change_treatment(False, False))

    def test_suicide_risk_one(self):
        a1 = {9: 0}
        self.assertFalse(self.phq9.suicide_risk(a1))
		
    def test_suicide_risk_two(self):
        a2 = {9: 1}
        self.assertTrue(self.phq9.suicide_risk(a2))
		
    def test_suicide_risk_three(self):
        a3 = {9: 2}
        self.assertTrue(self.phq9.suicide_risk(a3))

    def test_treatment_and_monitoring_one(self):
        a1 = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
        self.assertEqual(0, self.phq9.treatment_and_monitoring(a1))
		
    def test_treatment_and_monitoring_two(self):
        a2 = {1: 0, 2: 0, 3: 2, 4: 0, 5: 3, 6: 0, 7: 1, 8: 0, 9: 0, 10: 0}
        self.assertEqual(6, self.phq9.treatment_and_monitoring(a2))
		
    def test_treatment_and_monitoring_three(self):
        a3 = {1: 1, 2: 0, 3: 0, 4: 0, 5: 3, 6: 0, 7: 0, 8: 0, 9: 0, 10: 2}
        self.assertEqual(6, self.phq9.treatment_and_monitoring(a3))

    def test_convert_results(self):
        a1 = {'1': ['2'], '2': ['1']}
        a1_expected = {1: 2, 2: 1}
        self.assertEqual(self.phq9.convert_results(a1), a1_expected)

    def test_phq9_evaluation(self):
        a1 = {'1': ['0'], '2': ['0'], '3': ['0'], '4': ['0'], '5': ['0'], '6': ['0'], '7': ['0'], '8': ['0'],
              '9': ['0'], '10': ['1']}
        expected = {'diagnosis': False, 'change_treatment': False,'suicide_risk': False, 'severity_score': 1}
        self.assertEqual(self.phq9.phq9_evaluation(a1), expected)


class TestMDQ(TestCase):
    mdq = None

    def setUp(self):
        self.mdq = MDQ()

    def test_evaluation_question_one_one(self):
        a1 = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0}
        self.assertFalse(self.mdq.evaluation_question_one(a1))
		
    def test_evaluation_question_one_two(self):
        a2 = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0}
        self.assertFalse(self.mdq.evaluation_question_one(a2))
		
    def test_evaluation_question_one_three(self):
        a3 = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0}
        self.assertTrue(self.mdq.evaluation_question_one(a3))
		
	def test_evaluation_question_one_four(self):
        a4 = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 1}
        self.assertTrue(self.mdq.evaluation_question_one(a4))
		
    def test_evaluation_question_one_five(self):
        a5 = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 1}
        self.assertFalse(self.mdq.evaluation_question_one(a5))

    def test_evaluation_question_two_one(self):
        a1 = {14: 0}
        self.assertFalse(self.mdq.evaluation_question_two(a1))
	
    def test_evaluation_question_two_two(self):
        a2 = {14: 1}
        self.assertTrue(self.mdq.evaluation_question_two(a2))
	
    def test_evaluation_question_two_three(self):
        a3 = {14: 2}
        self.assertFalse(self.mdq.evaluation_question_two(a3))

    def test_evaluation_question_three_one(self):
        a1 = {15: 0}
        self.assertFalse(self.mdq.evaluation_question_three(a1))
		
    def test_evaluation_question_three_two(self):
        a2 = {15: 1}
        self.assertFalse(self.mdq.evaluation_question_three(a2))
		
    def test_evaluation_question_three_three(self):
        a3 = {15: 2}
        self.assertTrue(self.mdq.evaluation_question_three(a3))
		
	def test_evaluation_question_three_four(self):
        a4 = {15: 3}
        self.assertTrue(self.mdq.evaluation_question_three(a4))

    def test_convert_results(self):
        a1 = {'1': ['2'], '2': ['1']}
        a1_expected = {1: 2, 2: 1}
        self.assertEqual(self.mdq.convert_results(a1), a1_expected)

    def test_mdq_diagnosis_one(self):
        a1 = {'1': ['0'], '2': ['0'], '3': ['0'], '4': ['0'], '5': ['0'], '6': ['0'], '7': ['0'], '8': ['0'], '9': ['0'], '10': ['0'],'11': ['0'], '12': ['0'], '13': ['0'], '14': ['0'], '15': ['0']}
        self.assertFalse(self.mdq.mdq_diagnosis(a1))
		
    def test_mdq_diagnosis_two(self):
        a2 = {'1': ['1'], '2': ['1'], '3': ['1'], '4': ['1'], '5': ['1'], '6': ['1'], '7': ['0'], '8': ['0'], '9': ['0'], '10': ['0'],'11': ['0'], '12': ['0'], '13': ['0'], '14': ['0'], '15': ['3']}
        self.assertFalse(self.mdq.mdq_diagnosis(a2))
	
	def test_mdq_diagnosis_three(self):
        a3 = {'1': ['1'], '2': ['1'], '3': ['1'], '4': ['1'], '5': ['1'], '6': ['1'], '7': ['1'], '8': ['0'], '9': ['0'], '10': ['0'],'11': ['0'], '12': ['0'], '13': ['0'], '14': ['1'], '15': ['0']}
        self.assertFalse(self.mdq.mdq_diagnosis(a3))
		
	def test_mdq_diagnosis_four(self):
        a4 = {'1': ['1'], '2': ['1'], '3': ['1'], '4': ['1'], '5': ['1'], '6': ['1'], '7': ['0'], '8': ['0'], '9': ['0'], '10': ['0'],'11': ['0'], '12': ['0'], '13': ['0'], '14': ['0'], '15': ['3']}
        self.assertFalse(self.mdq.mdq_diagnosis(a4))
		
	def test_mdq_diagnosis_five(self):
        a5 = {'1': ['1'], '2': ['1'], '3': ['1'], '4': ['1'], '5': ['1'], '6': ['1'], '7': ['0'], '8': ['1'], '9': ['1'], '10': ['0'],'11': ['0'], '12': ['0'], '13': ['0'], '14': ['1'], '15': ['3']}
        self.assertTrue(self.mdq.mdq_diagnosis(a5))

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

		
class UrlsTestCase(TestCase):
	def test_logout_url(self):
		url = reverse('logout-view')
		self.assertEqual(url, '/application/logout/')
	
	def test_create_user_url(self):
		url = reverse('create-new-user')
		self.assertEqual(url, '/application/create_user/')
		
	def test_backend_home_url(self):
		url = reverse('backend-home')
		self.assertEqual(url, '/application/backend_home/')
		
	def test_documentation_url(self):
		url = reverse('documentation')
		self.assertEqual(url, '/application/documentation/')
		
	def test_survey_url(self):
		url = reverse('survey')
		self.assertEqual(url, '/application/survey/')
		
	def test_medications_url(self):
		url = reverse('medications')
		self.assertEqual(url, '/application/medications/')
		
	def test_patients_url(self):
		url = reverse('patients')
		self.assertEqual(url, '/application/patients/')
		
	def test_treatment_overview_url(self):
		url = reverse('treatment-overview')
		self.assertEqual(url, '/application/treatment-overview')
		
	def test_new_patient_url(self):
		url = reverse('new-patient')
		self.assertEqual(url, '/application/new-patient')
		
	def test_bug_report_url(self):
		url = reverse('bug_report')
		self.assertEqual(url, '/application/bug_report/')
	
class ApplicationConfigTest(TestCase):
	def test_apps_one(self):
		self.assertEqual(ApplicationConfig.name, 'application')
	
	def test_apps_two(self):
		self.assertEqual(apps.get_app_config('application').name, 'application')

		
		
		
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


>>>>>>> development
