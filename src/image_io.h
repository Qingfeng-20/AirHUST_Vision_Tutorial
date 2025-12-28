#ifndef IMAGE_IO_H
#define IMAGE_IO_H

#include <opencv2/opencv.hpp>
#include <string>

// 从文本文件恢复图像
cv::Mat loadImageFromTxt(const std::string& txtPath, int rows, int cols, int channels);

// 保存图像（不变）
bool saveImage(const std::string& filePath, const cv::Mat& image);

// 显示图像（不变）
void showImage(const std::string& windowName, const cv::Mat& image);

#endif // IMAGE_IO_H