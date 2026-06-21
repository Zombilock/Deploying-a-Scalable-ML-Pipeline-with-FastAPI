# Model Card

## Model Details

This model is developed by Christopher Clark as part of the Udacity Machine Learning DevOps project "Deploying a Scalable ML Pipeline with FastAPI".
The model was created on June 21, 2026.
The model version is 1.0.0
The model used is Random Forest.
The model uses the default parameters for the random forest model.

## Intended Use

This model is intended to be used for predicting income either above or below 50k based on census income data.

## Training Data

The training data is comprised of 80% of the original census income dataset.

## Evaluation Data

The evaluation data utilized 20% of the original census dataset

## Metrics

The precision score was 0.7419.
The recall score was 0.6384.
The F1 score was 0.6863.

## Ethical Considerations

There are many factors to consider when looking at income data. Many factors can contribute to a bias in the data, which makes prediction difficult. While this model looks at a binary threshold, there are many outside factors to consider when analyzing the overall income data.

## Caveats and Recommendations

The recall and F1 scores are a bit low. This means the chosen model may not be the best fit, but it could also be a result of the above considerations causing bias and skewing the accuracy of the model. This type of data is constantly changing and is affected by many more factors than are provided in the dataset. Having a more in depth dataset with other involved factors would help with understanding this data.