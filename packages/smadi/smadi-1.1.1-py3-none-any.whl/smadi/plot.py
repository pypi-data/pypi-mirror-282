import matplotlib
import matplotlib.pyplot as plt


from smadi.metadata import indicators_thresholds


def set_thresholds(method):
    """
    Set the thresholds for the specified method based on the method name.

    parameters:
    -----------

    method: str
        The method name for which the thresholds are to be set. Supported methods are:
        'zscore', 'smapi', 'smdi', 'smca', 'smad', 'smci', 'smds', 'essmi', 'beta', 'gamma'
    """

    if method in indicators_thresholds.keys():
        return indicators_thresholds[method]
    else:
        return None


def get_plot_options(**kwargs):
    """
    Set the basic plot options based on the provided kwargs for the plot.

    parameters:
    -----------

    kwargs: dict
        The keyword arguments for the matplotlib plot.

    returns:
    --------

    plot_options: dict
        The plot options for the figure.

    """
    plot_options = {
        "title": kwargs.get("title", None),
        "xlabel": kwargs.get("xlabel", None),
        "ylabel": kwargs.get("ylabel", None),
        "legend": kwargs.get("legend", None),
        "legend_labels": kwargs.get("legend_labels", None),
        "figsize": kwargs.get("figsize", None),
        "grid": kwargs.get("grid", None),
        "savefig": kwargs.get("savefig", None),
    }

    return plot_options


def plot_figure(plot_params):
    """
    Plot the figure based on the provided plot parameters.

    parameters:
    -----------

    plot_params: dict
        The plot parameters for the figure.

    """

    # Set labels and title
    plt.title(plot_params["title"])
    plt.xlabel(plot_params["xlabel"])
    plt.ylabel(plot_params["ylabel"])

    # Add legend if specified
    if plot_params["legend"]:
        if plot_params["legend_labels"] is not None:
            plt.legend(plot_params["legend_labels"])
        else:
            plt.legend(loc="lower left")

    # Show plot
    plt.grid(plot_params["grid"])
    plt.tight_layout()
    if plot_params["savefig"] is not None:
        plt.savefig(plot_params["savefig"])
    plt.show()


def plot_colmns(df, x_axis, colmns_kwargs):
    """
    Plot the data in each column of the dataframe with the provided x_axis.

    parameters:
    -----------

    df: pd.DataFrame
        The dataframe containing the data to plot.

    x_axis: list
        The x-axis values for the plot.

    colmns_kwargs: dict
        The dictionary containing the column names and their respective matplotlib plot options.

    """
    for colmn, kwargs in colmns_kwargs.items():
        plt.plot(x_axis, df[colmn], **kwargs)


def draw_hbars(thresholds, x_axis):
    """
    Draw horizontal bars on the plot based on the provided thresholds for each anomaly method.

    parameters:
    -----------

    thresholds: dict
        The dictionary containing the thresholds for each category of the anomaly method.

    x_axis: list
        The x-axis values for the plot.
    """
    thresholds = set_thresholds(thresholds)
    for key, value in thresholds.items():
        alpha = (
            int(key.split("-")[1]) * 0.2
            if key.startswith("D") or key.startswith("W")
            else 0.1
        )
        color = (
            "brown"
            if key.startswith("D")
            else "blue" if key.startswith("W") else "green"
        )
        plt.fill_between(x_axis, value[0], value[1], color=color, alpha=alpha)


def clss_counter(df, columns, thresholds):
    """
    Count the number of values in the dataframe that fall within the thresholds for each category of the anomaly method.

    parameters:
    -----------

    df: pd.DataFrame
        The dataframe containing the data to plot.

    columns: dict
        The dictionary containing the column names and their respective matplotlib plot options.

    thresholds: str
        The name of the anomaly method to use its thresholds.
    """

    results = []
    anomaly_thresholds = set_thresholds(thresholds)

    if len(columns) > 2:
        raise ValueError("The number of columns should not exceed 2.")

    for colm, _ in columns.items():
        category_counter = {}
        for key, value in anomaly_thresholds.items():
            category_counter[key] = df[colm].between(value[0], value[1]).sum()

        results.append(category_counter)

    return results


def plot_categories_count(x_axis, results, anomaly_method):
    """
    Plot the number of values in each category of the anomaly method that fall within the thresholds.

    parameters:
    -----------

    x_axis: list
        The x-axis values for the plot.

    results: list
        The list containing the number of values in each category of the anomaly method.

    anomaly_method: str
        The name of the anomaly method to use its thresholds.

    """
    for i, result in enumerate(results):
        for key, value in result.items():
            thresholds = set_thresholds(anomaly_method)
            y = thresholds[key][1]
            x = x_axis[0] if i == 0 else x_axis[-1]
            halignment = "right" if i == 0 else "left"
            plt.text(
                x=x,
                y=y,
                s=f"{key}:{value}",
                fontsize=10,
                color="black",
                horizontalalignment=halignment,
                fontstyle="italic",
                in_layout=True,
                weight="bold",
            )


def plot_ts(
    df,
    x_axis,
    colmns_kwargs,
    plot_raw=False,
    raw_df=None,
    raw_var=None,
    raw_kwargs=None,
    **kwargs,
):
    """
    Plot the time series data for the provided dataframe.

    parameters:
    -----------

    df: pd.DataFrame
        The dataframe containing the data to plot.

    x_axis: list
        The x-axis values for the plot.

    colmns_kwargs: dict
        The dictionary containing the column names and their respective matplotlib plot options.

    plot_raw: bool
        Whether to plot the raw data on the plot as background.

    raw_df: pd.DataFrame
        The dataframe containing the raw data to plot.

    raw_var: str
        The name of the raw variable to plot.

    raw_kwargs: dict
        The dictionary containing the matplotlib plot options for the raw data.

    kwargs: dict
        The keyword arguments for the matplotlib plot for the figure such as title, xlabel, ylabel, legend, figsize, and grid.

    """
    # Set values for kwargs based on provided values
    plot_params = get_plot_options(**kwargs)
    if plot_params["figsize"] is not None:
        plt.figure(figsize=plot_params["figsize"])

    if plot_raw:
        plt.plot(
            raw_df.index,
            raw_df[raw_var],
            **raw_kwargs if raw_kwargs else {},
        )

    plot_colmns(df, x_axis, colmns_kwargs)
    plot_figure(plot_params)


def plot_anomaly(
    df, x_axis, colmns, thresholds, plot_hbars=True, plot_categories=True, **kwargs
):
    """
    Plot the anomaly detection results for the provided dataframe.

    parameters:
    -----------

    df: pd.DataFrame
        The dataframe containing the data to plot.

    x_axis: list
        The x-axis values for the plot.

    colmns: dict
        The dictionary containing the column names and their respective matplotlib plot options.

    thresholds: str
        The name of the anomaly method to use its thresholds.

    plot_hbars: bool
        Whether to plot the horizontal bars on the plot according to the thresholds of the anomaly method used.

    plot_categories: bool
        Whether to plot the number of values in each category of the anomaly method that fall within the thresholds.

    kwargs: dict
        The keyword arguments for the matplotlib plot for the figure such as title, xlabel, ylabel, legend, figsize, and grid.

    """

    # Set values for kwargs based on provided values
    plot_params = get_plot_options(**kwargs)
    plt.figure(figsize=plot_params["figsize"])
    plot_colmns(df, x_axis, colmns)

    if plot_hbars:
        draw_hbars(thresholds, x_axis)
    if plot_categories:
        results = clss_counter(df, colmns, thresholds)
        plot_categories_count(x_axis, results, thresholds)

    plot_figure(plot_params)


def plot_fill_bet(df=None, x_axis=None, colmn=None, plot_style="ggplot", **kwargs):
    """
    Plot the computed anomalies using the fill_between method.

    parameters:
    -----------

    df: pd.DataFrame
        The dataframe containing the data to plot. if None, the computed anomalies will be used.

    x_axis: list
        The x-axis values for the plot. if None, the index of the dataframe will be used.

    colmn: str
        The column name to plot.

    plot_style: str
        The plot style to use for the plot.

    kwargs: dict
        Additional parameters to be used for customizing the plot. It can be any of the following:

        ['title', 'xlabel', 'ylabel', 'legend', 'figsize', 'grid']

    """

    plt.style.use(plot_style)
    plot_params = get_plot_options(**kwargs)
    plt.figure(figsize=plot_params["figsize"])

    plt.fill_between(
        x_axis,
        df[colmn],
        where=df[colmn].values >= 0,
        color="blue",
        label="Wet",
    )

    plt.fill_between(
        x_axis,
        df[colmn],
        where=df[colmn].values < 0,
        color="red",
        label="Dry",
    )

    # Add horizontal line at y=0
    plt.axhline(y=0, color="black", linestyle="--", linewidth=1)

    plt.legend(loc="upper right", fontsize=10)

    plot_figure(plot_params)
