from typing import Any, List

import dash_mantine_components as dmc
import numpy as np
from dash_extensions.enrich import DashBlueprint, dcc, html
from dash_iconify import DashIconify
from plotly import colors


def create_slider(topic_names: List[str], i: int) -> dmc.Group:
    return dmc.Group(
        [
            dmc.Select(
                label="Select Topic",
                id={"type": "slider_selector", "index": i},
                data=[
                    {"value": topic_id, "label": topic_name}
                    for topic_id, topic_name in enumerate(topic_names)
                ],
                value=0
            ),
            dmc.
        ]
    )


def create_blueprint(
    document_topic_matrix: np.ndarray,
    topic_names: List[str],
    **kwargs,
) -> DashBlueprint:
    # --------[ Creating app blueprint ]--------
    app_blueprint = DashBlueprint()
    app_blueprint.layout = html.Div(
        [
            dmc.Group(
                [
                    dmc.Stack(
                        [
                            dmc.Group(
                                [
                                    dmc.Title("Topic Sliders", order=2),
                                    dmc.ActionIcon(
                                        DashIconify(
                                            icon="material-symbols:add", width=30
                                        ),
                                        id="add_slider",
                                    ),
                                ],
                                grow=True,
                            )
                        ]
                    ),
                    dmc.Stack(id="sliders"),
                    dmc.Table(id="documents_table"),
                ],
                position="apart",
                grow=1,
                align="stretch",
                className="flex-1 p-3",
            ),
        ],
        className="""
        hidden
        """,
        id="words_container",
    )

    # --------[ Registering callbacks ]--------
    for blueprint in blueprints:
        blueprint.register_callbacks(app_blueprint)
    return app_blueprint
