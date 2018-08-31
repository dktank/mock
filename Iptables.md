# Iptables
##防火墙
- 主机防火墙：针对于单个主机进行防护。
- 网络防火墙：针对网络入口进行防护，服务于防火墙后的本地局域网。
- 当客户端访问服务器web服务是，信息会通过内核的TCP协议传输到用户空间的web服务中。防火墙的作用是在内核中设置关卡，所有进出的报文都要通过这些关卡，经过检测后，符合放行条件的才被放行，符合阻拦条件的被阻拦。即（input关卡）和（output关卡），在iptables中被称作“链”。
- 当报文经过“链”时，必须和这个关卡上的所有规则匹配一遍。
- 表：相同功能的规则的集合，iptables中定义了4种表：
- - filter表：负责过滤功能，内核模块：iptables_filter
- - nat表：全称（network address translation）网络地址转换功能；内核模块：iptable_nat
- - mangle表:拆解报文，做出修改，并重新封装；内核模块：iptable_mangle
- - raw表：关闭nat表上启用的连接追踪机制；内核模块：iptable_raw
- 四种表优先级（由高到低）：raw > mangle > nat > filter

##规则
- 概念：根据指定的匹配条件来尝试匹配每个流经此处的报文，一旦匹配成功jia将由后面的处理动作进行处理。
- 简单理解 规则 = 匹配条件+处理动作
- 匹配条件：
- - 基本匹配条件：源地址，目标地址
- - 扩展匹配条件
- 处理动作：
- - ACCEPT:允许数据包通过
- - DROP:直接丢弃数据包
- - REJECT:拒绝数据包通过
- - SNAT：源地址转换
- - DNAT:目标地址转换
- - REDIRECT:在本机做端口映射

##Iptabyles
1. netfilter是真的防火墙，位于linux内核。
2. iptables并不是真正的防火墙，是一个命令工具，位于用户空间，可以操作netfilter
3. 规则存储在内核空间的信息过滤表中，这些规则分别指定了源地址，目的地址，传输协议和服务类型等
4. iptables根据规则所定义的方法处理数据包，如放行（accept），拒绝（reject）,丢弃（drop）等。而配置防火墙就是添加、修改、删除、这些规则

##iptables管理规则：
- \-A ：在链尾添加新的规则
- \-I[n]:插入为第n条规则
- \-D ：删除规则
- \-R[n] : 替换第n条
- \-L：显示规则链中已有的条目；
- \-F：清楚规则链中已有的条目；
- \-Z：清空规则链中的数据包计算器和字节计数器；
- \-t<表>：指定要操纵的表；
- \-h：显示帮助信息；
- \-p：指定要匹配的数据包协议类型；
- \-s：指定要匹配的数据包源ip地址；
- \-j<目标>：指定要跳转的目标；
- \-i<网络接口>：指定数据包进入本机的网络接口；
-o<网络接口>：指定数据包要离开本机所使用的网络接口。
```
iptables -t 表名 <-A/I/D/R> 规则链名 [规则号] <-i/o 网卡名> -p 协议名 <-s 源IP/源子网> --sport 源端口 <-d 目标IP/目标子网> --dport 目标端口 -j 动作
```
##命令示例
- 清除已有iptables规则：iptables -F   iptables -Z
- 开放指定的端口：iptables -A INPUT -p tcp --dport 80 -j ACCEPT    #允许访问80端口
- 屏蔽IP：iptables -I INPUT -s 123.0.0.0/8 -j DROP
- 查看已添加的iptables规则：iptables -L -n -v
- 将所有iptables以序号标记显示：iptables -L -n --line-numbers
- 删除INPUT里序号为8的规则：iptables -D INPUT 8
- 使iptables规则生效：iptables-restore < /etc/iptables/rules.v4 

## AppArmor与SELinux
1. -  二者相同点：都是Linux中的强制访问控制(Mandatory Access Control)
   - 二者不同点：
       - SELinux太过复杂，apparmor的代码也更易理解和易读。
       - Apparmor使用文件名（路径名）最为安全标签，而SELinux使用文件的inode作为安全标签（在文件系统中，只有inode才具有唯一性）
       - SELinux更安全
2. Apparmor
- Apparmor有两种工作模式
     - Enforcement ： 在这种模式下，配置文件里列出的限制条件都会得到执行，并且对于违反这些限制条件的程序会进行日志记录。
     - Complain ： 在这种模式下，配置文件里的限制条件不会得到执行，Apparmor只是对程序的行为进行记录。





