import yaml
from pathlib import Path
from typing import Dict, List, Set, Optional

# ── Module filenames (relative to the schema directory) ────────────────────────
MODULE_FILES = [
    "catcore_common.yaml",
    "catcore_synthesis_ap.yaml",
    "catcore_characterization_ap.yaml",
    "catcore_reaction_ap.yaml",
    "catcore_simulation_ap.yaml",
    "catcore.yaml",
]


# ─────────────────────────────────────────────────────────────────────────────
# Schema loading & merging
# ─────────────────────────────────────────────────────────────────────────────

def load_yaml_file(file_path: str) -> dict:
    path = Path(file_path)
    if not path.exists():
        print(f"  [WARNING] Module not found, skipping: {file_path}")
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def merge_schemas(modules: List[dict]) -> dict:
    """
    Merge all module dicts into one flat schema.

    Classes that appear in multiple modules (e.g. Synthesis is defined in
    catcore_synthesis_ap and stubbed in catcore.yaml) are intelligently merged:
    slot_usage and slots lists are unioned; all other keys let the later module win.
    """
    merged: dict = {"prefixes": {}, "classes": {}, "slots": {}, "enums": {}}

    for module in modules:
        if not module:
            continue

        for key in ("id", "name", "title", "description", "license",
                    "version", "default_prefix", "default_range"):
            if key not in merged and key in module:
                merged[key] = module[key]

        for section in ("prefixes", "classes", "slots", "enums"):
            section_data = module.get(section) or {}
            for name, definition in section_data.items():
                if section == "classes" and name in merged["classes"]:
                    existing = merged["classes"][name]
                    incoming = definition or {}
                    if "slot_usage" in incoming:
                        existing.setdefault("slot_usage", {})
                        existing["slot_usage"].update(incoming["slot_usage"])
                    if "slots" in incoming:
                        existing_slots = existing.get("slots", [])
                        for s in incoming["slots"]:
                            if s not in existing_slots:
                                existing_slots.append(s)
                        existing["slots"] = existing_slots
                    for k, v in incoming.items():
                        if k not in ("slot_usage", "slots"):
                            existing[k] = v
                else:
                    merged[section][name] = dict(definition) if isinstance(definition, dict) else definition

    return merged


def load_merged_schema(schema_dir: str) -> dict:
    schema_dir_path = Path(schema_dir)
    modules = []
    for filename in MODULE_FILES:
        full_path = schema_dir_path / filename
        print(f"  Loading: {full_path}")
        modules.append(load_yaml_file(str(full_path)))

    merged = merge_schemas(modules)
    print(f"  Merged schema: {len(merged.get('classes', {}))} classes, "
          f"{len(merged.get('slots', {}))} slots\n")
    return merged


# ─────────────────────────────────────────────────────────────────────────────
# BUG FIX 1: Mixin slot resolution
#
# In LinkML, a class can declare `mixins: [MixinA, MixinB]`.  The converter's
# original get_class_slots() only looked at `slots`, completely ignoring mixin
# contributions.  This means e.g. PowderXRD was missing xray_source/monochromator
# (from XRaySourceMixin), and BandGap was missing 5 slots from two mixins.
#
# get_all_class_slots() walks the full mixin chain and returns the complete
# deduplicated slot list: own slots first, then each mixin's slots in order.
# ─────────────────────────────────────────────────────────────────────────────

def get_all_class_slots(schema: dict, class_name: str,
                        _seen: Optional[Set[str]] = None) -> List[str]:
    """
    Return ALL slots available on a class, including those contributed by mixins
    (resolved recursively so that mixin-of-mixin chains work too).

    Order: own `slots` first, then each mixin's slots in declaration order.
    Duplicates are removed (first occurrence wins).
    """
    if _seen is None:
        _seen = set()
    if class_name in _seen:
        return []
    _seen.add(class_name)

    classes  = schema.get("classes", {})
    class_def = classes.get(class_name, {})

    own_slots   = class_def.get("slots", []) or []
    mixin_names = class_def.get("mixins", []) or []

    # Gather mixin slots (recursively, in case mixins themselves have mixins)
    mixin_slots: List[str] = []
    for mixin_name in mixin_names:
        for s in get_all_class_slots(schema, mixin_name, _seen.copy()):
            if s not in mixin_slots:
                mixin_slots.append(s)

    # Deduplicate: own slots take priority
    combined: List[str] = list(own_slots)
    for s in mixin_slots:
        if s not in combined:
            combined.append(s)

    return combined


# ─────────────────────────────────────────────────────────────────────────────
# BUG FIX 2: Mixin class filtering in subclass listings
#
# The original get_subclasses() returned mixin classes (e.g. DryingMixin,
# XRaySourceMixin) alongside real output classes because both use `is_a`.
# Mixin classes are purely internal slot-containers and must NOT appear as
# subclasses in the generated docs.
#
# is_mixin() checks the `mixin: true` flag set on each mixin class definition.
# get_subclasses() now skips classes where is_mixin() returns True.
# ─────────────────────────────────────────────────────────────────────────────

def is_mixin(schema: dict, class_name: str) -> bool:
    """Return True if the class is a LinkML mixin (mixin: true)."""
    return bool(schema.get("classes", {}).get(class_name, {}).get("mixin", False))


def get_subclasses(schema: dict, parent_class: str) -> List[str]:
    """
    Return all (recursive) non-mixin subclasses of parent_class.
    Mixin classes are excluded from the result.
    """
    subclasses = []
    for class_name, class_def in schema.get("classes", {}).items():
        if class_def.get("is_a") == parent_class and not is_mixin(schema, class_name):
            subclasses.append(class_name)
            subclasses.extend(get_subclasses(schema, class_name))
    return subclasses


# ─────────────────────────────────────────────────────────────────────────────
# Standard helpers
# ─────────────────────────────────────────────────────────────────────────────

def get_slot_details(schema: dict, slot_name: str) -> dict:
    return schema.get("slots", {}).get(slot_name, {})


def is_class_in_schema(schema: dict, class_name: str) -> bool:
    return class_name in schema.get("classes", {})


def snake_to_readable(text: str) -> str:
    return text.replace("_", " ")


def expand_curie(schema: dict, value: str) -> str:
    if ":" not in value or value.startswith("http"):
        return value
    prefix, local = value.split(":", 1)
    prefixes = schema.get("prefixes", {})
    if prefix not in prefixes:
        return value
    entry = prefixes[prefix]
    if isinstance(entry, str):
        base = entry
    elif isinstance(entry, dict):
        base = (entry.get("prefix_reference") or entry.get("uri")
                or entry.get("prefix") or "")
    else:
        return value
    if not base:
        return value
    return base + local if base.endswith(("/", "#")) else base + local


def get_slot_cardinality(schema: dict, class_name: str,
                         slot_name: str, slot_details: dict) -> str:
    """
    Determine the cardinality label for a slot in the context of a class.
    Falls back to slot-level required/recommended flags when no slot_usage
    override exists (important for modular files where cardinality is set
    directly on the slot definition rather than in slot_usage).
    """
    class_def = schema.get("classes", {}).get(class_name, {})
    usage = class_def.get("slot_usage", {}).get(slot_name, {})

    required    = usage.get("required",    slot_details.get("required",    False))
    recommended = usage.get("recommended", slot_details.get("recommended", False))
    multivalued = usage.get("multivalued", slot_details.get("multivalued", False))

    parts = []
    if required:
        parts.append("Required")
    elif recommended:
        parts.append("Recommended")
    else:
        parts.append("Optional")
    if multivalued:
        parts.append("Multivalued")
    return ", ".join(parts)


# ─────────────────────────────────────────────────────────────────────────────
# Markdown formatters
# ─────────────────────────────────────────────────────────────────────────────

def format_class_markdown(
    schema: dict,
    class_name: str,
    level: int = 3,
    processed_classes: Optional[Set[str]] = None,
    parent_class: Optional[str] = None,
) -> str:
    if processed_classes is None:
        processed_classes = set()
    if class_name in processed_classes:
        return ""
    processed_classes.add(class_name)

    classes   = schema.get("classes", {})
    class_def = classes.get(class_name, {})

    description = class_def.get("description", "No description available")
    class_uri   = class_def.get("class_uri", "")
    is_abstract = class_def.get("abstract", False)
    schema_link = f"./elements/{class_name}.md"

    md = f'<details markdown="1">\n'
    md += f'<summary><strong>{snake_to_readable(class_name)}</strong></summary>\n\n'

    if is_abstract:
        md += "**Abstract Class**\n\n"

    md += f"**Description:** {description}\n\n"

    if class_uri:
        expanded = expand_curie(schema, class_uri)
        md += f"**CURIE:** [`{class_uri}`]({expanded})\n\n"

    md += f"**Schema Reference:** [{class_name}]({schema_link})\n\n"

    # BUG FIX 1 applied: use get_all_class_slots instead of class_def.get('slots')
    slots = get_all_class_slots(schema, class_name)
    if slots:
        md += "**Slots**\n\n"
        for slot_name in slots:
            slot_details = get_slot_details(schema, slot_name)
            md += format_slot_markdown(
                schema, slot_name, slot_details, level + 2,
                processed_classes.copy(), class_name
            )

    md += (
        f"<p>\n"
        f"      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new"
        f"?template=term_improvement.yaml&title=Term%20Feedback:%20{class_name}"
        f' target="_blank" class="md-button md-button--primary">\n'
        f"        💡 Submit Term Feedback\n"
        f"      </a>\n"
        f"    </p>"
    )
    md += "</details>\n\n"
    return md


def format_slot_markdown(
    schema: dict,
    slot_name: str,
    slot_details: dict,
    level: int = 3,
    processed_classes: Optional[Set[str]] = None,
    parent_class: Optional[str] = None,
) -> str:
    if processed_classes is None:
        processed_classes = set()

    description = slot_details.get("description", "No description available")
    range_type  = slot_details.get("range", "string")
    slot_uri    = slot_details.get("slot_uri", "")
    unit        = slot_details.get("unit", {})
    schema_link = f"./elements/{slot_name}.md"

    cardinality         = ""
    striped_cardinality = ""
    if parent_class:
        cardinality         = get_slot_cardinality(schema, parent_class, slot_name, slot_details)
        cardinality         = f" ({cardinality})"
        striped_cardinality = cardinality.replace("(", "").replace(")", "")

    md  = f'<details markdown="1">\n'
    md += f"<summary><strong>{snake_to_readable(slot_name)}</strong>{cardinality}</summary>\n\n"
    md += f"**Description:** {description}\n\n"
    md += f"**Data Type:** {range_type}\n\n"
    md += f"**Cardinality:** {striped_cardinality}\n\n"

    if slot_uri:
        expanded = expand_curie(schema, slot_uri)
        md += f"**CURIE:** [`{slot_uri}`]({expanded})\n\n"

    md += f"**Schema Reference:** [{slot_name}]({schema_link})\n\n"

    if unit:
        ucum_code = unit.get("ucum_code", "")
        if ucum_code:
            md += f"**Unit:** {ucum_code}\n\n"

    if is_class_in_schema(schema, range_type) and not is_mixin(schema, range_type):
        md += "**Data Type Class Details:**\n\n"
        md += format_class_markdown(schema, range_type, level, processed_classes, None)

        # BUG FIX 2 applied: get_subclasses already filters out mixins
        subclasses = get_subclasses(schema, range_type)
        if subclasses:
            md += f"**Possible Subclasses / Enumerations of {snake_to_readable(range_type)}:**\n\n"
            for subclass in subclasses:
                if subclass not in processed_classes:
                    md += format_class_markdown(
                        schema, subclass, level + 1, processed_classes, None
                    )

    md += (
        f"<p>\n"
        f"  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new"
        f"?template=term_improvement.yaml&title=Term%20Feedback:%20{slot_name}"
        f' target="_blank" class="md-button md-button--primary">\n'
        f"    💡 Submit Term Feedback\n"
        f"  </a>\n"
        f"</p>"
    )
    md += "</details>\n\n"
    return md


LEGEND = """\
<details markdown="1"><summary markdown="1"> **Legend** </summary>

- **Description:**A short description for Comprehension purposes

- **Data Type:** This specifies exactly what kind of information belongs in this field. Most simply, it could be a direct value, such as a number (float) or a piece of text (string). However, the Data Type can also point to another Class in the schema. When this happens, the field is not just a single value; it becomes a structured container. Designating a Class as the Data Type causes the field to contain a complete structured record, defined entirely by its own comprehensive collection of specific fields. Consequently, this allows for the systematic construction of complex data structures via organized, nested information layers within the broader schema architecture.

- **Cardinality:** This controls how many entries a specific data field must have. It defines if a field is required or optional, and whether it can accept a single value versus a list of multiple values.

- **CURIE:** A CURIE (Compact URI) is a short, easy-to-read reference that acts as a useful shortcut for a long, complex web address. Instead of seeing a full URL, you will see a two-part reference like gene:symbol, where the parts are separated by a colon. The first part is the prefix (a short code for the source website), and the second is the local identifier for the specific item. This structure is much easier to read and type, making the schema less cluttered and reducing errors. The full web link (URI) for the CURIE is always available if you click the provided link.

- **Schema Reference:** This link directs you to the complete, technical documentation for this part of the schema. This detailed view is generated automatically by LinkML's documentation tool and provides all underlying rules, data types, and complex relationships for expert users and developers.

- **Slots:** A Slot represents an individual data field or attribute that belongs to a specific Class (entity type) within the schema. If a Class defines an entity like 'Book', the Slots define the individual pieces of information about that book, such as the 'title', 'author', and 'ISBN'. Essentially, Slots are the essential building blocks that define the characteristics and permissible data for every record in the schema.

- **Enumerations:** Often called an Enum, Enumerations are a predefined, fixed list of permissible values that a Slot can accept. It is used to strictly limit the available choices for a data field to ensure consistency and prevent errors. For example, a 'Status' field might be restricted to the Enumeration list of only 'Active', 'Inactive', or 'Pending'. Any data entered that is not on this limited list is considered invalid by the schema.

</details>"""


def generate_markdown_for_main_class(
    schema: dict, main_class: str, output_file: str
):
    classes        = schema.get("classes", {})
    main_class_def = classes.get(main_class, {})
    class_uri      = main_class_def.get("class_uri", "")
    is_abstract    = main_class_def.get("abstract", False)

    md_content  = f"# {snake_to_readable(main_class)}\n\n"
    md_content += "test description\n\n"

    if is_abstract:
        md_content += "**Abstract Class**\n\n"

    if class_uri:
        md_content += f"**CURIE:** [`{class_uri}`]({class_uri})\n\n"

    # BUG FIX 1 applied: use get_all_class_slots for the main class too
    slots = get_all_class_slots(schema, main_class)
    if slots:
        md_content += LEGEND + "\n"
        md_content += "## Slots\n\n"
        processed_classes: Set[str] = set()
        for slot_name in slots:
            slot_details = get_slot_details(schema, slot_name)
            md_content += format_slot_markdown(
                schema, slot_name, slot_details, 3,
                processed_classes.copy(), main_class
            )

    processed_classes = {main_class}
    # BUG FIX 2 applied: get_subclasses already filters mixin classes
    subclasses = get_subclasses(schema, main_class)

    if subclasses:
        md_content += "## Subclasses\n\n"

        direct_subclasses = [
            sc for sc in subclasses
            if classes.get(sc, {}).get("is_a") == main_class
        ]

        for subclass in direct_subclasses:
            if subclass not in processed_classes:
                md_content += format_class_markdown(
                    schema, subclass, level=3,
                    processed_classes=processed_classes
                )

            nested_subclasses = [
                sc for sc in subclasses
                if classes.get(sc, {}).get("is_a") == subclass
            ]
            if nested_subclasses:
                md_content += f"**Nested Subclasses of {snake_to_readable(subclass)}:**\n\n"
                for nested in nested_subclasses:
                    if nested not in processed_classes:
                        md_content += format_class_markdown(
                            schema, nested, level=4,
                            processed_classes=processed_classes
                        )

    main_class_lower = main_class.lower()
    md_content += (
        f'<iframe\n'
        f'    src="assets/chart_{main_class_lower}.html"\n'
        f'    width="100%"\n'
        f'    height= "800vh"\n'
        f'    style="border: 2px solid #5C88DA; background-color: #F0F8FF;\n'
        f'    "\n'
        f'    allowfullscreen\n'
        f'></iframe>'
    )

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(md_content)

    print(f"  ✓ {output_file}")


# ─────────────────────────────────────────────────────────────────────────────
# Smoke-test: run against the uploaded files and report slot counts
# ─────────────────────────────────────────────────────────────────────────────

def smoke_test(schema: dict):
    """Print expected vs resolved slot counts for key classes."""
    tests = {
        # class                expected_min_slots  reason
        "Synthesis":           (6,  "6 direct slots"),
        "Characterization":    (5,  "5 direct slots"),
        "Reaction":            (8,  "8 direct slots"),
        "Simulation":          (2,  "2 direct slots"),
        "WetImpregnation":     (1,  "inherits from Impregnation via is_a chain → but Impregnation has 3+mixin slots"),
        "Impregnation":        (9,  "3 own + DryingMixin(4) + CalcinationMixin(6)"),
        "CoPrecipitation":     (14, "PrecipitationMixin(4) + DryingMixin(4) + CalcinationMixin(6)"),
        "PowderXRD":           (10, "8 own + XRaySourceMixin(2)"),
        "BandGap":             (12, "7 own + MaterialDescriptorMixin(2) + DFTSettingsMixin(3)"),
        "DielectricTensors":   (7,  "2 own + MaterialDescriptorMixin(2) + DFTSettingsMixin(3)"),
    }
    print("── Smoke test: resolved slot counts ─────────────────────────────")
    all_ok = True
    for cls, (expected_min, reason) in tests.items():
        resolved = get_all_class_slots(schema, cls)
        ok = len(resolved) >= expected_min
        status = "✓" if ok else "✗"
        if not ok:
            all_ok = False
        print(f"  {status} {cls}: {len(resolved)} slots (expected ≥{expected_min} — {reason})")
        if not ok:
            print(f"       got: {resolved}")
    print()

    print("── Smoke test: mixin filtering ───────────────────────────────────")
    sim_subclasses  = get_subclasses(schema, "Simulation")
    char_subclasses = get_subclasses(schema, "Characterization")
    syn_subclasses  = get_subclasses(schema, "Synthesis")

    mixin_names = [n for n, d in schema.get("classes", {}).items() if d.get("mixin")]
    leaked_sim  = [c for c in sim_subclasses  if c in mixin_names]
    leaked_char = [c for c in char_subclasses if c in mixin_names]
    leaked_syn  = [c for c in syn_subclasses  if c in mixin_names]

    for label, leaked, subclasses in [
        ("Simulation",       leaked_sim,  sim_subclasses),
        ("Characterization", leaked_char, char_subclasses),
        ("Synthesis",        leaked_syn,  syn_subclasses),
    ]:
        if leaked:
            print(f"  ✗ {label}: mixin classes leaked into subclasses: {leaked}")
            all_ok = False
        else:
            print(f"  ✓ {label}: {len(subclasses)} subclasses, no mixins leaked")

    print()
    print("── Overall:", "ALL TESTS PASSED ✓" if all_ok else "SOME TESTS FAILED ✗")
    print()


# ─────────────────────────────────────────────────────────────────────────────
# Entry point
# ─────────────────────────────────────────────────────────────────────────────

def main(schema_dir: str, output_dir: str = "."):
    """
    Load all CatCore module YAML files from schema_dir, merge them, optionally
    run the smoke test, then generate one Markdown doc page per main class.
    """
    print(f"\nLoading CatCore modules from: {schema_dir}")
    schema = load_merged_schema(schema_dir)

    smoke_test(schema)

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    main_classes = {
        "Synthesis":        "synthesis.md",
        "Characterization": "characterization.md",
        "Reaction":         "reaction.md",
        "Simulation":       "simulation.md",
    }

    print(f"Generating Markdown docs in: {output_dir}")
    for main_class, filename in main_classes.items():
        output_file = output_path / filename
        generate_markdown_for_main_class(schema, main_class, str(output_file))

    print(f"\n✓ All done — {len(main_classes)} files written to '{output_dir}'.")

if __name__ == "__main__":
    # ── Edit these two paths to match your local setup ──────────────────────
    schema_dir = "./schema"
    output_dir = "./docs"
    # ────────────────────────────────────────────────────────────────────────
    main(schema_dir, output_dir)
