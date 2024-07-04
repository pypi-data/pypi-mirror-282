import subprocess
from io import StringIO
import pandas as pd
import numpy as np
eye_output = ""
delay_setting = {}
eye_width = {}
import re
#yarr_output = subprocess.getoutput('emulator-eye-diagram')
yarr_output = open('eye-diagram.log').read()

ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
yarr_output_cleaned = ansi_escape.sub('', yarr_output)

for line in yarr_output_cleaned.splitlines(keepends=True):
    if line.count("|") >= 16:
        eye_output += (
            line.replace("\033[32m", "")
            .replace("\033[0m", "")
            .replace("| \n", "\n")
        )
    if "[  info  ][  eyeDiagram   ]" in line and "lane" in line:
        lane = line.split("lane ")[1].split(" ")[0].replace("\n", "")
        if "Delay setting" in line:
            values = line.split("eye width ")[1].replace("\n", "")
            eye_width[lane] = int(float(values.split(": ")[0]))
            delay_setting[lane] = int(float(values.split(": ")[1]))
        else:
            eye_width[lane] = 0
            delay_setting[lane] = 0

colnames = ["Delay"] + [f"lane{i}" for i in range(16)]
testdata = pd.read_csv(
    StringIO(eye_output), sep="|", names=colnames, header=None, index_col=False
)

dtype = [(colname, np.int64 if i==0 else np.float64) for i,colname in enumerate(colnames)]
split_where = yarr_output_cleaned.index('[')
testdata2 = np.genfromtxt(StringIO(yarr_output_cleaned[:split_where]), delimiter='|', usecols=np.arange(len(colnames)), dtype=dtype)

for colname in colnames:
    assert list(testdata[colname]) == list(testdata2[colname])
breakpoint()
print(testdata)
