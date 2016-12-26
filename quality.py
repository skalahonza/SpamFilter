import os

import utils
import confmat


def quality_score(tp, tn, fp, fn):
    return (tp + tn) / (tp + tn + 10 * fp + fn)


def compute_quality_for_corpus(corpus_dir):
    truth = utils.read_classification_from_file(corpus_dir + os.path.sep + "!truth.txt")
    predicted = utils.read_classification_from_file(corpus_dir + os.path.sep + "!prediction.txt")
    predMat = confmat.BinaryConfusionMatrix("SPAM", "OK")
    predMat.compute_from_dicts(truth, predicted)
    confusion_dict = predMat.as_dict()
    return quality_score(confusion_dict["tp"], confusion_dict["tn"], confusion_dict["fp"], confusion_dict["fn"])
