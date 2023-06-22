import plotly.graph_objects as go
import plotly.offline as offline
import plotly.express as px


class Visualize:
    def scatter_plot(self, x_series, y_series, names, 
                        filename_html, offline_plot=True,
                        ):
        fig=go.Figure(data=go.Scatter(x=x_series,
                        y=y_series,
                        mode='markers',
                        marker=dict(size=16),
                        #legendgroup=legend,
                        #color=legend,
                        text=names))
        
        if offline_plot:
            offline.plot(fig, filename=filename_html)

        else:
            fig.show()
       
        return 


    def scatter_plot2(self, df, filename):
        fig = px.scatter(df, x="obj1", y="obj2", color="front",
                        hover_data=['id'])

        fig.update_traces(marker=dict(size=16))

        fig.show()
        fig.write_html(filename)
       
        return 