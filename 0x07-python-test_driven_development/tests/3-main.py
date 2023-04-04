#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("Alene", "Lamesgin")
say_my_name("kebede", "Asefa")
say_my_name("Tom")
try:
    say_my_name(12, "Asefa")
except Exception as e:
    print(e)
