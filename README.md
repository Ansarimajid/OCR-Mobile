# OCR Text Recognition Demo User Guide

This document provides instructions on how to run the OCR text recognition demo on an Android app, highlighting its usability and openness, such as running your own trained models in the demo. It also explains how to ensure the demo continues to run after updating models/input/output processing.

## How to Run the OCR Text Recognition Demo

### Environment Setup

1. Install Android Studio on your local machine. Detailed installation instructions can be found on the [Android Studio website](https://developer.android.com/studio).
2. Prepare an Android phone and enable USB debugging mode. To enable it: `Phone Settings -> Developer Options -> Enable Developer Options and USB Debugging Mode`

**Note:** If your Android Studio is not yet configured with NDK, please preconfigure it according to the [NDK and CMake installation and configuration](https://developer.android.com/studio/projects/install-ndk) in the Android Studio user guide. You can choose the latest NDK version or use the same version as the Paddle Lite prediction library.

### Deployment Steps

1. The OCR text recognition demo is located in the `Paddle-Lite-Demo/ocr/Android/app/c++/ppocr_demo` directory.
2. Navigate to the `Paddle-Lite-Demo/libs` directory and run the `download.sh` script to download the required Paddle Lite prediction library.
3. Navigate to the `Paddle-Lite-Demo/ocr/assets` directory and run the `download.sh` script to download the OPT-optimized model, test images, and label files.
4. Navigate to the `Paddle-Lite-Demo/ocr/Android/app/c++/ppocr_demo` directory and run the `prepare.sh` script to copy the model, test images, and other resource files to the current project.
5. Open the `ppocr_demo` project with Android Studio.
6. Connect your phone to the computer, enable USB debugging and file transfer mode, and connect your phone device in Android Studio (the phone needs to allow installation of software via USB).

<p align="center">
<img src="https://paddlelite-demo.bj.bcebos.com/demo/ocr/docs_img/android/run_ppocr_app.jpg"/>
</p>

> **Note:**
>> If you encounter NDK configuration errors during project import, compilation, or runtime, open `File > Project Structure > SDK Location`, and modify the `Android NDK location` to the path of the NDK configured on your machine.
>> If you downloaded the NDK through Android Studio's SDK Tools (see "Environment Setup"), you can select the default path from the dropdown menu.
>> Another NDK configuration method is to manually complete the NDK path configuration in the `image_classification_demo/local.properties` file, as shown below.
>> If the above steps still do not resolve the NDK configuration error, try updating the Android Gradle plugin version according to the [Updating the Android Gradle Plugin](https://developer.android.com/studio/releases/gradle-plugin?hl=en#updating-plugin) section in the official Android Studio documentation.

7. Click the Run button to automatically compile the app and install it on your phone. (This process will automatically download the Paddle Lite prediction library and model, and requires internet access). The result should look like this:

| APP Icon | APP Effect |
| ---      | ---        |
| ![app_pic](https://paddlelite-demo.bj.bcebos.com/demo/ocr/docs_img/android/ppocr_app_pic.jpg) | ![app_res](https://paddlelite-demo.bj.bcebos.com/demo/ocr/docs_img/android/ppocr_app_run.jpg) |

```shell
cd Paddle-Lite-Demo/libs
# Download the required Paddle Lite prediction library
sh download.sh
cd ../ocr/assets
# Download OPT-optimized models, test images, label files, and config files
sh download.sh
cd ../android/app/c++/ppocr_demo
# Copy the prediction library, models, and other resource files to the current project
sh prepare.sh
# Open the ppocr_demo project with Android Studio and complete the app compilation and run
```

## How to Update the Prediction Library

* Paddle Lite project: https://github.com/PaddlePaddle/Paddle-Lite
* Refer to the [Paddle Lite source code compilation document](https://paddle-lite.readthedocs.io/zh/latest/source_compile/compile_env.html) to compile the Android prediction library.
* The compiled artifacts are located under `build.lite.xxx.xxx.xxx/inference_lite_lib.xxx.xxx`.
  * Replace the C++ library:
    * Header files:
      Replace the generated `build.lite.android.xxx.gcc/inference_lite_lib.android.xxx/cxx/include` folder with the `ppocr_demo/app/PaddleLite/cxx/include` folder in the demo.
    * armeabi-v7a:
      Replace the generated `build.lite.android.armv7.gcc/inference_lite_lib.android.armv7/cxx/libs/libpaddle_lite_api_shared.so` library with the `ppocr_demo/app/PaddleLite/cxx/libs/armeabi-v7a/libpaddle_lite_api_shared.so` library in the demo.
    * arm64-v8a:
      Replace the generated `build.lite.android.armv8.gcc/inference_lite_lib.android.armv8/cxx/libs/libpaddle_lite_api_shared.so` library with the `ppocr_demo/app/PaddleLite/cxx/libs/arm64-v8a/libpaddle_lite_api_shared.so` library in the demo.

**Note:**
If the prediction library is upgraded, it is recommended to update the OPT-optimized model accordingly. For example, if the prediction library is upgraded to version 2.10-rc, follow these steps:

```shell
# Download PaddleOCR V2.0 version Chinese-English inference models
wget https://paddleocr.bj.bcebos.com/dygraph_v2.0/slim/ch_ppocr_mobile_v2.0_det_slim_infer.tar && tar xf ch_ppocr_mobile_v2.0_det_slim_infer.tar
wget https://paddleocr.bj.bcebos.com/dygraph_v2.0/slim/ch_ppocr_mobile_v2.0_rec_slim_infer.tar && tar xf ch_ppocr_mobile_v2.0_rec_slim_infer.tar
wget https://paddleocr.bj.bcebos.com/dygraph_v2.0/slim/ch_ppocr_mobile_v2.0_cls_slim_infer.tar && tar xf ch_ppocr_mobile_v2.0_cls_slim_infer.tar
# Get the OPT tool for MAC system version 2.10
wget https://github.com/PaddlePaddle/Paddle-Lite/releases/download/v2.10-rc/opt_mac
# Convert the V2.0 detection model
./opt --model_file=./ch_ppocr_mobile_v2.0_det_slim_infer/inference.pdmodel --param_file=./ch_ppocr_mobile_v2.0_det_slim_infer/inference.pdiparams --optimize_out=./ch_ppocr_mobile_v2.0_det_slim_opt --valid_targets=arm --optimize_out_type=naive_buffer
# Convert the V2.0 recognition model
./opt --model_file=./ch_ppocr_mobile_v2.0_rec_slim_infer/inference.pdmodel --param_file=./ch_ppocr_mobile_v2.0_rec_slim_infer/inference.pdiparams --optimize_out=./ch_ppocr_mobile_v2.0_rec_slim_opt --valid_targets=arm --optimize_out_type=naive_buffer
# Convert the V2.0 orientation classifier model
./opt --model_file=./ch_ppocr_mobile_v2.0_cls_slim_infer/inference.pdmodel --param_file=./ch_ppocr_mobile_v2.0_cls_slim_infer/inference.pdiparams --optimize_out=./ch_ppocr_mobile_v2.0_cls_slim_opt --valid_targets=arm --optimize_out_type=naive_buffer
```

## Demo Code Introduction

First, we provide an overview of the OCR text recognition demo's code structure, then briefly introduce the functions of each part from both Java and C++ sides.

<p align="center"><img width="300" height="500" src="https://paddlelite-demo.bj.bcebos.com/demo/ocr/docs_img/android/ppocr_android_app.jpg"/></p>

1. `PaddleLite/`: Contains the PaddleLite prediction library.

**Note:** If you need to update the prediction library, such as updating the Android v8 dynamic library `so`, update the new dynamic library `so` in the `PaddleLite/cxx/libs/armv64-v8a` directory.

2. `OpenCV/`: Contains the OpenCV prediction library.

3. `assets/`: Contains the OCR demo's models, test images, label files, and config files.

**Note:**

- `./assets/ppocr_keys_v1.txt` is the Chinese dictionary file. If you are using an English, numeric, or other language model, replace it with the corresponding language dictionary.
- Dictionary files for other languages can be downloaded from the PaddleOCR repository: https://github.com/PaddlePaddle/PaddleOCR/tree/release/2.3/ppocr/utils

4. `./src/main/cpp`: Contains the C++ prediction code.
   - `cls_process.cc`: Full pipeline for the orientation classifier, including preprocessing, prediction, and post-processing.
   - `rec_process.cc`: Full pipeline for the CRNN recognition model, including preprocessing, prediction, and post-processing.
   - `det_process.cc`: Full pipeline for the CRNN detection model, including preprocessing, prediction, and post-processing.
   - `

ppredictor.cc`: Full pipeline for the prediction module, including preprocessing, prediction, and post-processing.

5. `./src/main/java/com/baidu/paddle/ppocr`: Contains the Java UI code.
   - `MainActivity.java`: UI code for the main activity.
   - `Predictor.java`: Java code for PaddleLite prediction.
