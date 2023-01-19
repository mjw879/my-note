```bash
-g # 生成调试信息,该程序可以被调试器调试
-Wall # 使能所有警告
# 其他警告类型
    -Wcomment  #出现注释嵌套时发出警告。
    -Wconversion  #如果程序中存在隐式类型转换，则发出警告。
    -Wformat  #检查printf和scanf等格式化输入输出函数的格式字符串和参数类型的匹配情况，如果发现不匹配则发出警告。
    -Winline  #如果函数不能被内联，则发出警告。
    -Wlong-long  #如果使用了long long型数据，则发出警告。
    -Wmain  #如果main函数的返回类型不是int型，或者调用main函数时使用的参数数目不正确，则发出警告。
    -Wmissing-declarations  #如果定义了全局函数，但却没有在头文件中声明，则发出警告。
    -Wparentheses  #在某些情况下，如果忽略掉了括号，则会发出警告。
    -Wreturn-type  #如果函数定义了返回类型，而默认类型是int型，编译器会发出警告。
    -Wuninitialized  #如果使用的自动变量没有被初始化，则发出警告。
    -Wundef  #如果在#if宏中使用了未定义的变量做判断，则发出警告。
    -Wunused  #如果声明的变量或static型函数没有使用，则发出警告。
```