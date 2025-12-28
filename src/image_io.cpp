#include "image_io.h"
#include <fstream>
#include <iostream>
#include <sstream>

cv::Mat loadImageFromTxt(const std::string& txtPath, int rows, int cols, int channels) {
    std::ifstream file(txtPath);
    if (!file.is_open()) {
        std::cerr << "Error: Cannot open file " << txtPath << std::endl;
        return cv::Mat();
    }

    // 确定 OpenCV 类型
    int type;
    if (channels == 1) {
        type = CV_8UC1;
    } else if (channels == 3) {
        type = CV_8UC3;
    } else {
        std::cerr << "Error: Unsupported channel count: " << channels << std::endl;
        return cv::Mat();
    }

    cv::Mat img(rows, cols, type);

    if (channels == 1) {
        for (int i = 0; i < rows; ++i) {
            uint8_t* rowPtr = img.ptr<uint8_t>(i);
            for (int j = 0; j < cols; ++j) {
                int val;
                if (!(file >> val)) {
                    std::cerr << "Error: Not enough data in file!" << std::endl;
                    return cv::Mat();
                }
                rowPtr[j] = static_cast<uint8_t>(val);
            }
        }
    } else if (channels == 3) {
        for (int i = 0; i < rows; ++i) {
            cv::Vec3b* rowPtr = img.ptr<cv::Vec3b>(i);
            for (int j = 0; j < cols; ++j) {
                int b, g, r;
                if (!(file >> b >> g >> r)) {
                    std::cerr << "Error: Not enough data in file!" << std::endl;
                    return cv::Mat();
                }
                rowPtr[j] = cv::Vec3b(static_cast<uchar>(b), static_cast<uchar>(g), static_cast<uchar>(r));
            }
        }
    }

    file.close();
    return img;
}

bool saveImage(const std::string& filePath, const cv::Mat& image) {
    if (image.empty()) {
        std::cerr << "Error: Cannot save empty image." << std::endl;
        return false;
    }
    return cv::imwrite(filePath, image);
}

void showImage(const std::string& windowName, const cv::Mat& image) {
    if (image.empty()) {
        std::cerr << "Error: Cannot display empty image." << std::endl;
        return;
    }
    cv::imshow(windowName, image);
    cv::waitKey(0);
    cv::destroyAllWindows();
}