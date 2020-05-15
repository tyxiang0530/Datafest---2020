import plotly.graph_objs as go
import plotly
from plotly.subplots import make_subplots
import pandas as pd


# swap category numbers to categories
def switch_cat(num_in):
    switcher = {
        10: 'Music',
        19: 'Travel and Events',
        22: 'People and Blogs',
        24: 'Entertainment',
        25: 'News and Politics',
        26: 'How-to and Style',
        27: 'Education',
        28: 'Science and Tech'
    }
    return switcher.get(num_in, 'invalid')

# Create scatter plot of average sentiment that is mapped against date
def create_scatter_plot_death(country_in):
    df = pd.read_csv('C:\\Users\\tyxia\\Documents\\Pomona\\'
                     'Research\\Datafest2020\\Results\\R_analysis_'
                     + country_in + '.csv')

    fig = make_subplots(specs=[[{'secondary_y': True}]])

    trace1 = go.Scatter(
        x = df['date_avg'],
        y = df['sent_avg_10'],
        name = 'Music Sentiment Scores',
        yaxis = 'y',
        line = dict(color = '#ff7f0e')
    )

    trace2 = go.Scatter(
        x = df['date_avg'],
        y = df['sent_avg_19'],
        name = 'Travel and Events Sentiment Scores',
        yaxis = 'y',
        line = dict(color = '#2ca02c')
    )

    trace3 = go.Scatter(
        x = df['date_avg'],
        y = df['sent_avg_22'],
        name = 'People and Blogs Sentiment Scores',
        yaxis='y',
        line = dict(color = '#9467bd')
    )

    trace4 = go.Scatter(
        x = df['date_avg'],
        y = df['sent_avg_24'],
        name = 'Entertainment Sentiment Scores',
        yaxis='y',
        line = dict(color = '#8c564b')
    )

    trace5 = go.Scatter(
        x = df['date_avg'],
        y = df['sent_avg_25'],
        name = 'News and Politics Sentiment Scores',
        yaxis='y',
        line = dict(color = '#e377c2')
    )

    trace6 = go.Scatter(
        x = df['date_avg'],
        y = df['sent_avg_26'],
        name = 'How-to and Style Sentiment Scores',
        yaxis='y',
        line = dict(color = '#7f7f7f')
    )

    trace7 = go.Scatter(
        x = df['date_avg'],
        y = df['sent_avg_27'],
        name = 'Education Sentiment Scores',
        yaxis='y',
        line = dict(color = '#bcbd22')
    )

    trace8 = go.Scatter(
        x = df['date_avg'],
        y = df['sent_avg_28'],
        name = 'Science and Tech Sentiment Scores',
        yaxis='y',
        line = dict(color = '#17becf')
        )

    trace9 = go.Scatter(
        x = df['date_avg'],
        y = df['sent_avg_all'],
        name = 'All Categories Combined Sentiment Score',
        yaxis='y',
        line = dict(color = 'darkgoldenrod')
        )

    trace10 = go.Scatter(
        x = df['date_avg'],
        y = df['case_num'],
        name = 'Total Coronavirus Cases in ' + country_in,
        yaxis='y2',
        line = dict(color = '#d62728', width = 4, dash = 'dash')
        )

    fig.add_trace(trace1, secondary_y = False)
    fig.add_trace(trace2, secondary_y = False)
    fig.add_trace(trace3, secondary_y = False)
    fig.add_trace(trace4, secondary_y = False)
    fig.add_trace(trace5, secondary_y = False)
    fig.add_trace(trace6, secondary_y = False)
    fig.add_trace(trace7, secondary_y = False)
    fig.add_trace(trace8, secondary_y = False)
    fig.add_trace(trace9, secondary_y = False)
    fig.add_trace(trace10, secondary_y = True)

    # Set x-axis title
    fig.update_xaxes(title_text='Date on a Two Week Cycle')
    fig.update_layout(title_text = "YouTube Video Sentiment Overtime By Category: "
                      + country_in,
                      title_x = 0.25)
    # Create axis objects
    fig.update_layout(
        autosize = True,
        yaxis=dict(
            title="Average Sentiment Polarity",
            titlefont=dict(
                color="#1f77b4"
            )
        ),
        yaxis2=dict(
            title="<b>secondary</b> Total Coronavirus Cases in " + country_in,
            titlefont=dict(
                color="#d62728"
            ),
            side="right"
        )
    )
    plotly.offline.plot(fig, filename='C:\\Users\\tyxia\\Documents\\Pomona\\Research\\'
                                      'Datafest2020\\Plots\\plots\\' + country_in +
                                      '_line.html')
    fig.show()


# create box plot of sentiment mapped against date
def create_box_plot_death_nonbinary(country_in, cat_num):
    df = pd.read_csv('C:\\Users\\tyxia\\Documents\\Pomona\\'
                     'Research\\Datafest2020\\Results\\R_analysis_'
                     + country_in + '.csv')
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    trace1 = go.Box()
    trace2 = go.Scatter()
    if country_in == 'Australia':
        intro_y = df['total_confirmed']
        trace2 = go.Scatter(
            x=df['date'],
            y=intro_y.head(102),
            name='Coronavirus Cases in ' + country_in,
            yaxis='y2',
            mode='markers',
            marker=dict(color='#d62728',
                        size=12,
                        line=dict(width=1,
                                  color='DarkSlateGrey'))
        )

        if cat_num == '10':
            music = df.head(102)
            trace1 = go.Box(
                x = music['date'],
                y = music['sentiment_score'],
                name = 'Music Sentiment Distribution',
                marker_color='#17becf'
            )

        if cat_num == '19':
            travel = df[102:230]
            trace1 = go.Box(
                x = travel['date'],
                y = travel['sentiment_score'],
                name = 'Travel and Events Sentiment Distribution',
                marker_color='#bcbd22'
            )

        if cat_num == '22':
            people = df[230:360]
            trace1 = go.Box(
                x = people['date'],
                y = people['sentiment_score'],
                name = 'People and Blogs Sentiment Distribution',
                marker_color='#7f7f7f'
            )

        if cat_num == '24':
            entertainment = df[360:490]
            trace1 = go.Box(
                x = entertainment['date'],
                y = entertainment['sentiment_score'],
                name = 'Entertainment Sentiment Distribution',
                marker_color='#e377c2'
            )

        if cat_num == '25':
            news = df[490:601]
            trace1 = go.Box(
                x = news['date'],
                y = news['sentiment_score'],
                name = 'News and Politics Sentiment Distribution',
                marker_color='#8c564b'
            )

        if cat_num == '26':
            how = df[601:731]
            trace1 = go.Box(
                x = how['date'],
                y = how['sentiment_score'],
                name = 'How-to and Style Sentiment Distribution',
                marker_color='#9467bd'
            )

        if cat_num == '27':
            education = df[731:861]
            trace1 = go.Box(
                x = education['date'],
                y = education['sentiment_score'],
                name = 'Education Sentiment Distribution',
                marker_color='#2ca02c'
            )

        if cat_num == '28':
            science = df[861:968]
            trace1 = go.Box(
                x = science['date'],
                y = science['sentiment_score'],
                name = 'Science and Technology Sentiment Distribution',
                marker_color='#ff7f0e'
            )

        if cat_num == 'All':
            all = df[968:1098]
            trace1 = go.Box(
                x = all['date'],
                y = all['sentiment_score'],
                name='All Categories Sentiment Distribution',
                marker_color='#ff7f0e'
            )

    if country_in == 'Canada':
        intro_y = df['total_confirmed']
        trace2 = go.Scatter(
            x=df['date'],
            y=intro_y.head(126),
            name='Coronavirus Cases in ' + country_in,
            yaxis='y2',
            mode='markers',
            marker=dict(color='#d62728',
                        size=12,
                        line=dict(width=1,
                                  color='DarkSlateGrey'))
        )
        if cat_num == '10':
            music = df.head(126)
            trace1 = go.Box(
                x = music['date'],
                y = music['sentiment_score'],
                name = 'Music Sentiment Distribution',
                marker_color='#17becf'
            )

        if cat_num == '19':
            travel = df[126:256]
            trace1 = go.Box(
                x = travel['date'],
                y = travel['sentiment_score'],
                name = 'Travel and Events Sentiment Distribution',
                marker_color='#bcbd22'
            )

        if cat_num == '22':
            people = df[256:385]
            trace1 = go.Box(
                x = people['date'],
                y = people['sentiment_score'],
                name = 'People and Blogs Sentiment Distribution',
                marker_color='#7f7f7f'
            )

        if cat_num == '24':
            entertainment = df[385:513]
            trace1 = go.Box(
                x = entertainment['date'],
                y = entertainment['sentiment_score'],
                name = 'Entertainment Sentiment Distribution',
                marker_color='#e377c2'
            )

        if cat_num == '25':
            news = df[513:642]
            trace1 = go.Box(
                x = news['date'],
                y = news['sentiment_score'],
                name = 'News and Politics Sentiment Distribution',
                marker_color='#8c564b'
            )

        if cat_num == '26':
            how = df[642:771]
            trace1 = go.Box(
                x = how['date'],
                y = how['sentiment_score'],
                name = 'How-to and Style Sentiment Distribution',
                marker_color='#9467bd'
            )

        if cat_num == '27':
            education = df[771:901]
            trace1 = go.Box(
                x = education['date'],
                y = education['sentiment_score'],
                name = 'Education Sentiment Distribution',
                marker_color='#2ca02c'
            )

        if cat_num == '28':
            science = df[901:1021]
            trace1 = go.Box(
                x = science['date'],
                y = science['sentiment_score'],
                name = 'Science and Technology Sentiment Distribution',
                marker_color='#ff7f0e'
            )

        if cat_num == 'All':
            all = df[1021:1150]
            trace1 = go.Box(
                x = all['date'],
                y = all['sentiment_score'],
                name='All Categories Sentiment Distribution',
                marker_color = '#ff7f0e'
            )

    if country_in == 'India':
        intro_y = df['total_confirmed']
        trace2 = go.Scatter(
            x=df['date'],
            y=intro_y.head(129),
            name='Coronavirus Cases in ' + country_in,
            yaxis='y2',
            mode='markers',
            marker=dict(color='#d62728',
                        size=12,
                        line=dict(width=1,
                                  color='DarkSlateGrey'))
        )
        if cat_num == '10':
            music = df.head(129)
            trace1 = go.Box(
                x = music['date'],
                y = music['sentiment_score'],
                name = 'Music Sentiment Distribution',
                marker_color = '#17becf'
            )

        if cat_num == '19':
            travel = df[129:258]
            trace1 = go.Box(
                x = travel['date'],
                y = travel['sentiment_score'],
                name = 'Travel and Events Sentiment Distribution',
                marker_color = '#bcbd22'
            )

        if cat_num == '22':
            people = df[258:388]
            trace1 = go.Box(
                x = people['date'],
                y = people['sentiment_score'],
                name = 'People and Blogs Sentiment Distribution',
                marker_color = '#7f7f7f'
            )

        if cat_num == '24':
            entertainment = df[388:516]
            trace1 = go.Box(
                x = entertainment['date'],
                y = entertainment['sentiment_score'],
                name = 'Entertainment Sentiment Distribution',
                marker_color = '#e377c2'
            )

        if cat_num == '25':
            news = df[516:645]
            trace1 = go.Box(
                x = news['date'],
                y = news['sentiment_score'],
                name = 'News and Politics Sentiment Distribution',
                marker_color = '#8c564b'
            )

        if cat_num == '26':
            how = df[645:775]
            trace1 = go.Box(
                x = how['date'],
                y = how['sentiment_score'],
                name = 'How-to and Style Sentiment Distribution',
                marker_color = '#9467bd'
            )

        if cat_num == '27':
            education = df[775:905]
            trace1 = go.Box(
                x = education['date'],
                y = education['sentiment_score'],
                name = 'Education Sentiment Distribution',
                marker_color = '#2ca02c'
            )

        if cat_num == '28':
            science = df[905:1035]
            trace1 = go.Box(
                x = science['date'],
                y = science['sentiment_score'],
                name = 'Science and Technology Sentiment Distribution',
                marker_color = '#ff7f0e'
            )

        if cat_num == 'All':
            all = df[1035:1165]
            trace1 = go.Box(
                x = all['date'],
                y = all['sentiment_score'],
                name='All Categories Sentiment Distribution',
                marker_color = '#ff7f0e'
            )

    if country_in == 'United Kingdom':
        intro_y = df['total_confirmed']
        trace2 = go.Scatter(
            x=df['date'],
            y=intro_y.head(130),
            name='Coronavirus Cases in ' + country_in,
            yaxis='y2',
            mode='markers',
            marker=dict(color='#d62728',
                        size=12,
                        line=dict(width=1,
                                  color='DarkSlateGrey'))
        )
        if cat_num == '10':
            music = df.head(130)
            trace1 = go.Box(
                x = music['date'],
                y = music['sentiment_score'],
                name = 'Music Sentiment Distribution',
                marker_color = '#17becf'
            )

        if cat_num == '19':
            travel = df[130:260]
            trace1 = go.Box(
                x = travel['date'],
                y = travel['sentiment_score'],
                name = 'Travel and Events Sentiment Distribution',
                marker_color = '#bcbd22'
            )

        if cat_num == '22':
            people = df[260:389]
            trace1 = go.Box(
                x = people['date'],
                y = people['sentiment_score'],
                name = 'People and Blogs Sentiment Distribution',
                marker_color = '#7f7f7f'
            )

        if cat_num == '24':
            entertainment = df[389:518]
            trace1 = go.Box(
                x = entertainment['date'],
                y = entertainment['sentiment_score'],
                name = 'Entertainment Sentiment Distribution',
                marker_color = '#e377c2'
            )

        if cat_num == '25':
            news = df[518:648]
            trace1 = go.Box(
                x = news['date'],
                y = news['sentiment_score'],
                name = 'News and Politics Sentiment Distribution',
                marker_color = '#8c564b'
            )

        if cat_num == '26':
            how = df[648:778]
            trace1 = go.Box(
                x = how['date'],
                y = how['sentiment_score'],
                name = 'How-to and Style Sentiment Distribution',
                marker_color = '#9467bd'
            )

        if cat_num == '27':
            education = df[778:908]
            trace1 = go.Box(
                x = education['date'],
                y = education['sentiment_score'],
                name = 'Education Sentiment Distribution',
                marker_color = '#2ca02c'
            )

        if cat_num == '28':
            science = df[908:1038]
            trace1 = go.Box(
                x = science['date'],
                y = science['sentiment_score'],
                name = 'Science and Technology Sentiment Distribution',
                marker_color = '#ff7f0e'
            )

        if cat_num == 'All':
            all = df[1038:1168]
            trace1 = go.Box(
                x = all['date'],
                y = all['sentiment_score'],
                name='All Categories Sentiment Distribution',
                marker_color = '#ff7f0e'
            )
    if country_in == 'United States':
        intro_y = df['total_confirmed']
        trace2 = go.Scatter(
            x = df['date'],
            y = intro_y.head(129),
            name='Coronavirus Cases in ' + country_in,
            yaxis='y2',
            mode='markers',
            marker=dict(color='#d62728',
                        size=12,
                        line=dict(width=1,
                                  color='DarkSlateGrey'))
        )
        if cat_num == '10':
            music = df.head(129)
            trace1 = go.Box(
                x = music['date'],
                y = music['sentiment_score'],
                name = 'Music Sentiment Distribution',
                marker_color='#17becf'
            )

        if cat_num == '19':
            travel = df[129:259]
            trace1 = go.Box(
                x = travel['date'],
                y = travel['sentiment_score'],
                name = 'Travel and Events Sentiment Distribution',
                marker_color='#bcbd22'
            )

        if cat_num == '22':
            people = df[259:389]
            trace1 = go.Box(
                x = people['date'],
                y = people['sentiment_score'],
                name = 'People and Blogs Sentiment Distribution',
                marker_color='#7f7f7f'
            )

        if cat_num == '24':
            entertainment = df[389:519]
            trace1 = go.Box(
                x = entertainment['date'],
                y = entertainment['sentiment_score'],
                name = 'Entertainment Sentiment Distribution',
                marker_color='#e377c2'
            )

        if cat_num == '25':
            news = df[519:648]
            trace1 = go.Box(
                x = news['date'],
                y = news['sentiment_score'],
                name = 'News and Politics Sentiment Distribution',
                marker_color='#8c564b'
            )

        if cat_num == '26':
            how = df[649:778]
            trace1 = go.Box(
                x = how['date'],
                y = how['sentiment_score'],
                name = 'How-to and Style Sentiment Distribution',
                marker_color='#9467bd'
            )

        if cat_num == '27':
            education = df[778:908]
            trace1 = go.Box(
                x = education['date'],
                y = education['sentiment_score'],
                name = 'Education Sentiment Distribution',
                marker_color='#2ca02c'
            )

        if cat_num == '28':
            science = df[908:1038]
            trace1 = go.Box(
                x = science['date'],
                y = science['sentiment_score'],
                name = 'Science and Technology Sentiment Distribution',
                marker_color='#ff7f0e'
            )

        if cat_num == 'All':
            all = df[1038:1168]
            trace1 = go.Box(
                x = all['date'],
                y = all['sentiment_score'],
                name='All Categories Sentiment Distribution',
                marker_color='#ff7f0e'
            )

    fig.add_trace(trace1, secondary_y = False)
    fig.add_trace(trace2, secondary_y = True)
    fig.add_shape(
        # Line Vertical
        dict(
            type = "line",
            x0 = 7,
            y0 = 0,
            x1 = 7,
            y1 = 2,
            line = dict(
                color = "RoyalBlue",
                width = 3,
                dash = "dot"
            )
        ),
        name = 'First Coronavirus Case Found')

    fig.update_xaxes(title_text = 'Date on a Two Week Cycle')
    if cat_num == 'All':
        fig.update_layout(title_text='Distribution of YouTube Sentiment Scores Over Time for '
                                     'All Videos in ' + country_in,
                          title_x=0.25)
    else:
        fig.update_layout(title_text = 'Distribution of YouTube Sentiment Scores Over Time for '
                          + switch_cat(int(cat_num)) + ' in ' + country_in,
                          title_x = 0.25)
    # Create axis objects
    fig.update_layout(
        yaxis = dict(
            title = 'Sentiment Scores',
            titlefont = dict(
                color = '#1f77b4'
            )
        )
    )

    fig.update_layout(
        showlegend = False,
        annotations =[
            dict(
                x = 7,
                y = 1.25,
                text = 'First Coronavirus case detected in ' + country_in,
                showarrow = True,
                font = dict(
                    family = 'Courier New, monospace',
                    size = 14,
                    color = '#ffffff'
                ),
                align = 'center',
                arrowhead = 2,
                arrowsize = 1,
                arrowwidth = 2,
                arrowcolor = '#636363',
                ax = 20,
                ay = -30,
                bordercolor = '#c7c7c7',
                borderwidth = 2,
                borderpad = 4,
                bgcolor = '#ff7f0e',
                opacity = 0.8
            )
        ]
    )
    fig.update_layout(
        autosize = True,
        yaxis2 = dict(
            title = '<b>secondary</b> Total Coronavirus Cases in ' + country_in,
            titlefont = dict(
                color = '#d62728'
            ),
            side = 'right'
        )
    )

    plotly.offline.plot(fig, filename='C:\\Users\\tyxia\\Documents\\Pomona\\Research\\'
                                      'Datafest2020\\Plots\\plots\\' + country_in + cat_num + '_boxes.html')

    fig.show()


# create charts denoting Z-Score, P-Value, and Range
def create_chart_scores_both_touched():
    df = pd.read_csv('C:\\Users\\tyxia\\Documents\\Pomona\\Research\\'
                     'Datafest2020\\Results\\Z, P Country Category.csv')

    fig = go.Figure(data=[go.Table(
        header = dict(values = [(df.columns[0]), ' ', ' ', (df.columns[4])],
                      fill_color = 'paleturquoise',
                      align = 'left'),
        cells = dict(values = [df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2],
                               df.iloc[:, 3], df.iloc[:, 4], df.iloc[:, 5]],
                     fill_color = 'lavender', align = 'left'))
    ])
    plotly.offline.plot(fig, filename='C:\\Users\\tyxia\\Documents\\Pomona\\Research\\'
                                      'Datafest2020\\Plots\\plots\\below_05_charts.html')
    fig.show()


def create_chart_scores_both_untouched():
    df = pd.read_csv('C:\\Users\\tyxia\\Documents\\Pomona\\Research\\'
                     'Datafest2020\\Results\\Z, P Country Category - untouched.csv')

    fig = go.Figure(data=[go.Table(
        header = dict(values = [(df.columns[1]), ' ', ' ', (df.columns[3])],
                      fill_color = 'paleturquoise',
                      align = 'left'),
        cells = dict(values = [df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2],
                               df.iloc[:, 0], df.iloc[:, 3], df.iloc[:, 4]],
                     fill_color = 'lavender', align = 'left'))
    ])
    plotly.offline.plot(fig, filename='C:\\Users\\tyxia\\Documents\\Pomona\\Research\\'
                                      'Datafest2020\\Plots\\plots\\all_charts.html')
    fig.show()


country = ['Australia', 'Canada', 'India', 'United Kingdom', 'United States']
category = ['10', '19', '22', '24', '25', '26', '27', '28', 'All']

