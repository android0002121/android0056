'''
    不同于其它程序的新的概念协程，一个比线程更小的运行单位
    可以实现同样效果的功能
   2.greenlet:是一个由C语言实现的协程模块。通过设置switch()来实现任意函数之间的切换
    2.1 安装第三方模块
    安装:pip insta11 模块名
    卸载:pip uninstall 模块名
    查看已安装的模块:pip list
    2.2 注意:geenlet属于手动切换，当遇到I0操作，程序会阻塞，而不能进行自动切换
    2.3 通过greenlet实现任务的切换
    导入greenlet模块
    from greenlet import greenlet
'''
from greenlet import greenlet

def sing():
    print('sing.....')
    g2.switch()
    print('singed.....')

def dance():
    print('danceing .....')
    print('danceed .....')
    g1.switch()

# greenlet可以在函数中自由的进行切换,让程序进入冻结状态
if __name__=='__main__':
    g1 = greenlet(sing)
    g2 = greenlet(dance)
    g1.switch()
    g2.switch()
