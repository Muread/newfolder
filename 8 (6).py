def mape(y_true, y_pred):
    n = len(y_true)
    errors = [abs((y_true[i] - y_pred[i]) / y_true[i]) for i in range(n)]
    mape = (sum(errors) / n) * 100
    return mape
    