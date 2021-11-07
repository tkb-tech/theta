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

