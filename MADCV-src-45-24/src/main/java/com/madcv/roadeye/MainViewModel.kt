package com.madcv.roadeye

import androidx.lifecycle.ViewModel

/**
 *  This ViewModel is used to store object detector helper settings
 */
class MainViewModel : ViewModel() {
//    private var _delegate: Int = ObjectDetectorHelper.DELEGATE_CPU
    private var _threshold: Float =
        ObjectDetectorHelper.THRESHOLD_DEFAULT
    private var _maxResults: Int =
        ObjectDetectorHelper.MAX_RESULTS_DEFAULT
//    private var _model: Int = ObjectDetectorHelper.MODEL_EFFICIENTDETV0
//
//    val currentDelegate: Int get() = _delegate
    val currentThreshold: Float get() = _threshold
    val currentMaxResults: Int get() = _maxResults
    val currentModel: Int get() = ObjectDetectorHelper.MODEL_EFFICIENTDETV0
//
//    fun setDelegate(delegate: Int) {
//        _delegate = delegate
//    }

    fun setThreshold(threshold: Float) {
        _threshold = threshold
    }

    fun setMaxResults(maxResults: Int) {
        _maxResults = maxResults
    }
//
//    fun setModel(model: Int) {
//        _model = model
//    }
}
