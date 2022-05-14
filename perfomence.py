import pandas as pd
import csv
import plotly.express as px
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
df = pd.read_csv("StudentsPerformance.csv")
#print(df)
marks = df["math score"].tolist()
#print(height)
mean = statistics.mean(marks)
median = statistics.median(marks)
sd = statistics.stdev(marks)
mode = statistics.mode(marks)
print(mean,median,mode,sd)
fsds,fsde = mean-sd , mean+sd
ssds,ssde = mean-(2*sd) , mean+(2*sd)
tsds,tsde = mean-(3*sd) , mean+(3*sd)
fig = ff.create_distplot([marks],["result"],show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.022],mode = "lines", name = "mean" ))
fig.add_trace(go.Scatter(x = [fsds,fsds],y = [0,0.022],mode = "lines", name = "fsds" ))
fig.add_trace(go.Scatter(x = [fsde,fsde],y = [0,0.022],mode = "lines", name = "fsde" ))
fig.add_trace(go.Scatter(x = [ssds,ssds],y = [0,0.022],mode = "lines", name = "ssds" ))
fig.add_trace(go.Scatter(x = [ssde,ssde],y = [0,0.022],mode = "lines", name = "ssde" ))
fig.add_trace(go.Scatter(x = [tsds,tsds],y = [0,0.025],mode = "lines", name = "tsds" ))
fig.add_trace(go.Scatter(x = [tsde,tsde],y = [0,0.025],mode = "lines", name = "tsde" ))
fig.show()
data1 = [result for result in marks if result>fsds and result<fsde]
data2 = [result for result in marks if result>ssds and result<ssde]
data3 = [result for result in marks if result>tsds and result<tsde]
percentage1 = len(data1)*100/len(marks)
percentage2 = len(data2)*100/len(marks)
percentage3 = len(data3)*100/len(marks)
print(percentage1,percentage2,percentage3)
