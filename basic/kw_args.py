#!/usr/bin/env python3
# -*- coding: -utf-8 -*-

def print_scores(**kw):
	print('      Name score')
	print('----------------')
	for name,score in kw.items():
		print('%10s %d' % (name,score))

#test1
print_scores(Adam=99, Lisa=88, Bart=77)
#test2
data = {
	'Adam Lee': 99,
	'Lisa S': 88,
	'F.Bart':77
}
print_scores(**data)


def print_info(name, *, gender, city='Beijing', age):
    print('Personal Info')
    print('---------------')
    print('   Name: %s' % name)
    print(' Gender: %s' % gender)
    print('   City: %s' % city)
    print('    Age: %s' % age)
    print()
    
#test3
print_info('Bob', gender='male', age=20)
#test4
print_info('Lisa', gender='female', city='Shanghai', age=18)