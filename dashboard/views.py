from django.shortcuts import render
import matplotlib.pyplot as plt
import numpy as np
import io
import urllib, base64
# Create your views here.
def dashboard(request):
    return render(request, "dashboard/side.html")



def chart_view(request):
    # Sample data
    days = ["01 Feb", "02 Feb", "03 Feb", "04 Feb", "05 Feb", "06 Feb", "07 Feb"]
    revenue_current = [6300, 6400, 6200, 6600, 6500, 6700, 6000]
    revenue_previous = [6600, 6500, 6400, 6300, 6200, 6100, 6000]

    # Plotting the data
    plt.figure(figsize=(10, 6))
    plt.plot(days, revenue_current, marker='o', label='Revenue', color='blue')
    plt.plot(days, revenue_previous, marker='o', label='Revenue (previous period)', color='orange')

    # Customizing the plot
    plt.title('$45,385\nSales this week', loc='left', fontsize=20, color='white')
    plt.suptitle('12.5% ↑', x=0.9, y=0.95, fontsize=16, color='green')

    plt.xlabel('Date', fontsize=12, color='white')
    plt.ylabel('Revenue', fontsize=12, color='white')

    plt.ylim(5900, 6800)
    plt.xticks(fontsize=10, color='white')
    plt.yticks(fontsize=10, color='white')

    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.legend(loc='upper center', fontsize=10, ncol=2)

    plt.gca().set_facecolor('#0b1a34')
    plt.gcf().set_facecolor('#0b1a34')
    plt.gca().spines['top'].set_color('#0b1a34')
    plt.gca().spines['right'].set_color('#0b1a34')
    plt.gca().spines['left'].set_color('#0b1a34')
    plt.gca().spines['bottom'].set_color('#0b1a34')

    # Save the plot to a BytesIO object
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', facecolor='#0b1a34')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = 'data:image/png;base64,' + urllib.parse.quote(string)
    buf.close()

    return render(request, 'index.html', {'data': uri})
