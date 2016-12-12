class BinaryConfusionMatrix:
    def __init__(self, pos_tag, neg_tag=False):
        self.neg_tag = neg_tag
        self.pos_tag = pos_tag
        self.TP = 0
        self.TN = 0
        self.FP = 0
        self.FN = 0

    def as_dict(self):
        return {"tp": self.TP, "tn": self.TN, "fp": self.FP, "fn": self.FN}

    def eval_tag(self, tag):
        return tag == self.pos_tag or tag == self.neg_tag

    def update(self, truth, prediction):
        if not self.eval_tag(truth) or not self.eval_tag(prediction):
            exec(ValueError)
        else:
            # TRUE POSITIVE
            if prediction == self.pos_tag and truth == self.pos_tag:
                self.TP += 1
            # TRUE NEGTIVE
            elif prediction == self.neg_tag and truth == self.neg_tag:
                self.TN += 1
            # FALSE POSITIVE
            elif prediction == self.pos_tag and truth == self.neg_tag:
                self.FP += 1
            # FALSE NEGATIVE
            elif prediction == self.neg_tag and truth == self.pos_tag:
                self.FP += 1

    def compute_from_dicts(self, truth_dict, prediction_dict):
        for key, value in truth_dict:
            pass
        pass