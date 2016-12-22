---
title: mac终端_设置/查看/删除环境变量
date: 2016-12-12 12:21:26
tags:
- macOS
- environment
- http_proxy
---


设置环境变量：

```bash
export https_proxy='https://127.0.0.1:8087'
```

或

```bash
export http_proxy='http://127.0.0.1:8087'
```

查看环境变量：

```bash
export
```

删除环境变量：

```bash
unset http_proxy
```

或：

```bash
unset https_proxy
```

