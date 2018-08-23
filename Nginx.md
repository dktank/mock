# Nginx

##Nginx简介
- Nginx 是俄罗斯人编写的十分轻量级的 HTTP 服务器
- Nginx 以事件驱动的方式编写，所以有非常好的性能，同时也是一个非常高效的反向代理、负载平衡。
- 拥有匹敌 Lighttpd 的性能，同时还没有 Lighttpd 的内存泄漏问题，而且 Lighttpd 的 mod_proxy 也有一些问题并且很久没有更新。

##Nginx特点
- 处理静态文件，索引文件以及自动索引；打开文件描述符缓冲．
- 无缓存的反向代理加速，简单的负载均衡和容错．
- FastCGI，简单的负载均衡和容错．
- 模块化的结构。包括 gzipping, byte ranges, chunked responses,以及 SSI-filter 等 filter。如果由 FastCGI 或其它代理服务器处理单页中存在的多个 SSI，则这项处理可以并行运行，而不需要相互等待。
- 支持 SSL 和 TLSSNI．

##Nginx架构
1. 概要
    - Nginx 在启动后，在 unix 系统中会以 daemon 的方式在后台运行，后台进程包含一个 master 进程和多个 worker 进程。
    - master 进程主要用来管理 worker 进程，包含：接收来自外界的信号，向各 worker 进程发送信号，监控 worker 进程的运行状态，当 worker 进程退出后(异常情况下)，会自动重新启动新的 worker 进程。
    -  worker 进程处理基本网络事件。
    -  一个请求，只可能在一个 worker 进程中处理，一个 worker 进程，不可能处理其它进程的请求。
    -  worker 进程的个数一般设置为机器cpu核数。
    -  每个 worker 里面只有一个主线程，Nginx 采用了异步非阻塞的方式来处理请求解决高并发。
    -  所有 worker 进程在注册 listenfd 读事件前抢 accept_mutex，抢到互斥锁的那个进程注册 listenfd 读事件，在读事件里调用 accept 接受该连接。当一个 worker 进程在 accept 这个连接之后，就开始读取请求，解析请求，处理请求，产生数据后，再返回给客户端，最后才断开连接，这样保证了一个请求，完全由 worker 进程来处理，且只在一个 worker 进程中处理。

    #####这样做的好处：
    - 对于每个 worker 进程来说，独立的进程省掉了锁带来的开销
    - 一个进程退出后，其它进程还在工作，服务不会中断，master 进程则很快启动新的 worker 进程。
    - worker 进程的异常退出，会导致当前 worker 上的所有请求失败，不过不会影响到所有worker请求，所以降低了风险。
2. Nginx概念









