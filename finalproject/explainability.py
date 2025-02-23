import lime
from lime.lime_tabular import LimeTabularExplainer
import numpy as np
import matplotlib.pyplot as plt

def explain_model_with_lime(model, X_train, X_test, feature_names, class_names):
   
    # Initialize LIME explainer
    explainer = LimeTabularExplainer(
        training_data=np.array(X_train),
        feature_names=feature_names,
        class_names=class_names,
        mode="classification"
    )

    # Choose a random sample from the test set
    i = np.random.randint(0, X_test.shape[0])
    sample = X_test[i].reshape(1, -1)

    # Generate explanation
    explanation = explainer.explain_instance(
        data_row=sample[0],
        predict_fn=model.predict_proba
    )

    # Visualize explanation
    explanation.show_in_notebook(show_table=True)
    explanation.as_pyplot_figure()
    plt.show()

    return explanation





