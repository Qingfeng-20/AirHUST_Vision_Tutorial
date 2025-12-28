import cv2
import numpy as np

def analyze_and_fix_channel_swap(input_path, output_path):
    # 1. 读取图像
    img = cv2.imread(input_path)
    if img is None:
        raise FileNotFoundError(f"无法读取图像: {input_path}")
    print(f"图像尺寸: {img.shape}")
    print("图像读取成功。")

    # 2. 显示原始图像，让用户观察异常区域
    cv2.imshow("Original Image (Look for color anomalies)", img)
    print("请观察图像中颜色异常的区域（例如：人脸发蓝、天空发红等）")
    print("按 'q' 关闭窗口并继续...")
    while True:
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
    cv2.destroyAllWindows()

    # 3. 手动指定异常区域坐标（示例：假设异常区域在 [y1:y2, x1:x2]）
    # 你可以根据实际图像调整以下坐标
    y1, y2 = 150, 350  # 示例：从第150行到350行
    x1, x2 = 200, 400  # 示例：从第200列到400列

    print(f"正在处理异常区域: [{y1}:{y2}, {x1}:{x2}]")

    # 4. 提取该区域
    roi = img[y1:y2, x1:x2].copy()  # 复制一份，避免修改原图

    # 5. 分离通道（OpenCV 默认是 BGR）
    b, g, r = cv2.split(roi)

    # 6. 尝试不同通道排列组合，找到最“正常”的视觉效果
    # 我们尝试所有 6 种排列：
    channel_orders = [
        ("BGR", b, g, r),      # 原始顺序（可能就是错的）
        ("RGB", r, g, b),      # 常见错误：BGR -> RGB
        ("RBG", r, b, g),
        ("BRG", b, r, g),
        ("GBR", g, b, r),
        ("GRB", g, r, b),
    ]

    best_order_name = "BGR"
    best_roi = roi.copy()
    best_score = -1

    for name, ch1, ch2, ch3 in channel_orders:
        fixed_roi = cv2.merge([ch1, ch2, ch3])
        # 简单评估：计算绿色通道均值（人脸/皮肤通常绿色适中）
        # 或者你可以手动观察哪个最自然
        green_mean = np.mean(fixed_roi[:, :, 1])  # G通道均值
        red_mean = np.mean(fixed_roi[:, :, 2])    # R通道均值
        blue_mean = np.mean(fixed_roi[:, :, 0])   # B通道均值

        # 简单启发式评分：皮肤区域通常 R > G > B
        score = red_mean - blue_mean  # 红色越突出越好（对人脸）
        if score > best_score:
            best_score = score
            best_order_name = name
            best_roi = fixed_roi

        # 可选：显示每个排列供你人工判断（取消注释即可）
        # cv2.imshow(f"Try: {name}", fixed_roi)
        # cv2.waitKey(0)

    print(f"✅ 推荐通道顺序: {best_order_name}")
    print(f"   修复后区域绿色通道均值: {np.mean(best_roi[:,:,1]):.2f}")
    print(f"   修复后区域红色通道均值: {np.mean(best_roi[:,:,2]):.2f}")

    # 7. 应用最佳通道顺序到原图的 ROI 区域
    img[y1:y2, x1:x2] = best_roi

    # 8. 显示修复后的图像
    cv2.imshow("Fixed Image", img)
    print("修复完成！按任意键关闭窗口...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 9. 保存修复后的图像
    success = cv2.imwrite(output_path, img)
    if success:
        print(f"✅ 图像已保存至: {output_path}")
    else:
        print(f"❌ 图像保存失败！")

if __name__ == "__main__":
    input_image = "processed_lena.jpg"   # 你的输入文件名
    output_image = "fixed_lena.jpg"      # 输出文件名

    try:
        analyze_and_fix_channel_swap(input_image, output_image)
    except Exception as e:
        print(f"❌ 错误: {e}")