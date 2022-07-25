from django.shortcuts import render
from django.views.generic import TemplateView
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np


def line_charts():
    fig = go.Figure(
        go.Scatter(x=[1, 2, 3], y=[3, 5, 2]),
        # layout=go.Layout(width=400, height=400),
        layout=go.Layout(),
    )
    return fig.to_html(include_plotlyjs=False)


def bar_charts():
    tips = px.data.tips()
    print(f"tips: {tips}")
    fig = px.histogram(
        tips,
        # x="sex", y="tip", histfunc="avg", color="smoker", barmode="group",
        x="tip", y="time", histfunc="avg", color="smoker", barmode="group",
        facet_row="sex", facet_col="day", 
        category_orders={
            # "time": ["Lunch", "Dinner"],
            "sex": ["Male", "Female"],
            "day": ["Thur", "Fri", "Sat", "Sun"],
        },
        orientation="h",
        height=400, width=800)
    # fig.write_html('../output/boxplot_with_facet_px.html', auto_open=False)
    return fig.to_html(include_plotlyjs=False)

    # fig = go.Figure(
    #     go.Scatter(x=[1, 2, 3], y=[3, 5, 2]),
    #     # layout=go.Layout(width=400, height=400),
    #     layout=go.Layout(),
    # )
    # return fig.to_html(include_plotlyjs=False)

from plotly.subplots import make_subplots

def histograms():
    iris = px.data.iris()
    fig = make_subplots(rows=1, cols=2, subplot_titles=('がく片の長さ(cm)', '品種毎のがく片の長さ(cm)'))
    fig.add_trace(go.Histogram(
        x=iris['sepal_length'], xbins=dict(start=4,end=8,size=0.25), hovertemplate="%{x}cm: %{y}個", 
        name="全品種"), row=1, col=1)
    for species in ['setosa', 'versicolor', 'virginica']:
        fig.add_trace(go.Histogram(x=iris.query(f'species=="{species}"')['sepal_length'],
                            xbins=dict(start=4,end=8,size=0.25), hovertemplate="%{x}cm: %{y}個", name=species), row=1, col=2)
    fig.update_layout(barmode='overlay', height=400, width=900)
    fig.update_traces(opacity=0.3, row=1, col=2)
    fig.update_xaxes(tickvals=np.arange(4,8,0.5), title_text='sepal_length')
    fig.update_yaxes(title_text='度数')
    # fig.write_html('../output/histogram_with_boxplot_plotly.html', auto_open=False)
    return fig.to_html(include_plotlyjs=False)

def bar_plotly():
    # ギャップマインダーのデータ
    df = px.data.gapminder()
    # アメリカ大陸のデータだけ抽出
    df_Americas = df[df['continent'] == 'Americas']
    print(df_Americas)
    #         country continent  year  ...     gdpPercap  iso_alpha  iso_num
    # 48    Argentina  Americas  1952  ...   5911.315053        ARG       32
    # 49    Argentina  Americas  1957  ...   6856.856212        ARG       32
    # 50    Argentina  Americas  1962  ...   7133.166023        ARG       32
    # 51    Argentina  Americas  1967  ...   8052.953021        ARG       32
    # 52    Argentina  Americas  1972  ...   9443.038526        ARG       32
    # ...         ...       ...   ...  ...           ...        ...      ...
    # 1639  Venezuela  Americas  1987  ...   9883.584648        VEN      862
    # 1640  Venezuela  Americas  1992  ...  10733.926310        VEN      862
    # 1641  Venezuela  Americas  1997  ...  10165.495180        VEN      862
    # 1642  Venezuela  Americas  2002  ...   8605.047831        VEN      862
    # 1643  Venezuela  Americas  2007  ...  11415.805690        VEN      862
    # [300 rows x 8 columns]
    fig = px.bar(
        # df_Americas, x='year', y='pop',
        # df_Americas, x='pop', y='year',
        df_Americas[df_Americas['year'] > 1980], x='pop', y='year',
        color='country',
        facet_col='country', facet_col_wrap=5,  # 国ごとに5列になるように分ける
        # log_y=True,  # 縦軸をlog（常用対数）表示
        log_x=True,  # 縦軸をlog（常用対数）表示
        orientation='h',
    )
    # グラフ全体とホバーのフォントサイズ変更
    fig.update_layout(
        height=1000,  # グラフの高さ
        hoverlabel_font_size=20,
        legend_orientation='h'  # 凡例の向き
    )

    return fig.to_html(include_plotlyjs=False)






    # iris = px.data.iris()
    # fig = go.Figure()
    # # species = sorted(list(set(iris['species'])))
    # # print(f"species: {species}")
    # fig.add_trace(go.Bar(
    #     x=iris['sepal_length'].head(),
    #     y=species,
    #     name='sepal_length',
    #     orientation='h',
    # ))
    # return fig.to_html(include_plotlyjs=False)


class LineChartsView(TemplateView):
    template_name = "plot.html"

    def get_context_data(self, **kwargs):
        context = super(LineChartsView, self).get_context_data(**kwargs)
        context["plot"] = line_charts()
        context["plot1"] = bar_charts()
        context["plot2"] = histograms()
        context["plot3"] = bar_plotly()
        return context

class TopView(TemplateView):
    template_name = "top.html"

    def get_context_data(self, **kwargs):
        # context = super(TopView, self).get_context_data(**kwargs)
        context = super().get_context_data(**kwargs)
        context["items"] = ["52", "53", "54"]
        context["checked_list"] = ["52"]
        context["message"] = 'Get'
        return context

    def post(self, request, *args, **kwargs):
        context = super(TopView, self).get_context_data(**kwargs)
        selection_list = request.POST.getlist("office")
        print("selection_list:", selection_list)
        context["items"] = ["52", "53", "54"]
        context["checked_list"] = selection_list
        context["message"] = 'Post'
        return render(request, self.template_name, context)
