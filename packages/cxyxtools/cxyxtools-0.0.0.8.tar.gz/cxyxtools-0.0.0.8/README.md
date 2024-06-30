# cxyx_tools

#### 介绍
python 工具类

#### 软件架构
软件架构说明


#### 安装教程

1.  pip install cxyxtools



#### 使用说明

```
目前已支持:
    1 梯度下降方式,求解 int,float,枚举类型变量最优解,使得方法得到最小值
      使用方式:
        from cxyx_tools.core.variable import BorderLessFloatVariable, EnumVariable
        from cxyx_tools.core.gradient import gradient_wrapper, Variable
        @gradient_wrapper(round_number=1000)
        def f(y: Variable, x: Variable, z: Variable, t: int):
            sumu = 0
            for i in range(100000):
                sumu += i
            return (x.get_val() - 5) ** 2 + (y.get_val() - 10) ** 2 + (
                    z.get_val() - 9 - x.get_val()) ** 2 + sumu


        t = time.time()

        r = f(BorderLessFloatVariable(0, 0.01), BorderLessFloatVariable(2, 0.01),
          z=EnumVariable([1, 3], 1), t=5)
        print(f"耗时 : %s s" % (
            time.time() - t))
        print(r)
      #############################################################
        耗时 : 1.5787789821624756 s
        最终解
        最小值	: 4999950060.50005
        args	:[9.99992919921875, -0.5049972534179688]
        kwargs	:{'z': 3, 't': 5}

```

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request


#### 特技

1.  使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2.  Gitee 官方博客 [blog.gitee.com](https://blog.gitee.com)
3.  你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解 Gitee 上的优秀开源项目
4.  [GVP](https://gitee.com/gvp) 全称是 Gitee 最有价值开源项目，是综合评定出的优秀开源项目
5.  Gitee 官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6.  Gitee 封面人物是一档用来展示 Gitee 会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)
