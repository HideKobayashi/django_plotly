from django.shortcuts import render
from django.views.generic import TemplateView
import plotly.graph_objects as go


def line_charts():
    fig = go.Figure(
        go.Scatter(x=[1, 2, 3], y=[3, 5, 2]),
        # layout=go.Layout(width=400, height=400),
        layout=go.Layout(),
    )
    return fig.to_html(include_plotlyjs=False)


class LineChartsView(TemplateView):
    template_name = "plot.html"

    def get_context_data(self, **kwargs):
        context = super(LineChartsView, self).get_context_data(**kwargs)
        context["plot"] = line_charts()
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
