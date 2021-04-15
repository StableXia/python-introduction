height = float(input("输入身高："))  # 输入身高
weight = float(input("输入体重："))  # 输入体重
bmi = weight / (height * height)  # 计算BMI指数

if bmi < 18.5:
    print("BMI指数为：" + str(bmi))  # 输出BMI指数
    print("体重过轻")
