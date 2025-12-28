#include "image_io.h"
#include <iostream>

int main() {
    // ⚠️ 请根据你的 .txt 文件修改以下参数！
    std::string txtPath = "data/input_image.txt";  // ← 你的像素文本文件
    int rows = 480;    // ← 图像高度（必须已知）
    int cols = 640;    // ← 图像宽度（必须已知）
    int channels = 3;  // ← 1=灰度, 3=彩色

    std::string outputPath = "data/output/recovered_image.png";

    // 1. 从 .txt 恢复图像
    cv::Mat recovered = loadImageFromTxt(txtPath, rows, cols, channels);
    if (recovered.empty()) {
        return -1;
    }

    // 2. 显示
    showImage("Recovered Image", recovered);

    // 3. 保存
    if (saveImage(outputPath, recovered)) {
        std::cout << "Recovered image saved to " << outputPath << std::endl;
    } else {
        std::cerr << "Failed to save recovered image!" << std::endl;
        return -1;
    }

    return 0;
}