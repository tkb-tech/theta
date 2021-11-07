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

flag = 0
cnt = len(value) - 1
while flag == 0:
    if value[cnt] != "null":
        flag = 810
    else:
        cnt = cnt - 1

print(cnt)

print("--------------------------------------------")

for i in range(cnt):
    if value[i] != "null":
        if unit[i] != "null":
            sys.stdout.write(comp[i]+" "+value[i]+" "+unit[i]+", ")
        else:
            sys.stdout.write(comp[i]+" "+value[i]+", ")

if value[cnt] != "null":
    if unit[cnt] != "null":
        print(comp[cnt]+" "+value[cnt]+" "+unit[cnt])
    else:
        print(comp[cnt]+" "+value[cnt])

print("--------------------------------------------")

