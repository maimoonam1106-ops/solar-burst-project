import plotly.graph_objects as go

def create_plot(df, peaks, bursts):
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df['time_tag'],
        y=df['smooth_flux'],
        mode='lines',
        name='Flux'
    ))

    fig.add_trace(go.Scatter(
        x=df['time_tag'].iloc[peaks],
        y=df['smooth_flux'].iloc[peaks],
        mode='markers',
        marker=dict(color='red'),
        name='Peaks'
    ))

    for start, peak, end in bursts:
        fig.add_vrect(
            x0=df['time_tag'].iloc[start],
            x1=df['time_tag'].iloc[end],
            fillcolor="yellow",
            opacity=0.3,
            line_width=0
        )

    return fig
