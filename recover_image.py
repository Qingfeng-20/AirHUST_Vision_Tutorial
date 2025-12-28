import numpy as np
import cv2
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="从纯像素值文本文件恢复图像")
    parser.add_argument("input", help="输入的 .txt 像素文件路径")
    parser.add_argument("--rows", type=int, required=True, help="图像高度（行数）")
    parser.add_argument("--cols", type=int, required=True, help="图像宽度（列数）")
    parser.add_argument("--channels", type=int, default=1, choices=[1, 3], help="通道数（1=灰度, 3=彩色）")
    parser.add_argument("--output", default="recovered.png", help="输出图像路径")
    
    args = parser.parse_args()

    try:
        # 使用 np.loadtxt 安全读取所有整数（自动跳过空行，支持大文件）
        pixels = np.loadtxt(args.input, dtype=np.uint8)
    except UnicodeDecodeError:
        # 如果编码出错，尝试指定 UTF-8（虽然 np.loadtxt 通常不受影响）
        try:
            pixels = np.loadtxt(args.input, dtype=np.uint8, encoding='utf-8')
        except Exception as e:
            print(f"读取文件失败：{e}")
            sys.exit(1)
    except Exception as e:
        print(f"读取文件出错：{e}")
        sys.exit(1)

    expected_size = args.rows * args.cols * args.channels
    if pixels.size != expected_size:
        print(f"错误：像素数量不匹配！")
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
    print("按任意键关闭窗口...")
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