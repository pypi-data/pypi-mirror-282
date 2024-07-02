

## 安装sqldrafter

`pip install --upgrade sqldrafter`

 ## 初始化数据源配置
```
sqldrafter init
```
## 创建私有空间
```
sqldrafter createSpace
```
初始化私有空间，并返回空间ID 
## 初始化表schema
引入表schema 到空间中，并生成一个excel到本地
```
sqldrafter gen <spaceid> <table1> <table2> ...
```

## 更新Schema
通过更新本地文件，更新表信息到sqldrafter
```
sqldrafter update <filename>
```

## 更新指标
通过更新本地文件，更新表信息到sqldrafter
```
sqldrafter update <filename>
```

## 更新指标项

```
sqldrafter indicator <spaceId> <key> <value>
```

## text2sql 
```
sqldrafter query <spaceId> <question>
```
