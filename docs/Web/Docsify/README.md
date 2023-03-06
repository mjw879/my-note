#### 1. 介绍

    本意是利用**docsify**创建阅读markdown的网页

#### 2. 基础

1. 下载**node.js**  
   `sudo apt-get install nodejs`  
   `sudo apt-get install npm`
2. 全局安装 docsify-cli 工具  
   `npm i docsify-cli -g`
3. 初始化文档结构  
   `docsify init ./docs`
   > 初始化成功后，./docs目录下会创建以下几个文件：
   >
   > ```
   > -| docs/
   >    -| .nojekyll 用于阻止 GitHub Pages 忽略掉下划线开头的文件
   >    -| index.html 入口文件
   >    -| README.md 会做为主页内容渲染
   > ```
4. 本地实时预览
    `docsify serve ./docs`  
    > 启动一个本地服务器，可以方便地实时预览效果。默认访问地址为： http://localhost:3000

#### 1. 依赖
