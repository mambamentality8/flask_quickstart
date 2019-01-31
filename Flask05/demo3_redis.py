from redis import StrictRedis

# 实例化连接redis对象
# redis_client = StrictRedis(host='',port=6379,db=1)
# 修改响应的数据为字符串,decode_responses表示解码响应为string类型，如果不写，默认bytes。
redis_client = StrictRedis(decode_responses=True)

# 操作数据库,存入字符串；setex/get/delete
redis_client.set('hello','world')

# 查询数据，取出后是bytes类型
print(redis_client.get('hello'))

