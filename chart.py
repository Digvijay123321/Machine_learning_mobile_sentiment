from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.plotting import figure
from bokeh.transform import dodge
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="your_user_name",
  password="your_password",
  database="database_name",
)

mycursor = mydb.cursor(buffered=True)


query_mobile = "select name from negative ORDER BY name"


mycursor.execute(query_mobile)
m_lt = mycursor.fetchall()
mobiles = [item for t in m_lt for item in t]

def draw_graph(feature):
    output_file("./feat/{}.html".format(feature))
    query_positive = "select {} from positive ORDER BY name"
    query_negative = "select {} from negative ORDER BY name"
    
    mycursor.execute(query_positive.format(feature))
    p_lt = mycursor.fetchall()
    p_list = [item for t in p_lt for item in t]
    
    mycursor.execute(query_negative.format(feature))
    n_lt = mycursor.fetchall()
    n_list = [item for t in n_lt for item in t]
    
    sentiment = ['Positive', 'Negative']

    data = {'mobiles' : mobiles,
        'Positive'   : p_list,
        'Negative'   : n_list}

    source = ColumnDataSource(data=data)

    max_all = max(data['Positive'] + data['Negative'])

    p = figure(x_range=mobiles, y_range=(0, max_all+2), plot_height=550, plot_width=1500, title=feature.capitalize(),
           toolbar_location="below")
    p.title.text_font_size = '30pt'

    p.vbar(x=dodge('mobiles',  0.0,  range=p.x_range), top='Positive', width=0.2, source=source,
       color="#718dbf", legend_label="Positive")


    p.vbar(x=dodge('mobiles',  0.25, range=p.x_range), top='Negative', width=0.2, source=source,
       color="#e84d60", legend_label="Negative")


    p.add_tools(HoverTool(tooltips=[("Positive review", "@Positive"), ("Negative review", "@Negative")]))

    p.x_range.range_padding = 0.1
    p.xgrid.grid_line_color = None
    p.legend.location = "top_left"
    p.legend.orientation = "horizontal"

    show(p)