from motion_detector import df
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

df["Start_string"]=df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S") #Converting datetime into string
df["End_string"]=df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds=ColumnDataSource(df)   #creating columndatasourceobject

p=figure(x_axis_type='datetime',height=100,width=500, sizing_mode="stretch_both", title="Motion Graph") #Making the layout of graph
p.yaxis.minor_tick_line_color=None       #Removing the middle numbers from y axis
p.ygrid[0].ticker.desired_num_ticks=1   #Removing grid lines


hover=HoverTool(tooltips=[("Start","@Start"),("End","@End")])   #creating hover object
p.add_tools(hover)  #adding hover tool

q=p.quad(left="Start_string", right="End_string",bottom=0,top=1,color="green",source=cds)   #mentioning the properties of the quadrant to be plotted

output_file("Graph1.html")
show(p)
