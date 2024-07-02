from collections.abc import Sequence
from typing import Callable, Any, List, Tuple, Union
import numpy as np
import tensorflow as tf
from .classifierhelper import classifier_predict_simple_uncertainty, fit

class TargetPerformance:
    def __init__(self, validity_checker:Callable[[np.ndarray], np.ndarray], label, estimator=None, performance_predict_uncertainty_func: Callable[[Any, np.ndarray], Tuple[np.ndarray, np.ndarray]]=classifier_predict_simple_uncertainty, target_perf_fit_func:Callable[[Any, np.ndarray, np.ndarray], None]=fit):
        self.estimator = estimator
        self.performance_predict_uncertainty_func = performance_predict_uncertainty_func
        self.target_perf_fit_func = target_perf_fit_func
        self.label = label
        self.validity_checker = validity_checker

class ContinuousDesignBound:
    def __init__(self, lower_bound:float, upper_bound:float, label):
        self.label = label
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.validate()
    def validate(self):
        if(self.lower_bound>=self.upper_bound):
            raise ValueError("ContinuousDesignBound lower bound must be less than upper bound.")
        if(self.label=="" or self.label is None):
            raise ValueError("ContinuousDesignBound must have a label.")

class CategoricalDesignBound:
    def __init__(self, categories:List[Any], label):
        self.categories = categories
        self.label = label
        self._validate()
    
    def _validate(self):
        if not (isinstance(self.categories, np.ndarray) or isinstance(self.categories, Sequence)):
            raise ValueError("CategoricalDesignBound categories must be a list or numpy array.")
        if(len(self.categories)<=1):
            raise ValueError("CategoricalDesignBound must have at least 2 categories.")
        if(self.label=="" or self.label is None):
            raise ValueError("CategoricalDesignBound must have a label.")

class DataSetup:
    def __init__(self, params:List[Union[ContinuousDesignBound,CategoricalDesignBound]], targetPerfs:List[TargetPerformance], PERFORMANCE_ESTIMATOR_DROPOUT_RATE:float=0.2):
        self.params = params
        self.target_perfs = targetPerfs
        total_input_len = 0
        for param in params:
            if isinstance(param, ContinuousDesignBound):
                total_input_len += 1
            else:
                total_input_len += len(param.categories)
        for perf in targetPerfs:
            if(perf.estimator is None):
                perf.estimator = tf.keras.Sequential([
                    tf.keras.layers.Dense(100, activation='relu', input_shape=(total_input_len,)),
                    tf.keras.layers.Dense(50, activation='relu'),
                    tf.keras.layers.Dropout(PERFORMANCE_ESTIMATOR_DROPOUT_RATE),
                    tf.keras.layers.Dense(25, activation='relu'),
                    tf.keras.layers.Dense(1, activation='sigmoid')
                ])
                perf.estimator.compile(optimizer='adam',
                loss='binary_crossentropy', 
                metrics=['accuracy'])
