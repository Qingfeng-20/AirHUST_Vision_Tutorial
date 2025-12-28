// image_io.h
#ifndef IMAGE_IO_H
#define IMAGE_IO_H

#include <opencv2/opencv.hpp>
#include <string>

// 读取图像
cv::Mat readImage(const std::string& filePath);

// 显示图像（窗口名 + 图像）
void showImage(const std::string& windowName, const cv::Mat& image);

// 保存图像
bool saveImage(const std::string& filePath, const cv::Mat& image);

#endif // IMAGE_IO_H