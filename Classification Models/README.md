This notebook demonstartes implementation of various machine learning models used to predict if a patient is hyperglycemic or not based on their ECG data.

a) ECG data is preprocessed using:
1. Butter BandPass Filter
2. R-Peaks detection using Pan tompkins method
3. P,Q,S,T waves detection using neurokit library.

b) Feature dataset is obtained from fiducial points using
1. Euclidean Distance
2. Slope

c) Following models are demonstrated :
1. One Class SVM
2. Logistic Regression
3. Linear SVM
4. Random Forest

Random Forest gives the best accuracy of 86%.

