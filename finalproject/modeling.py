from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score

def train_random_forest(X_train, y_train, X_test, y_test):
    """
    Train and evaluate a Random Forest model.
    """
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    metrics = {
        "accuracy": accuracy_score(y_test, y_pred),
        "f1_score": f1_score(y_test, y_pred),
        "roc_auc": roc_auc_score(y_test, model.predict_proba(X_test)[:, 1]),
    }
    return model, metrics
