# 07 Periphery

The neighbouring literature that the harvest retrieved and that screening did not admit.
Counts below are harvest `n_available` from `queries.csv` and screening `cut_reason` tallies.

[Certain] Twenty API calls were scoped as periphery (`q021`–`q030`, OpenAlex and arXiv).
OpenAlex `n_available` on those calls was 902 + 3515 earth observation, 2144 + 977 climate
and atmosphere, 91 + 93 ocean, 616 + 607 planetary, and 1057 + 975 geoscience_general.

[Certain] Screening assigned 347 records `cut_reason: periphery`. Of records given a
periphery subfield at screening, 221 were `earth_observation`, 83 `climate_atmosphere`,
17 `ocean`, 9 `planetary`, and 17 `geoscience_general`. A further 284 were cut
`not-geoscience` and 114 `not-agentic`; those are not periphery in the schema sense.

[Certain] Earth-observation queries were the largest neighbour. `q022:openalex`
(`n_available` 3515) and `q021:openalex` (902) together dominate the harvest volume
outside the ten core subfields. The shortlist still contained many remote-sensing
multi-agent papers whose output is a land-cover map or a satellite-image caption rather
than a subsurface artefact; those were cut as periphery rather than admitted under
`engineering_geology` or `mining`.

[Certain] Climate and atmosphere is the second-largest neighbour (`q023:openalex`
`n_available` 2144; `q024:openalex` 977). Ocean is the smallest of the four named
neighbours (`q025:openalex` 91; `q026:openalex` 93). Planetary sits between them
(`q027:openalex` 616; `q028:openalex` 607).

[Certain] `geoscience_general` was harvested as periphery (`q029`, `q030`) and used as
the cut for sources whose output is generic research assistance — literature search, data
discovery, code generation, question answering over mixed Earth-science content — rather
than an artefact in one of the ten core subfields. Seventeen screened records carry that
subfield as `cut_reason: periphery`.

[Likely] The periphery is not a thin halo around a large core. On OpenAlex
`n_available` alone, the four named neighbour domains plus `geoscience_general` exceed
several individual core subfields, including mining (`q013:openalex` 47) and inversion
(`q017:openalex` 75). That comparison is of query-hit volume, not of admitted systems.

[Absent-searched] No dedicated periphery harvest was run for hydrology-as-surface-water or ecology (`q005`, `q006`, `q021`–`q030`); those topics appear only where they matched a core or named-periphery query.
