// main.cpp
#include "image_io.h"
#include <iostream>

int main() {
    // 👇 选择你想读的图片（根据你 data/ 下的文件）
    std::string inputPath = "data/hesiqi.png";      // 或 "data/ranjinle.jpg"
    std::string outputPath = "data/output/result.png"; // 保存为 PNG（也可 .jpg）

    // 1. 读取
    cv::Mat img = readImage(inputPath);
    if (img.empty()) {
        return -1;
    }

    // 2. 显示
    showImage("Loaded Image", img);

    // 3. 保存（不做处理，直接保存）
    if (saveImage(outputPath, img)) {
        std::cout << "Image saved to " << outputPath << std::endl;
    } else {
        std::cerr << "Failed to save image!" << std::endl;
        return -1;
    }

    return 0;
}