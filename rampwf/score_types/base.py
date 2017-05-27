class BaseScoreType(object):
    def worst(self):
        if self.is_lower_the_better:
            return self.maximum
        else:
            return self.minimum

    def check(self, y_true, y_pred):
        if self.n_columns == 0:
            assert len(y_true.shape) == 1
            assert len(y_pred.shape) == 1
        else:
            assert len(y_true.shape) == 2
            assert len(y_pred.shape) == 2
        assert len(y_true) == len(y_pred)