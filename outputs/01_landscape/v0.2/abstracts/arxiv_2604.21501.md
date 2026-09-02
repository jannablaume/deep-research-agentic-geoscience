Source: https://arxiv.org/html/2604.21501 (arXiv HTML rendering, fetched query_id 20)

GeoMind is an agentic workflow for lithology classification with reasoned tool invocation.
It organizes lithology interpretation as a multi-step decision process coordinated by a
Planner-Executor-Reflector architecture, with perception, reasoning, and analysis modules
that respectively translate raw well logs into semantic trends, infer lithology hypotheses
from multi-source evidence, and verify predictions against stratigraphic constraints.
Experiments on four benchmark well-log datasets (SEAM, Facies, FORCE, GeoLink) demonstrate
that GeoMind consistently outperforms strong baselines (XGBoost, InceptionTime, MOMENT,
GPT4TS, and domain-specific methods) in classification performance while providing
transparent and traceable decision-making processes, with improvements of approximately 5.7
F1 points on FORCE and 3.4 points on Facies. Code is available at
https://github.com/lqzxt/GeoMind.
