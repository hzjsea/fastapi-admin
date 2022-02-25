# fastapi-admin
fastapi-admin



## Project structure 

```
- DockerFile
- Docker-compose
- app.pyproject.toml 项目配置文件，定义项目在不同环境下的启动参数
```


- app
  - models 数据库映射到成程序当中的model层
  - schemas 各种在请求过程中产生或需要的消息类
  - settings 各种配置内容，单例模式统一出口
  - tests 测试类文件夹
  - utils 工具类文件夹
  - logsX 日志
  - db 数据库连接 等等 fastapi 对数据库连接采用依赖注入的方式，每次请求都是一条新的数据库连接， 请求关闭之后连接断开并被丢弃
  - crud 抽离业务逻辑层， 具体是否需要要开具体的场景和需求