# Codebook: Reconstructed Multimodal Music Mapping (MMM) Tables

## Scope and reconstruction method

This release transcribes the paper’s three tabular summaries and its reported inter-rater reliability claim into CSV files and one Excel workbook. Textual entries are carried over from the tables; only typographic cleanup (for example, removing quotation marks around track titles) and column/header normalization have been applied. No numeric counts, annotations, or observations were inferred from the audio files.

**Important sample-size disclaimer:** The paper does not report an overall **N=36** or per-track *n*. These values are not supplied or assumed in this reconstruction. The reported reliability subset’s size and composition are also not specified.

## Files and sheets

- `mmm_schema_table_reconstructed.csv` — reconstructed Table 1 schema summary (paper pp. 38–39).
- `mmm_track_summary_reconstructed.csv` — three-track comparison (pp. 47–48).
- `acoustic_cognitive_correspondence_reconstructed.csv` — acoustic–cognitive correspondence table (pp. 48–50).
- `reliability_report_reconstructed.csv` — κ=.84 reporting (pp. 34 and 51).
- `mmm_reconstructed_master.xlsx` — the same four datasets on separate sheets (`mmm_schema_table`, `mmm_track_summary`, `acoustic_cognitive_correspondence`, `reliability_report`).

## Column definitions and provenance

### Schema table

| Column | Definition | Status |
|---|---|---|
| `schema` | Image-schema label (FORCE, PATH, CONTAINER, BLOCKAGE, UP, or DOWN). | Directly reported in source table. |
| `primary_sonic_cues` | Principal acoustic cues associated with the schema. | Directly reported. |
| `linguistic_structural_correlates` | Linguistic and/or structural correlates associated with the schema. | Directly reported; preserves the combined source-table category. |
| `experiential_function` | Primary experiential function associated with the schema. | Directly reported. |
| `source_doc` | Filename of the source document. | Traceability metadata added during reconstruction. |
| `source_pages` | Printed/document page range attributed to the table. | Traceability metadata; page ranges follow the task/source table location. |

### Track summary

| Column | Definition | Status |
|---|---|---|
| `track` | Track title in the comparison. | Directly reported; quotation marks normalized away. |
| `dominant_schemas` | Dominant schema(s) assigned to the track. | Directly reported. |
| `acoustic_profile` | Main sonic configuration for the track. | Directly reported; source heading normalized to this field name. |
| `conceptual_pattern` | Conceptual pattern listed for the track. | Directly reported. |
| `emergent_meaning` | Emergent meaning listed for the track. | Directly reported. |
| `source_doc` | Filename of the source document. | Traceability metadata. |
| `source_pages` | Printed/document page range attributed to the comparison. | Traceability metadata. |

### Acoustic–cognitive correspondence

| Column | Definition | Status |
|---|---|---|
| `sonic_evidence` | Acoustic evidence item. | Directly reported. |
| `linguistic_evidence` | Linguistic evidence item. | Directly reported. |
| `structural_evidence` | Structural evidence item. | Directly reported. |
| `mapping_schema` | Resulting image-schema mapping. | Directly reported; source heading normalized to this field name. |
| `source_doc` | Filename of the source document. | Traceability metadata. |
| `source_pages` | Printed/document page range attributed to the table. | Traceability metadata. |

### Reliability report

| Column | Definition | Status |
|---|---|---|
| `metric` | Reliability statistic named in the paper. | Directly reported. |
| `value` | Reported value of the statistic. | Directly reported (κ = .84). |
| `subset_n_reported` | Number of items in the independently coded subset, if specified. | Not reported; left blank. |
| `subset_details_reported` | Description of the subset, if specified. | “Not reported”; the text only states that a second coder evaluated a subset. |
| `reproducible_from_paper` | Whether the reported reliability statistic can be independently reproduced from the paper’s available detail. | Reconstruction judgment: `No`; the subset data/size and coder-level decisions are not provided. |
| `notes` | Concise supporting qualification about the reliability claim. | Reconstructed explanatory note based on the paper’s text; no data added. |
| `source_doc` | Filename of the source document. | Traceability metadata. |
| `source_pages` | Pages where the reliability claim is reported. | Traceability metadata. |

## Directly observed vs. reconstructed/derived

The schema, track comparison, and correspondence rows are transcriptions of information explicitly present in the paper’s tables. CSV column names are normalized to the requested snake_case names; these names do not change the meaning of the source fields. The reliability value is explicitly reported in the paper. The blank subset count, `Not reported` subset details, and `No` reproducibility assessment encode the absence of enough published detail to reconstruct the κ calculation. Source filenames and page references are traceability fields rather than analytical observations. No track-level or overall sample counts are created.

## Citation and traceability

Source for all rows: *Cognitive Mapping of Multimodal Sonic Environments UTOPIA* (`Cognitive Mapping of Multimodal Sonic Environments UTOPIA.docx`). Each row includes `source_doc` and `source_pages` fields so records remain traceable when separated from the workbook. Page references identify the requested table/claim locations: schema table pp. 38–39; track comparison pp. 47–48; acoustic–cognitive correspondence pp. 48–50; reliability claims pp. 34 and 51.
