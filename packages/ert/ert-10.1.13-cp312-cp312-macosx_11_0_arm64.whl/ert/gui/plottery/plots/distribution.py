from typing import TYPE_CHECKING, Dict, List

import pandas as pd

from .plot_tools import PlotTools

if TYPE_CHECKING:
    from matplotlib.axes import Axes
    from matplotlib.figure import Figure

    from ert.gui.plottery import PlotConfig, PlotContext


class DistributionPlot:
    def __init__(self):
        self.dimensionality = 1

    @staticmethod
    def plot(
        figure, plot_context, ensemble_to_data_map, _observation_data, std_dev_images
    ):
        plotDistribution(figure, plot_context, ensemble_to_data_map, _observation_data)


def plotDistribution(
    figure: "Figure",
    plot_context: "PlotContext",
    ensemble_to_data_map: Dict[str, pd.DataFrame],
    _observation_data: pd.DataFrame,
):
    config = plot_context.plotConfig()
    axes = figure.add_subplot(111)

    plot_context.deactivateDateSupport()

    plot_context.y_axis = plot_context.VALUE_AXIS

    if plot_context.log_scale:
        axes.set_yscale("log")

    ensemble_list = plot_context.ensembles()
    ensemble_indexes: List[int] = []
    previous_data = None
    for ensemble_index, (ensemble, data) in enumerate(ensemble_to_data_map.items()):
        ensemble_indexes.append(ensemble_index)

        if not data.empty:
            _plotDistribution(
                axes, config, data, ensemble, ensemble_index, previous_data
            )
            config.nextColor()

        previous_data = data

    axes.set_xticks([-1] + ensemble_indexes + [len(ensemble_indexes)])

    rotation = 0
    if len(ensemble_list) > 3:
        rotation = 30

    axes.set_xticklabels([""] + ensemble_list + [""], rotation=rotation)

    config.setLegendEnabled(False)

    PlotTools.finalizePlot(
        plot_context, figure, axes, default_x_label="Ensemble", default_y_label="Value"
    )


def _plotDistribution(
    axes: "Axes",
    plot_config: "PlotConfig",
    data: pd.DataFrame,
    label: str,
    index: int,
    previous_data,
):
    data = pd.Series(dtype="float64") if data.empty else data[0]

    axes.set_xlabel(plot_config.xLabel())
    axes.set_ylabel(plot_config.yLabel())

    style = plot_config.distributionStyle()

    if data.dtype == "object":
        try:
            data = pd.to_numeric(data, errors="coerce")
        except AttributeError:
            data = data.convert_objects(convert_numeric=True)

    if data.dtype == "object":
        dots = []
    else:
        dots = axes.plot(
            [index] * len(data),
            data,
            color=style.color,
            alpha=style.alpha,
            marker=style.marker,
            linestyle=style.line_style,
            markersize=style.size,
        )

        if plot_config.isDistributionLineEnabled() and previous_data is not None:
            line_style = plot_config.distributionLineStyle()
            x = [index - 1, index]
            y = [previous_data[0], data]
            axes.plot(
                x,
                y,
                color=line_style.color,
                alpha=line_style.alpha,
                linestyle=line_style.line_style,
                linewidth=line_style.width,
            )

    if len(dots) > 0:
        plot_config.addLegendItem(label, dots[0])
