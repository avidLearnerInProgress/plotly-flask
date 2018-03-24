from plotly.offline import plot
import plotly.graph_objs as go
from flask import Flask, render_template, send_file, make_response, Markup

app = Flask(__name__)

names = ['india', 'black money', 'gst', 'reserve bank', 'prime', 'modi', 'october', 'new path growth', 'common man', 'formal economy', 'maharashtra ahead', 'clean', 'january', 'time history', 'august']
names = names[:10]
name_keys = []
for ele in range(1,len(names)+1):
	name_keys.append(ele)
print(name_keys)
values = [10, 6, 6, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2]
values = values[:10]
	

@app.route('/results', methods=['GET', 'POST'])
def results():
		trace0 = go.Bar(
        x=name_keys,
        y=values,
        text=names,
        marker=dict(
            color='#60a1f7',
            line=dict(
                color='#302af7',
                width=2,
            )
        ),
        opacity=0.6
    	)
		data = [trace0]
		layout = go.Layout(
				title='{{article_name}}',
				titlefont=dict(
					family='Roboto, sans-serif',
					size=30,
					color='#000000'
				),
				xaxis=dict(
					title='Keywords',
					titlefont=dict(
						family='Roboto, sans-serif',
						size=20,
						color='#f28c10'
						)
					),
				yaxis=dict(
				title='Count',
				titlefont=dict(
					family='Roboto, sans-serif',
					size=20,
					color='#f28c10'
					)
				),
				autosize=False,
				width=900,
    			height=600,
				margin=go.Margin(
        			l=100,
        			r=100,
        			b=100,
        			t=100,
    				pad=2
    			),
    			paper_bgcolor='#cacece',
    			plot_bgcolor='#eaf2f1'
			)
		fig = go.Figure(data=data, layout=layout)
		my_plot_div = plot(fig, output_type='div')
		return render_template('results.html',div_placeholder=Markup(my_plot_div))

if __name__ == '__main__':
	app.run(debug=True)


