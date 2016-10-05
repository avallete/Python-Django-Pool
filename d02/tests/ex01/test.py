from intern import Intern

anon_intern = Intern()
mark = Intern(Name='Mark')

print(anon_intern)
print(mark)

anon_coffee = anon_intern.make_coffee()
mark_coffee = mark.make_coffee()

print(anon_coffee)
print(mark_coffee)

try:
    anon_intern.work()
except Exception as e:
    print(e)

try:
    mark.work()
except Exception as e:
    print(e)