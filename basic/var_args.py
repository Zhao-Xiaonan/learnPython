#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def hello(greeting,*args):
	if(0 == len(args)):
		print('%s!' % greeting)
	else:
		print('%s,%s!' % (greeting,','.join(args)))


hello('Hi')
hello('Hi','Sara')
hello('Hello', 'Michael', 'Bob', 'Adam')

names = ('Bart', 'Lisa')
hello('Hello', *names)