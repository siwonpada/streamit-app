# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="MLB Player HR Predictor",
        page_icon="🔮",
    )

    st.write("# Welcome MLB Player HR Predictor 👋")

    st.markdown(
        """
        MLB Player HR Predictor is a web application that predicts the number of home runs a Major League Baseball player will hit in a season.

        The application uses a machine learning model trained on data from the 2022 MLB seasons. The model takes a player's statistics from the previous season as input and outputs the predicted number of home runs for the upcoming season.

        This application has two main features:

        1. **Predict HRs**: Enter a player's statistics from the previous season to get the predicted number of home runs for the upcoming season.

        2. **Player Comparison**: Compare the predicted number of home runs for two players based on their statistics from the previous season.
    """
    )


if __name__ == "__main__":
    run()
