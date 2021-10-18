def generator_1(titles):
    print("第一个生成器")
    yield titles
def generator_2(titles):
    print("记录调用的次数~~")
    yield from titles

titles = ["Pyhton","Java","C++"]
# for title in generator_1(titles):
#     print("生成器1：",title)
print(next(generator_1(titles)))

a2 = generator_2(titles)
print(next(a2))
print(next(a2))
print(next(a2))


# for title in generator_2(titles):
#     print("生成器2：",title)






















