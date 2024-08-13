import redis


r_cache = redis.Redis(host='localhost', port=6379, decode_responses=True)
#
# def cache_deco(func):
#     def wraper(num, *args, **kwargs):
#         if r_cache.exists(num):
#             print(f'Cache {num} exists')
#             return r_cache.get(num)
#
#         print(f'Calculations for {num}')
#         result = func(num, *args, **kwargs)
#         r_cache.set(num, result, ex=100)
#         return result
#     return wraper
#
#
# @cache_deco
# def factorial(num):
    # if r_cache.exists(num):     вместо этого используем декоратор
    #     print(f'CAche used for {num}')
    #     return r_cache.get(num)
    # else:
    #     print(f'Calculating for {num}')

    # if num == 0:
    #     return 1
    # else:
    #     return  num * factorial(num - 1)
        # r_cache.set(num, result, ex=5)
        # return result



# if __name__ == '__main__':
#    res = factorial(5)

#
#
#
def cache_fibo(func):
    def wraper(num, *args, **kwargs):
        if r_cache.exists(num):
            print(f'Cache {num} exists')
            return r_cache.get(num)

        print(f'Calculations for {num}')
        result = func(num, *args, **kwargs)
        r_cache.set(num, result, ex=100)
        return result
    return wraper


@cache_fibo
def fibonacci(num):
    if num == 0:
        return 0
    if num == 1:
        return 1

    prev = 0
    curr = 1

    for i in range(2, num + 1):
        next = prev + curr
        prev = curr
        curr = next
    return curr
#
if __name__ == '__main__':
    for i in range(0, 50):
        print(fibonacci(i))
