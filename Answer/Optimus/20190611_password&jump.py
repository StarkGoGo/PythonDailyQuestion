# 给用户三次输入用户名和密码的机会，要求如下：‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬
# 1）如输入第一行输入用户名为‘Kate’, 第二行输入密码为‘666666’，输出‘登录成功！’，退出程序；‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬
# 2）当一共有3次输入用户名或密码不正确输出“3
# 次用户名或者密码均有误！退出程序。”。

def userPasswd():
    num2 = 0
    for i in range(0,3):
        username = input('请输入用户名：')
        userPassword = input('输入密码：')
        if username == "kate" and userPassword == "666666":
            print("登录成功！")
            break
        else:
            num2 +=1
            if num2 >=3:
                print("3次用户名或者密码均有误！退出程序。")
            continue
userPasswd()



# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。
# 求该青蛙跳上一个n级的台阶总共有多少种跳法
# 注：先后次序不同 算作是不同的结果
def jumps(n):
    if n ==1:
        return 1
    if n==2:
        return 2
    return jumps(n-1)+jumps(n-2)
print(jumps(4))