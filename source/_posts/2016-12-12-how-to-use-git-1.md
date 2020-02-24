---
title: Git从零开始 使用技巧1–快捷命令配置
date: 2016-12-12 12:25:21
tags:
- git
- alias
- shell
---

当下载好Git后，需要进行一些常用的初始化配置，例如：快捷命令的配置，git环境的配置等。这里，我把常用的需要配置的命令列举在下面。

```bash
#配置使用git仓库的人员姓名
git config --global user.name "Your Name Comes Here"
 
#配置使用git仓库的人员email
git config --global user.email "you@yourdomain.example.com"
 
#配置到缓存 默认15分钟
git config --global credential.helper cache
 
#修改缓存时间
git config --global credential.helper 'cache --timeout=3600'
 
git config --global color.ui true
git config --global alias.co checkout
git config --global alias.ci commit
git config --global alias.st status
git config --global alias.br branch
git config --global core.editor "vim" # 设置Editor使用textmate
 
#开启git的diff 3
git config --global merge.conflictstyle diff3

#设置git lg format log
git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
```