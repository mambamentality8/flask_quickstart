class Config:
    DEBUG = None

# 不同环境下，需要开启或关闭调试模式
# 开发模式，调试模式开启
class DevelopmentConfig(Config):
    DEBUG = True

# 生产模式，调试模式关闭
class ProductionConfig(Config):
    DEBUG = False

# 实现配置类的字典映射
config_dict = {
    'dev':DevelopmentConfig,
    'pro':ProductionConfig
}
