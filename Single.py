class Single(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):  # （hasattr判断里面有没有某个属性或者方法）
            cls._instance = super().__new__(cls)  # python2里这样使用super(Single, cls).__new__(cls)
        return cls._instance


single1 = Single()
single2 = Single()
print(id(single1))
print(id(single2))
