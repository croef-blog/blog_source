---
title: Git从零开始 使用技巧3–简单的提交步骤
date: 2016-12-12 12:26:57
tags:
- git
- alias
- shell
---

提交修改步骤

```bash
#查看文件状态  
git st
 
#添加当前修改的文件到暂存区  
git add .  
  
#如果你自动追踪文件，包括你已经手动删除的，状态为Deleted的文件  
git add -u  
 
#提交你的修改  
git commit –m "你的注释"  
 
#拉取远程代码，同时进行rebase操作
git pull --rebase
 
#推送代码到远程分支
git push
```
