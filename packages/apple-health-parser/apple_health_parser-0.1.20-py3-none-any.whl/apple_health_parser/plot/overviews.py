from datetime import date
from itertools import compress
from pathlib import Path

from plotly import graph_objects as go
from plotly import subplots
from plotly.graph_objs import Figure

from apple_health_parser.config.definitions import AllowedImageFormats
from apple_health_parser.consts import FLAG_METADATA
from apple_health_parser.exceptions import InvalidImageFormat, MissingFlag
from apple_health_parser.models.parsed import ParsedData
from apple_health_parser.utils.preprocessor import Preprocessor


class ActivityOverview:
    def __init__(
        self,
        data: dict[str, ParsedData],
        year: int = date.today().year,
        source: str | None = None,
        title: bool = False,
    ) -> None:
        """
        Initialize the ActivityOverview object.

        Args:
            data (dict[str, ParsedData]): Dict with flag as key and ParsedData as value
            year (int, optional): Year, defaults to date.today().year
            source (str | None, optional):  Source, defaults to None
            title (bool, optional): Flag to include the plot title, defaults to False
        """
        self.src = source
        self.data = data
        self.year = year
        self.title = title
        self._validate()

        self.dataframes = {
            k: Preprocessor(data=v, year=year, source=source).get_dataframe()
            for k, v in data.items()
        }

    def _validate(self) -> None:
        """
        Validate the data.

        Raises:
            MissingFlag: Missing flag metadata
        """
        flags = [
            "HKQuantityTypeIdentifierActiveEnergyBurned",
            "HKQuantityTypeIdentifierAppleExerciseTime",
            "HKCategoryTypeIdentifierAppleStandHour",
        ]
        flags_not_in_data_bool: list[bool] = [flag not in self.data for flag in flags]
        if not any(flags_not_in_data_bool):
            flags_not_in_data: str = str(list(compress(flags, flags_not_in_data_bool)))
            raise MissingFlag(flags_not_in_data)

    def _get_figure(self) -> Figure:
        """
        Plot the activity overview.

        The activity overview includes the following flags:
            - Active Energy Burned (kcal)
            - Exercise Time (min)
            - Stand Time (min)

        Returns:
            Figure: Figure object
        """
        fig = subplots.make_subplots(rows=3, cols=1, shared_xaxes=True)

        for row, (flag, data) in enumerate(self.dataframes.items()):
            daily_sum = data.groupby("date")["value"].sum().reset_index()

            fig.append_trace(
                go.Bar(
                    x=daily_sum.date,
                    y=daily_sum.value,
                    marker_color=FLAG_METADATA[flag].color,
                    name=FLAG_METADATA[flag].name,
                ),
                row=row + 1,
                col=1,
            )

            fig.update_yaxes(
                title_text="<br>".join(
                    f"{FLAG_METADATA[flag].name} ({FLAG_METADATA[flag].unit})".split(
                        " "
                    )
                ),
                row=row + 1,
                col=1,
                title_font=dict(size=10),
            )

        fig.update_layout(
            title=f"Activity Overview {self.year}" if self.title else None,
            template="simple_white",
            showlegend=False,
        )

        return fig

    def plot(
        self, show: bool = True, save: bool = False, format: str = "png"
    ) -> Figure:
        """
        Plot the figure.

        Args:
            show (bool, optional): Whether to show the figure, defaults to True
            save (bool, optional): Whether to save the figure, defaults to False
            format (str, optional): Format of the file to be saved, defaults to "png"

        Raises:
            InvalidImageFormat: Image format is not allowed

        Returns:
            Figure: Figure object
        """
        figure = self._get_figure()

        if show:
            figure.show()

        if save:
            if format.upper() not in AllowedImageFormats.__members__:
                raise InvalidImageFormat(format)

            output_dir = Path("plots")
            output_dir.mkdir(exist_ok=True)
            filename = f"activity_overview_{self.year}"

            if format == "html":
                figure.write_html(output_dir / f"{filename}.html")
            else:
                figure.write_image(
                    file=output_dir / f"{filename}.{format}", format=format, scale=1
                )

        return figure
