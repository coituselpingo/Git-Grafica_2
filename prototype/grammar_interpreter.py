import re


class Grammar:

    def __init__(self, star_case):
        try:
            foo = star_case
            foo.upper()
            del foo
        except:
            return None

        self.type = 0

        self.base = star_case

        self.rule_list = []

        self.antecedent = []
        self.rules = {}

    def set_rule(self, rule):
        try:
            foo = rule
            foo.upper()
            del foo
        except:
            return None

        self.antecedent.append(re.split(':', rule)[0])

        try:
            self.rules[re.split(':', rule)[0]].append(re.split(':', rule)[1])
        except:
            self.rules[re.split(':', rule)[0]] = [re.split(':', rule)[1]]

    def derivate_setence_regular(self, sentence):
        carry = sentence
        for head_ref in self.antecedent:
            for body_ref in self.rules[head_ref]:
                carry = re.sub(head_ref, body_ref, carry)

        return carry

    def derivate_setence_context(self, sentence):
        carry = sentence
        for head_ref in self.antecedent:
            for body_ref in self.rules[head_ref]:
                carry = re.sub(head_ref, body_ref, carry)

        return carry

    def derivate_setence_stochastic(self, sentence):
        carry = sentence
        for head_ref in self.antecedent:
            for body_ref in self.rules[head_ref]:
                carry = re.sub(head_ref, body_ref, carry)

        return carry

    def setType(self, type):
        self.type = type

    def derivate(self, sentence):
        if self.type == 0:
            return self.derivate_setence_regular(sentence)
        elif self.type == 1:
            return self.derivate_setence_context(sentence)
        else:
            return None

    def make_grew(self, age):
        grew_sentence = self.base
        for i in range(0,age):
            grew_sentence = self.derivate(grew_sentence)
        return grew_sentence


