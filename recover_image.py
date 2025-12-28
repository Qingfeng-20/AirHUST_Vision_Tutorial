import numpy as np
import cv2
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="从逗号分隔的像素文本文件恢复图像")
    parser.add_argument("input", help="输入的 .txt 像素文件路径")
    parser.add_argument("--rows", type=int, required=True, help="图像高度（行数）")
    parser.add_argument("--cols", type=int, required=True, help="图像宽度（列数）")
    parser.add_argument("--channels", type=int, default=3, choices=[1, 3], help="通道数（1=灰度, 3=彩色）")
    parser.add_argument("--output", default="recovered.png", help="输出图像路径")
    
    args = parser.parse_args()

    # 读取文件，逐行处理
    all_pixels = []
    with open(args.input, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith('#'):  # 跳过注释行
                continue
            if not line:  # 跳过空行
                continue
            # 按逗号分割，转为整数
            try:
                row_pixels = [int(x) for x in line.split(',')]
                all_pixels.extend(row_pixels)
            except ValueError as e:
                print(f"解析行失败: {line[:50]}... ({e})")
                sys.exit(1)

    # 转换为 NumPy 数组
    pixels = np.array(all_pixels, dtype=np.uint8)

    expected_size = args.rows * args.cols * args.channels
    if pixels.size != expected_size:
        print(f"❌ 像素数量不匹配！")
        print(f"  期望: {expected_size}（{args.rows} × {args.cols} × {args.channels}）")
        print(f"  实际: {pixels.size}")
        sys.exit(1)

    # 重塑为图像
    if args.channels == 1:
        image = pixels.reshape((args.rows, args.cols))
    else:
        image = pixels.reshape((args.rows, args.cols, args.channels))

    # 显示
    cv2.imshow("Recovered Image", image)
    print("✅ 图像已加载，按任意键关闭窗口...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 保存
    success = cv2.imwrite(args.output, image)
    if success:
        print(f"✅ 图像已成功保存至: {args.output}")
    else:
        print(f"❌ 保存失败！请检查输出路径是否可写。")

if __name__ == "__main__":
    main()