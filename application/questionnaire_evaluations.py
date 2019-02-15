#TODO: make work with DB
# questions:
# how to format question 10 on PHQ-9
# how to format Treatment and Monitoring:
# multiple sections?
# table for part 3?

class PHQ9:
    """
    The first part to the Diagnosis section of the PHQ-9 evaluation. This part is true
    if at least one of the first two questions is answered as either a 2 or a 3.

    @param: a patients answers to the PHQ-9 questionnaire
    @return: Boolean - if answer to the first two questions are answered as a 2 or a 3
    """
    def diagnosis_one(self, answers):
        if not answers:
            return False
        if answers.get(1) in (2, 3) or answers.get(2) in (2, 3):
            return True
        else:
            return False

    """
    The second part of the Diagnosis section of the PHQ-9 evaluation. This part calculates
    the total symptom count and returns true if the total system count is greater than 5.
    The Total symptom count is calculated using two components:
     1) One point is added to the total every time a patient responded with either a 2 or
        a 3 for the first 8 questions.
     2) One point is added if a patient answered question 9 with either a 1, 2 or 3.

    @param: A patients answers to the PHQ-9 questionnaire
    @return: Boolean - if the total system count is greater than five
    """
    def diagnosis_two(self, answers):
        count = 0
        for i in range(1, 10):
            if answers.get(i) in (2, 3):
                count += 1
        if count >= 5:
            return True
        else:
            return False

    """
    The third part of the Diagnosis section of the PHQ-9 evaluation. This method
    returns a boolean value based on the patients response to question 10 on the
    PHQ-9 questionnaire.

    @param: A patients answers to the PHQ-9 questionnaire
    @return: Boolean - if the answer to question 10 is greater than Not 'difficult at all'
    """
    def diagnosis_three(self, answers):
        if answers.get(10) > 1:
            return True
        else:
            return False

    """
    Evaluates the three components of the diagnosis section of the PHQ-9 evaluation.
    Determines if a tentative diagnosis of depression can be made, after ruling out
    physical causes, normal bereavement and a history of a manic or hypomanic episode.
    Screen for bipolar disorder using the Mood Disorders Questionnaire

    @param: A patients answers to the PHQ-9 questionnaire
    @return: Boolean - if a doctor can make a tentative diagnosis of depression
    """
    def diagnosis(self, d1, d2, d3):
        return d1 and d2 and d3

    """
    Treatment or treatment change may be warranted if at least one of the first two questions
    is rated a 2 or 3 OR question 10 is rated at least Somewhat difficult. 
    
    @param: A patients answers to the PHQ-9 questionnaire
    @return: Boolean - if the prescribing physician should consider a treatment change
    """
    def change_treatment(self, d1, d3):
        return d1 or d3

    """
    If the patient answers question 9 of the PHQ9 evaluation they should be assessed 
    for suicide risk.
    
    @param: A patients answers to the PHQ-9 questionnaire
    @return: Boolean - if patient should be assessed for suicide risk.
    """
    def suicide_risk(self, answers):
        if answers.get(9) > 0:
            return True
        else:
            return False

    """
    Based on the calculated severity score show the recommended treatment 
    and tentative diagnosis 
    
    @param: A patients answers to the PHQ-9 questionnaire
    @return: ??? 
    """
    def treatment_and_monitoring(self, answers):
        severity_score = int(0)
        for i in range(1, len(answers) + 1):
            severity_score += answers.get(i)
        return severity_score
        #TODO: based on severity score print table from PHQ9 treatment and monitoring section 3


    """
    @param:
    @return:
    """
    def phq9_evaluation(self, answers):
        d1 = self.diagnosis_two(answers)
        d2 = self.diagnosis_two(answers)
        d3 = self.diagnosis_three(answers)

        self.diagnosis(d1, d2, d3)
        self.change_treatment(answers, d1)
        self.suicide_risk(answers)
        self.treatment_and_monitoring(answers)
        # TODO: Monitoring – a change in the Severity Score of 5 or more
        #  is considered clinically significant in assessing improvement of symptoms.


class MDQ:
    """
    based on the patients answers to question one of the MDQ determine if questions two and three
    need to be asked

    @param:
    @return:
    """
    def logic_for_questions_two_and_three(self):
        #TODO: 1) rename this
        #      2) figure out what this will look like
        #      3) write this
        pass

    """
    If seven or mare of the patient's responses from question one are marked yes,
    return true.

    @param:
    @return:
    """
    def evaluation_question_one(self, answers):
        #TODO: determine format of answers to questions (bool or int)
        question_one_score = 0
        for i in range(1, len(answers)):
            if answers.get(i) == 1:
                question_one_score += 1
        if question_one_score >= 7:
            return True
        else:
            return False

    """
    if the patient answered question two of the MDQ as yes return true
    
    @param:
    @return:
    """
    def evaluation_question_two(self, answers):
        #TODO: determine format of answers to questions (bool or int)
        if answers.get(2) == 1:
            return True
        else:
            return False

    """
    if the patient answered question three of the MDQ as either Moderate Problem or
    Serious Problem return true
    
    @param:
    @return:
    """
    def evaluation_question_three(self, answers):
        #TODO: determine format of answers to questions (bool or int)
        if answers.get(3) >= 2:
            return True
        else:
            return False

    """
    Evaluates the three components of the diagnosis section of the MDQ. This method
    Determines if the screen is positive for possible bipolar I disorder. Complete a 
    clinical interview to make a diagnosis. This screen is not as sensitive for 
    Bipolar II Disorder (depression and hypomania).
    
    @param:
    @return:
    """
    def mdq_diagnosis(self, answers):
        #TODO: For Treatment and Monitoring see “Bipolar Disorder Treatment Overview.
        if self.evaluation_question_one(answers) and self.evaluation_question_two(answers) \
                and self.evaluation_question_three(answers):
            return True
        else:
            return False

