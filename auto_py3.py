# coding: utf-8
import sys

comp = [
"総蛋白",
"アルブミン",
"CK",
"AST",
"ALT",
"LD",
"ALP",
"γ-GTP",
"CRP",
"Cre",
"尿酸",
"BUN",
"血清血糖",
"中性脂肪",
"T-chol",
"HDL-chol",
"LDL-chol",
"Na",
"K",
"Cl",
"Ca",
"P",
"T-bil",
"D-bil",
"BNP",
"HbA1c",
"グリコアルブミン",
"WBC",
"RBC",
"Hb",
"Ht",
"Plt",
"MCV",
"MCHC",
"好塩基球",
"好酸球",
"好中球",
"桿状",
"分葉",
"新FDP定量",
"D-dimer",
"PT-INR",
"APTT-time",
"フィブリノゲン",
"アンチトロンビンⅢ",
"HBsAg（定量）",
"HCVAb(Index)",
"RPR定性（LA法）",
"梅毒TP定性",
"ケトン体",
"潜血",
"ウロビリノゲン",
"白血球",
"亜硝酸塩",
"赤血球",
"白血球",
"偏平上皮細胞",
"eGFR"
] #component



unit = [
"g/dL",
"g/dL",
"IU/L",
"IU/L",
"IU/L",
"U/L",
"mg/dL",
"IU/L",
"mg/dL",
"mg/dL",
"mg/dL",
"mg/dL",
"mg/dL",
"mg/dL",
"mg/dL",
"mg/dL",
"mg/dL",
"mEq/L",
"mEq/L",
"mEq/L",
"mg/dL",
"mg/dL",
"mg/dL",
"mg/dL",
"pg/mL",
"%",
"%",
"×10^2 /μL",
"×10^4/μL",
"g/dL",
"%",
"×10^4 /μL",
"fl",
"%",
"%",
"%",
"%",
"%",
"μ g/mL",
"μ g/mL",
"μ g/mL",
"null",
"sec",
"mg/dL",
"%",
"IU/mL",
"S/CO",
"R.U.",
"T.U.",
"null",
"null",
"null",
"null",
"null",
"/HPF",
"/HPF",
"/HPF",
"ml/min"
]
print("成分の種類は"+str(len(comp)))

value = []

for i in range(len(comp)):
    print(comp[i])
    x = input()
    if len(x) == 0:
        value.append("null")
    else:
        value.append(x)
    #value.append(x)

flag = 0
cnt = len(value) - 1
while flag == 0:
    if value[cnt] != "null":
        flag = 810
    else:
        cnt = cnt - 1

print("値がnullでない最後の成分は"+comp[cnt])

print("-------------------------------------------------------")

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

print("-------------------------------------------------------")

"""
総蛋白
アルブミン
CK
AST
ALT
LD
ALP
γ-GTP
CRP
Cre
尿酸
BUN
血清血糖
中性脂肪
T-chol
HDL-chol
LDL-chol
Na
K
Cl
Ca
P
T-bil
D-bil
BNP
HbA1c
グリコアルブミン
WBC
RBC
Hb
Ht
Plt
MCV
MCHC
好塩基球
好酸球
好中球
桿状
分葉
新FDP定量
D-dimer
PT-INR
APTT-time
フィブリノゲン
アンチトロンビンⅢ
HBsAg（定量）
HCVAb(Index)
RPR定性（LA法）
梅毒TP定性
ケトン体
潜血
ウロビリノゲン
白血球
亜硝酸塩
赤血球
白血球
偏平上皮細胞
eGFR
"""


"""
g/dL
g/dL
IU/L
IU/L
IU/L
U/L
mg/dL
IU/L
mg/dL
mg/dL
mg/dL
mg/dL
mg/dL
mg/dL
mg/dL
mg/dL
mg/dL
mEq/L
mEq/L
mEq/L
mg/dL
mg/dL
mg/dL
mg/dL
pg/mL
%
%
×10^2 /μL
×10^4/μL
g/dL
%
×10^4 /μL
fl
%
%
%
%
%
μ g/mL
μ g/mL
μ g/mL

sec
mg/dL
%
IU/mL
S/CO
R.U.
T.U.





/HPF
/HPF
/HPF
ml/min
"""

