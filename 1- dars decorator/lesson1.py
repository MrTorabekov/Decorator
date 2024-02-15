
# Decorator funcsiyani ozgartiradi va mukammalashtiradi
#closure deb ichma ich ochilgan funcsiyaga aytiladi
def hello(name):
    def get_name():
        return f"salom😅 {name}"

    return get_name()

s = hello("Akobir")
print(s)