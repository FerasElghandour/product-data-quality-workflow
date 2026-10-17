# Reproduction and benchmark scope

The notebook can now execute noninteractively. A reusable product gate validates schema, unique identifiers, rating/price ranges and whitespace-only titles before selection.

## Execute a recorded profile

```sh
python run_reproduction.py --profile checks --output reproduced/checks
```

Use a new output directory for each run. The driver writes command logs, source/input SHA-256 values, versions and an explicit outcome. It does not silently download data or turn generated fixtures into dataset-performance claims.

| Profile | Actual scope | Required inputs |
|---|---|---|
| `checks` | Source parsing only; not model training or behavior verification | None |
| `full-notebook` | Generated100-record workflow; export/readback and filtering, not real review-corpus performance | None |

Supply named paths with `--input name=/absolute/path`. Exact commands are versioned in [reproduction.json](reproduction.json); direct training commands and preparation contracts are below.

## Evidence boundary

The notebook generates its demonstration records. This is a data-quality utility, not a recommendation-accuracy or commercial-impact benchmark.

Keep input acquisition and source credits in [DATA.md](DATA.md). Historical results, new reference runs and small contract fixtures have separate evidential scope.

## Recorded command definitions

### checks

```text
{python} scripts/validate_source.py
{python} test_quality.py
```

### full-notebook

```text
{python} reproduce.py --output {output}/notebook
```

`{python}` is the current interpreter. `{output}` is the new run directory. `{input:name}` refers to a named absolute input path supplied to the driver. Install declared dependencies in a clean environment before executing. Never execute untrusted serialized models or notebooks.
