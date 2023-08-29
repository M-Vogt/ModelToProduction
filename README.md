# ModelToProduction
Task 1 for course DLBDSMTP01 B.Sc. Data Science

The scripts are formatted with black with the default configuration.

## Running the project

In order to start the project, make sure to have python installed with poetry package manager.
Install the dependencies via the CLI using poetry

    poetry install

To generate a dataset for training the model run

    poetry run poe gen_data

To train the model with the generated dataset run

    poetry run poe train_model

To run the server, execute

    poetry run poe serve

in your terminal. Hint: make sure to have the `dev` dependencies installed.
Subsequently in a second terminal run

    poetry run poe sensors

in your terminal to start sending simulated sensor values to the server for anomaly detection.
