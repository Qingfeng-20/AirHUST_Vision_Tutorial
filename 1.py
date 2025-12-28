import cv2

# 1. 读取图像（支持 .jpg, .png, .jpeg）
input_path = "input.png"  # 可替换为 .png 或 .jpeg 文件
image = cv2.imread(input_path)

# 检查图像是否成功加载
if image is None:
    raise FileNotFoundError(f"无法读取图像文件: {input_path}")

# 2. 显示图像
cv2.imshow("Image Display", image)
cv2.waitKey(0)  # 等待任意按键按下
cv2.destroyAllWindows()  # 关闭所有窗口

# 3. （可选）对图像做一点操作，例如转换为灰度图（也可以跳过）
# 这里我们不做任何处理，直接保存原图
# 你也可以取消注释下面两行来保存灰度图
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# image_to_save = gray_image

# 保存图像为 .jpg（也可以保存为 .png，只需更改扩展名）
output_path = "output_image.png"  # 或 "output_image.png"
success = cv2.imwrite(output_path, image)

if success:
    print(f"图像已成功保存为: {output_path}")
else:
    print("图像保存失败！")