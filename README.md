#### A Predictive Gas Procurement & Imbalance Management Decision-Support System for Gas-Fired Power Generation

![Models](https://img.shields.io/badge/Models-ARIMAX%20|%20GBM%20|%20LSTM-orange.svg)
![Pipeline](https://img.shields.io/badge/Pipeline-Operational%20Ready-purple.svg)
![Research](https://img.shields.io/badge/Backed%20By-Peer--Reviewed%20Research-teal.svg)

🎯 Project Overview

This project is an exercise and development of a data-driven decision-support platform that integrates:
- Short-term natural gas demand forecasting for gas-fired generators
- Pipeline scheduling optimization under operational constraints
- Real-time imbalance monitoring and prediction
- Market intelligence dashboards for procurement decisions

The system would help natural gas trading in:
- Procurement gas more efficiently
- Schedule flows consistent with pipeline constraints
- Stay within imbalance tolerances
- Understand market drivers (weather, power demand, pipeline conditions, price spreads)

🔬 Research Foundations (Cited)
1. Pipeline Scheduling & External Drivers

- [An Analytical Study on the Correlations Between Natural Gas Pipeline Network Scheduling Decisions and External Environmental Factors](https://www.mdpi.com/1996-1073/18/13/3274?utm_source=copilot.com)

The MDPI paper “An Analytical Study on the Correlations Between Natural Gas Pipeline Network Scheduling Decisions and External Environmental Factors” shows that
temperature, supply, and energy consumption strongly influence pipeline scheduling decisions.
This supports the project’s inclusion of:
- Weather-driven demand forecasting
- Correlation analysis between power load and gas nominations
- Predictive imbalance alerts

2. Optimal Control for Gas Scheduling

- [Optimal Control for Scheduling and Pricing Intra-day Natural Gas Transport on Pipeline Networks](https://arxiv.org/abs/1912.02895?utm_source=copilot.com)

The paper “Optimal Control for Scheduling and Pricing Intra-day Natural Gas Transport on Pipeline Networks” (Zlotnik et al.) provides a mathematical and optimization-based framework for:
- Gas flow scheduling
- Compressor constraints
- Time-dependent injections/withdrawals
- Economic valuation of gas at each node

This supports the project’s:
- Optimization engine for procurement & scheduling
- Pipeline-aware imbalance management
- Locational gas value estimation

3. Production & Marketing Scheduling

- [Production and marketing scheduling of natural gas based on table-manipulation method and Lingo software](https://www.researchgate.net/publication/356428191_Production_and_marketing_scheduling_of_natural_gas_based_on_table-manipulation_method_and_Lingo_software)

The ResearchGate paper on “Production and marketing scheduling of natural gas…” demonstrates structured approaches to allocating gas supply across multiple destinations. This supports:
- Allocation optimization
- Scenario-based procurement strategies
- Multi-node scheduling logic

🏗️ Project Architecture

gas_ops_rnd/\
├─ pyproject.toml / requirements.txt\
├─ README.md\
├─ data/\
│  ├─ raw/\
│  ├─ interim/\
│  └─ processed/\
├─ configs/\
│  ├─ forecasting.yaml\
│  └─ imbalance.yaml\
├─ notebooks/\
│  ├─ 01_eda_forecasting.ipynb\
│  ├─ 02_model_benchmarking.ipynb\
│  └─ 03_imbalance_exploration.ipynb\
├─ gas_ops/\
│  ├─ __init__.py\
│  ├─ io/\
│  │  ├─ loaders.py\
│  │  └─ pipelines.py\
│  ├─ features/\
│  │  ├─ weather_features.py\
│  │  ├─ power_features.py\
│  │  └─ gas_features.py\
│  ├─ models/\
│  │  ├─ arimax.py\
│  │  ├─ gradient_boosting.py\
│  │  ├─ lstm_seq2seq.py\
│  │  └─ ensemble_forecaster.py\
│  ├─ forecasting/\
│  │  ├─ dataset.py\
│  │  ├─ train.py\
│  │  └─ evaluate.py\
│  ├─ imbalance/\
│  │  ├─ dataset.py\
│  │  ├─ risk_model.py\
│  │  ├─ rules_engine.py\
│  │  └─ alerts.py\
│  └─ utils/\
│     ├─ metrics.py\
│     └─ logging.py\
└─ scripts/\
   ├─ run_forecasting_train.py\
   ├─ run_forecasting_infer.py\
   └─ run_imbalance_monitor.py

#### License
This project is licensed under the [MIT License](LICENSE).  
