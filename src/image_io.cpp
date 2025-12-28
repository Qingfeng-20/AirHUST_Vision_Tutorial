// image_io.cpp
// image_io.h
#ifndef IMAGE_IO_H
#define IMAGE_IO_H

#include <string>
#include <opencv2/opencv.hpp>

cv::Mat readImage(const std::string& filePath);
void showImage(const std::string& windowName, const cv::Mat& image);
bool saveImage(const std::string& filePath, const cv::Mat& image);

#endif // IMAGE_IO_H
#include <iostream>

cv::Mat readImage(const std::string& filePath) {
    cv::Mat img = cv::imread(filePath, cv::IMREAD_COLOR);
    if (img.empty()) {
        std::cerr << "Error: Could not read image from " << filePath << std::endl;
    }
    return img;
}

void showImage(const std::string& windowName, const cv::Mat& image) {
    if (image.empty()) {
        std::cerr << "Error: Cannot display empty image." << std::endl;
        return;
    }
    cv::imshow(windowName, image);
    cv::waitKey(0); // 等待按键
    cv::destroyAllWindows();
}

bool saveImage(const std::string& filePath, const cv::Mat& image) {
    if (image.empty()) {
        std::cerr << "Error: Cannot save empty image." << std::endl;
        return false;
    }
    return cv::imwrite(filePath, image);
}