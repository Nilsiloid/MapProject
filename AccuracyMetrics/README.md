# Accuracy Metric

The codefile [IOU.py](https://github.com/Nilsiloid/MapProject/blob/main/AccuracyMetrics/IOU.py), creates the bounding boxes of the annotations from the $x, y, w and h$ values from 2 text files and uses the Intersection Over Union algorithm to calculate the IOU value.

The file IOU_results_class1.txt stores the results of IOU accuracy metric(in %age) of the annotation labelled class 1(Map).
Similarly IOU_results_class2.txt stores the results of the annotation labelled class 2(Title).

Predictions_bounding_boxes and test_data_bounding_boxes are the 2 directories storing the files with $x, y, w and h$ values of bounding boxes of the annotations.
