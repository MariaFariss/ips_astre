# Student IPS/ASTRE Prediction Project

The primary goal of this project is to formulate hypotheses and anticipate the forthcoming option selections (Astre or IPS) made by students at our school. This prediction is founded on the analysis of questionnaire responses. Additionally, there is a web interface accessible for reviewing outcomes and making adjustments to the formulated hypotheses.

## Installation

Before starting, you need to install the necessary dependencies.

For the front-end, use npm:

```bash
npm install
```

For the script, use pip:

```bash
pip install -r requirements.txt
```

## Usage

To run the script, navigate to the src.script subfolder and run the following command:

```bash
uvicorn script:app --reload
```

To start the front-end server, use the following command:

```bash
npm run start
```

Hope you enjoy!!!