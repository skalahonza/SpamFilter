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

    def wrong_tag(self, tag):
        if tag == self.pos_tag or tag == self.neg_tag:
            return False
        return True


    def update(self, truth, prediction):
        if self.wrong_tag(truth) or self.wrong_tag(prediction):
            raise ValueError
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
                self.FN += 1

    def compute_from_dicts(self, truth_dict, prediction_dict):
        for key, value in truth_dict.items():
            predicted = prediction_dict[key]
            self.update(value, predicted)


if __name__ == "__main__":
    cm1 = BinaryConfusionMatrix(pos_tag=True, neg_tag=False)
    print(cm1.as_dict())
    # {'tp': 0, 'tn': 0, 'fp': 0, 'fn': 0}
    cm1.update(True, True)
    print(cm1.as_dict())
    # {'tp': 1, 'tn': 0, 'fp': 0, 'fn': 0}
    truth_dict = {'em1': 'SPAM', 'em2': 'SPAM', 'em3': 'OK', 'em4': 'OK'}
    pred_dict = {'em1': 'SPAM', 'em2': 'OK', 'em3': 'OK', 'em4': 'SPAM'}
    cm2 = BinaryConfusionMatrix(pos_tag='SPAM', neg_tag='OK')
    cm2.compute_from_dicts(truth_dict, pred_dict)
    print(cm2.as_dict())
    #  {'tp': 1, 'tn': 1, 'fp': 1, 'fn': 1}
