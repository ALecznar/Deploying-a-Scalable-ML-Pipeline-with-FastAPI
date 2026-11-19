# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
I decided to use RandomForestClassifer for my prediction to see if someone who makes more than $50000 a year, or if they make less than or equal to $50000 a year. I then used OneHotEncoder in order to convert the categories into numbers and then used labelBinarizer for the encoding of the salary labels. The pyhon model used was 3.10.13 and the other scikit version was scikit-learn 1.5.1.
## Intended Use
The intended use of the model is to have it predict the category of whether an individual makes more than 50k a year or less than or equal to 50k a year.
## Training Data
I utilized the provided census.csv file. The data had person data that had age, education, occupation, hours worked and other items in it for my prediction. The goal of the project is to predict the salary category of an individual. I used the standard 80-20rule where 80 percent of the data is used to train, and 20 percent of the data is used to test.
## Evaluation Data
the 20 percent of data that was not used to train the data, was then used to test the models performance.
## Metrics

The model had a Precision of 0.7435, a Recall of 0.6384, and an F1 score of 0.6870 on the test data.

## Ethical Considerations
Anyone who uses this model should know that its predictions, as with any ML model, can be wrong. The model can perform differently across different groups of people and its predicutions should not be used to make assumptions about people based on their race or sex.

## Caveats and Recommendations
I feel as though the grouping data can be skewed if not used appropriatly. Some of the groups have much fewer examples for the trainign data to learn from, so predicitons can be wrong based on certain groups. One reccomendation I would have is to pursue and obtain extra data for training purposes, so that you have a higher data pool to pull from and possibly have better predictions.