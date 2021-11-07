# coding: utf-8
import sys, codecs

comp = ["総蛋白",
"アルブミン",
"CK",
"AST",
"ALT",
"γ-GTP",
"LD",
"ALP",
"CRP",
"Cre",
"BUN",
"Na",
"K",
"Cl",
"Ca",
"BNP",
"WBC",
"Hb",
"Plt",
"D-dimer",
"PT-INR",
"APTT-time"] #component

unit = [
"g/dL",
"g/dL",
"IU/L",
"IU/L",
"IU/L",
"IU/L",
"U/L",
"mg/dL",
"mg/dL",
"mg/dL",
"mg/dL",
"mEq/L",
"mEq/L",
"mEq/L",
"mg/dL",
"pg/mL",
"×10^2 /μL",
"g/dL",
"×10^4 /μL",
"μ g/mL",
"null",
"sec"
]

print(len(comp))
print(len(unit))

value = []


print('こんにちわ！')

for i in range(len(comp)):
    print(comp[i]+'のデータを入力してくださいネ')
    x = raw_input()
    print("入力値は"+str(x))
    value.append(x)

print("--------------------------------------------")

for i in range(len(comp)-1):
    if value[i] != "null":
        if unit[i] != "null":
            sys.stdout.write(comp[i]+" "+value[i]+" "+unit[i]+", ")
        else:
            sys.stdout.write(comp[i]+" "+value[i]+", ")

if value[len(comp)-1] != "null":
    if unit[len(comp)-1] != "null":
        print(comp[len(comp)-1]+" "+value[len(comp)-1]+" "+unit[len(comp)-1])
    else:
        print(comp[len(comp)-1]+" "+value[len(comp)-1])

print("--------------------------------------------")



"""
ここから下は無関係なので消しちゃってもいいです。（備忘録のために残してあるだけ）

arxiv_num = []
title = []

check = 'y'
i = 0

print('please input the date of seminar')
date = input().split('/')

while check == 'y':
    print('please input arxiv number and title of the papers.')
    x = input().split('/')
    print(x)
    print(x[0])
    arxiv_num.append(x[0])
    title.append(x[1])
    print('is there any more paper? (y/n)')
    check = input()
    i = i + 1
    
    
print(arxiv_num)
print(title)

print(
'    <tr>')
print('        <th>')

sys.stdout.write('        ')
sys.stdout.write(date[0])
sys.stdout.write('/')
print(date[1])

print(
'            </th>')

print('        <td>')


for i in range(0,len(arxiv_num)):
    print('            <br>')
    sys.stdout.write(
    '            <a href="https://arxiv.org/abs/')
    sys.stdout.write(arxiv_num[i])


    sys.stdout.write('">')
    sys.stdout.write(arxiv_num[i])
    print('</a><br>')

    sys.stdout.write('            "')
    sys.stdout.write(title[i])
    sys.stdout.write('"')

    print(
    '<br>')





print(
'        </td>')
print(
'    </tr>')


"""
