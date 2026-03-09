# Schema Review: coremeta4cat

Review conducted: 2026-03-09
Scope: Reaction, Characterization, Simulation, and combined CatalysisDataset application profiles
Method: Generated test data YAML files, ran `just test` (_test-schema, _test-python, _test-examples), iterated until all pass.

---

## Summary

All three test stages now pass (`just test` exits 0):

| Stage | Command | Result |
|-------|---------|--------|
| `_test-schema` | `gen-project` dry run | PASS |
| `_test-python` | regenerate datamodel + pytest | PASS (6/6) |
| `_test-examples` | `linkml-run-examples` JSON schema validation | PASS (7 examples) |

---

## Test data files created

| File | Target class | Profile |
|------|-------------|---------|
| `tests/data/valid/Synthesis-001.yaml` | Synthesis | synthesis (pre-existing) |
| `tests/data/valid/Characterization-001.yaml` | Characterization | characterization (new) |
| `tests/data/valid/Characterization-002.yaml` | Characterization | characterization (new) |
| `tests/data/valid/Reaction-001.yaml` | Reaction | reaction (new) |
| `tests/data/valid/Simulation-001.yaml` | Simulation | simulation (new) |
| `tests/data/valid/CatalysisDataset-001.yaml` | CatalysisDataset | combined (new) |

### File naming convention

`test_data.py` derives the target class name via `Path(filepath).stem.split("-")[0]`.
The user-preferred name `CatalysisDataset_Reac_Syn-001.yaml` would produce `CatalysisDataset_Reac_Syn`,
which is not a valid class name. The file is therefore named `CatalysisDataset-001.yaml`.

---

## Schema errors found and fixed

### Fix 1 — Simulation.realized_plan: multivalued conflicts with Python MRO

**File:** `src/coremeta4cat/schema/coremeta4cat_simulation_ap.yaml`
**Severity:** ERROR — broke Python test (TypeError at load time)

**Root cause:**
`Simulation.slot_usage.realized_plan` had `multivalued: true` + `inlined_as_list: true`.
`Simulation.__post_init__` converted `realized_plan` to a list, but the parent class
`DataGeneratingActivity.__post_init__` (line 1383 of generated `coremeta4cat.py`) then ran:
```python
self.realized_plan = Plan(**as_dict(self.realized_plan))
```
which received a list and raised `TypeError: unhashable type: 'list'`.

**Fix:** Removed `multivalued: true` and `inlined_as_list: true` from `Simulation.slot_usage.realized_plan`.
`realized_plan` is now a single `SimulationMethod` instance, consistent with Synthesis and Characterization.

**Impact:** Simulation-001.yaml changed `realized_plan` from a list to a single dict.

**Known limitation (not fixed):**
The generated Python datamodel does not dispatch polymorphism for `realized_plan`.
When a `DFT` subclass dict is provided, it is loaded as the abstract base class
(`SimulationMethod`, `CharacterizationTechnique`, `PreparationMethod`) and subclass-specific
fields (e.g. `exchange_correlation_functional`, `energy_cutoff`) are silently ignored.
This is a fundamental limitation of the current code generator. Users wishing to preserve
subclass fields must use the Pydantic model or deserialise manually.

---

### Fix 2 — Characterization: `equipment` not in JSON schema properties

**File:** `src/coremeta4cat/schema/coremeta4cat_characterization_ap.yaml`
**Severity:** ERROR — `_test-examples` rejected `equipment` as unexpected property

**Root cause:**
`equipment` was listed in `Characterization.slot_usage` but not in `Characterization.slots:`.
The LinkML JSON schema generator only includes properties for slots listed in `slots:`.
With `additionalProperties: false` on the generated JSON schema, `equipment` was rejected.

**Fix:** Added `- equipment` to `Characterization.slots:`.

---

### Fix 3 — Reaction: `product_identification_method` not in JSON schema properties

**File:** `src/coremeta4cat/schema/coremeta4cat_reaction_ap.yaml`
**Severity:** ERROR — `_test-examples` rejected `product_identification_method` as unexpected property

**Root cause:**
`product_identification_method` was listed in `Reaction.slot_usage` but had no entry in
the module's global `slots:` section and was not in `Reaction.slots:`.

**Fix:**
1. Added `- product_identification_method` to `Reaction.slots:`.
2. Added a complete slot definition to the `slots:` section of `coremeta4cat_reaction_ap.yaml`.

---

### Fix 4 — ProductIdentificationMethod: abstract class absent from JSON schema $defs

**File:** `src/coremeta4cat/schema/coremeta4cat_reaction_ap.yaml`
**Severity:** ERROR — `PointerToNowhere: '/$defs/ProductIdentificationMethod' does not exist`

**Root cause:**
`ProductIdentificationMethod` was declared `abstract: true`. LinkML's JSON schema generator
omits abstract classes from `$defs`, so the `$ref: '#/$defs/ProductIdentificationMethod'`
generated for the `product_identification_method` slot was a dangling reference.

**Fix:** Removed `abstract: true` from `ProductIdentificationMethod`.

**Note:** The class has no concrete subclasses in this module. Users should link
`CharacterizationTechnique` instances (GCMS, HPLC_MS, NMRSpectroscopy, …) from
`coremeta4cat_characterization_ap`. The `ProductIdentificationMethod` stub is
retained for backward compatibility.

**Design decision:**
The original schema intended `ProductIdentificationMethod` as a forward reference to
analytical techniques. A cleaner long-term solution would be to change the slot range to
`CharacterizationTechnique` directly. This is deferred as a future schema improvement.

---

## Known limitations (not fixed in this round)

### L1 — Polymorphic realized_plan / calculated_property: no subclass dispatch

**Affects:** Simulation, Characterization, Synthesis
**Symptom:** Concrete subclass fields (`exchange_correlation_functional`, `energy_cutoff`,
`lattice_parameter`, etc.) are silently ignored when loading YAML via the Python dataclass
loader. The abstract base class is instantiated instead.

**Reason:** `DataGeneratingActivity.__post_init__` wraps `realized_plan` as `Plan(...)`.
Subclass-specific `__post_init__` runs first (Simulation, Characterization), but the
parent class overwrites with `Plan`. No type discriminator is used.

**Workaround:** Use the Pydantic model (`coremeta4cat_pydantic.py`) or add a `type:` field
and implement a custom loader that dispatches on the type tag.

**Recommendation:** Add a `type` discriminator field to `Plan` and its subclasses, then
implement dispatch logic in `DataGeneratingActivity.__post_init__` (or switch to Pydantic).

---

### L2 — CatalysisDataset `was_generated_by` items: single-field JsonObj loader bug

**Symptom:** If a `was_generated_by` item contains only `id:` (one field), the
Python loader passes the entire `JsonObj` as a positional argument to `DataGeneratingActivity`,
setting `self.id = JsonObj(...)` instead of a string. Strict CURIE validation then fails.

**Workaround applied:** All `was_generated_by` items include at least `title: [...]` (a list)
alongside `id:`, so the JsonObj has multiple fields and resolves correctly.

**Recommendation:** Fix `_normalize_inlined_as_list` in the generated `coremeta4cat.py`
to always pass `id` as a keyword argument rather than as a positional argument.

---

### L3 — DCAT title/description must be arrays

**Affects:** `CatalysisDataset`, `DataGeneratingActivity`, and other DCAT-derived classes
**Symptom:** Scalar string values for `title` or `description` fail JSON schema validation
(type must be `["array", "null"]`).

**Workaround:** Always use YAML list syntax for these fields:
```yaml
title:
  - "My title string"
description:
  - "My description string"
```

**Note:** This is intentional DCAT-AP behaviour (multivalued for multilingual support),
but is surprising and should be documented in user-facing guides.

---

### L4 — recommended: true treated as required in JSON schema

**Affects:** Any slot with `recommended: true`
**Symptom:** Slots marked `recommended` are included in the JSON schema `required` array,
making them mandatory for `_test-examples` validation even if the user considers them optional.

**Current state:** Accepted as-is. The `_test-examples` data includes all recommended fields.

**Recommendation:** Review whether `recommended` should map to `required` in JSON schema,
or whether a custom annotation (e.g. `ifAbsent: WARN`) is more appropriate.

---

### L5 — File naming: CatalysisDataset_Reac_Syn-001.yaml incompatible with test_data.py

**Context:** The user expressed a preference for `CatalysisDataset_Reac_Syn-001.yaml`
to encode which sub-profiles are used.

**Constraint:** `test_data.py` uses `stem.split("-")[0]` to derive the class name.
`CatalysisDataset_Reac_Syn-001` → class name `CatalysisDataset_Reac_Syn` → invalid.

**Resolution:** File named `CatalysisDataset-001.yaml`. Sub-profile information is
documented in the file header comment instead.

**Recommendation:** Either update `test_data.py` to use a metadata field (e.g. `type:`)
to determine the target class, or adopt a naming convention that embeds the class name
before the first hyphen (e.g. `CatalysisDataset-ReacSyn-001.yaml`).

---

## Persistent LinkML generator warnings (informational)

These warnings appear on every `gen-project` run. They are upstream issues unrelated to
the coremeta4cat schema changes:

```
Slot 'CatalogueRecord_primary_topic': A class without identifiers (Any) cannot be 'inlined' as a dictionary.
Slot 'Dataset_frequency': A class without identifiers (Frequency) cannot be 'inlined' as a dictionary.
Enumeration QUDTQuantityKindEnum using `reachable_from` ... not supported yet. Will be silently ignored.
Slot has_part.inverse (part_of), has multi domains (...) — Multi ranges not yet implemented
```
