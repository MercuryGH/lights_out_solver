# 开/关灯游戏求解器

这个求解器用于求解$GF(k)$上的$nm$元线性方程组。对于最基础的关灯游戏，$n$为行数，$m$为列数，$k=2$（即只有开、关两种状态），卷积核为$\left[\begin{matrix}0 & 1 & 0 \\1 & 1 & 1 \\0 & 1 & 0 \\\end{matrix}\right]$。

## 依赖

* SageMath

## 使用方法

直接在sage环境下（Python环境也可以）运行即可，修改源代码以配置合适的问题。

## 数学原理

详见 https://www.xarg.org/2018/07/lightsout-solution-using-linear-algebra/ 

## 改进？

参考 [hackergame2021-writeups/README.md at master · USTC-Hackergame/hackergame2021-writeups (github.com)](https://github.com/USTC-Hackergame/hackergame2021-writeups/blob/master/official/%E7%81%AF%EF%BC%8C%E7%AD%89%E7%81%AF%E7%AD%89%E7%81%AF/README.md)，指定某些格子不可点击后，整个系统不再线性，需要使用其他算法解决。
