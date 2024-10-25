import sys
from pyecharts.charts import Line
from pyecharts import options as ops

for line in sys.stdin:
    print(f"Processed: {line.strip()}")

   
