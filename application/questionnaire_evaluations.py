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
        for i in range(1, 9):
            if answers.get(i) in (2, 3):
                count += 1
        if answers.get(9) == 2 or answers.get(9) == 3:
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
    def diagnosis(self, answers):
        if self.diagnosis_one(answers) and self.diagnosis_two(answers) and self.diagnosis_three(answers):
            return True
        else:
            return False

    """
    @param: A patients answers to the PHQ-9 questionnaire
    @return:
    """
    def treatment_and_monitoring(self, answers):
        # --- Calculate Severity Score -------------------------------
        severityScore = int(0)
        for i in range(1, len(answers)):
            severityScore += answers.get(i)
        # ------------------------------------------------------------

        # --- Determine if treatment change may be warranted ---------
        if self.diagnosis_one(answers) or answers.get(10) >= 2:
            change_treatment = True
        # ------------------------------------------------------------

        # --- Determine if patient is suicide risk -------------------
        if answers.get(9) > 0:
            suicide_risk = True
        # ------------------------------------------------------------

        #TODO: how to format the info on this table:
        # pop-up?, new page?,
        # all together?, seperate?
        if severityScore >= 5:
            print("SEVERITY SCORE OF", severityScore, "USE THE FOLLOWING TABLE:")
            print("|---------|--------------------------------|--------------------------------------------------|")
            print("| Score   | Tentative Diagnosis            | Treatment Recommendation                         |")
            print("|---------|--------------------------------|--------------------------------------------------|")
            print("| 5 - 9   | Minimal symptoms               | Support, ask to call if worse, return in 1 month |")
            print("|---------|--------------------------------|--------------------------------------------------|")
            print("|         | Minor Depression               | Support, contact in one week                     |\n"
                  "| 10 - 14 | Dysthymia or major Depression, | Antidepressant or psychotherapy,                 |\n"
                  "|         | mild                           | contact in one week                              |")
            print("|---------|--------------------------------|--------------------------------------------------|")
            print("| 15 - 19 | Major Depression, moderate     | Antidepressant or psychotherapy                  |")
            print("|---------|--------------------------------|--------------------------------------------------|")
            print("|  >= 20  | Major Depression, severe       | Antidepressant and psychotherapy                 |\n"
                  "|         |                                | (especially if not improved on monotherapy)      |")
            print("|---------|--------------------------------|--------------------------------------------------|")

    """
    @param:
    @return:
    """
    def phq9_evaluation(self, answers):
        self.diagnosis(answers)
        self.treatment_and_monitoring(answers)
        # TODO: Monitoring – a change in the Severity Score of 5 or more
        #  is considered clinically significant in assessing improvement of symptoms.

    phq9_evaluation()


#TODO: make work with DB
# questions:
# how to format answers to question one
# how is answer to question 2 given
# how to format answer to question 3
# how to breakdown logic for when to ask questions 2 and 3

class MDQ:
    """
    @param:
    @return:
    """
    def mdq_evaluation(self, answers):
        question_one_score = 0
        for i in range(1, len(answers)):
            if answers.get(i) == 1:
                question_one_score += 1

        if question_one_score > 1:
            #ask question two and three
            pass


        # --- are the 7+ yes in question one ----------------------
        if question_one_score >= 7:
            diagnosis_one = True
        else:
            diagnosis_one = False

        # --- is question 2 yes -----------------------------------


        # --- is question 3 Moderate Problem or Serious Problem ---

        return None

    mdq_evaluation()
