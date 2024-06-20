# PeakTime Machine Learning #
- - -
## 🗄️ Dataset ##
We get data from Google Form. And our final dataset is ```dataset_akhir_final.csv``` . The data we use for training and testing is divided by 2 with the ratio 80 : 20.
- - -
## ⚙️ Tools ##
1. [Pandas](https://pandas.pydata.org/docs/index.html)
2. [Numpy](https://numpy.org/)
3. [Matplotlib](https://matplotlib.org/)
4. [TensorFlow](https://www.tensorflow.org/)
5. [sckit-learn](https://scikit-learn.org/stable/)
- - -
## 🏢 Model Architecture ##
1. Hyperparameter Tuning :
   1. Parameter to Tune :
      1. 'max_depth' : ```[None, 10, 20, 30]```.
      2. 'min_examples' : ```[1, 2, 5, 10]```.
      3. 'num_trees' : ```[50, 100, 200]```.
      4. 'compute_oob_vatriables_importances' : ``[True, False]``.
   2. Looping through Combinations :
      1. Initialize the model with the current parameters.
      2. Compile the model with accuracy as the evaluation metric.
      3. Train the model on the training dataset ```'train_ds'```.
      4. Evaluate the model on the testing dataset ```'test_ds'```.
      5. Track the best performing model.
2. Best Model Selection :
   1. Print the best configuration and the accuracy.
3. Final Model Training :
   1. Initialize the model with the hyperparameters.
   2. Compile the model.
   3. Train the model on ```'train_ds'```.
- - - 
## 📑 Evaluation
After testing on the dataset we got the following accuracy :
```
Test loss: 0.0000
Test accuracy: 0.8788
```
- - -
## 🙋 Machine Learning Member
| Name | Student ID |
| -----|------------|
| Leonardo Alfontus Mende Sirait | M119D4KY3013 |
| Rayhan Ahmad Rizalullah | M119D4KY1813 |
| Imanuel Uneputty | M012D4KY3208 |