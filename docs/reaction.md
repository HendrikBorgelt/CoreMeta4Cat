# Reaction

**Description:** The data class 'Reaction' describes the minimum information which should be reported 
with research data concerning the reaction for which the catalyst is applied.

---

## Main Class

<details>
<summary>### Reaction</summary>

**Description:** The data class 'Reaction' describes the minimum information which should be reported 
with research data concerning the reaction for which the catalyst is applied.

**URI:** `catcore:Reaction`

#### Slots (7)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>Reaction_catalyst_quantity</strong></summary>

**Description:** Quantity of catalyst used

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:catalyst_quantity`

**Unit:** g

</details>

<details>
<summary><strong>Reaction_reactor_design_type</strong></summary>

**Description:** Type of reactor design

**Range:** ReactorDesignType

**Multivalued:** Yes

**URI:** `voc4cat:0007018`

**Range Class Details:**

<details>
<summary>##### ReactorDesignType</summary>

**Abstract Class**

**Description:** Type of reactor design used

**URI:** `catcore:ReactorDesignType`

#### Slots (1)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

</details>

**Subclasses of ReactorDesignType:**

<details>
<summary>###### ElectrochemicalReactor</summary>

**Description:** Electrochemical reactor

**URI:** `voc4cat:0000193`

#### Slots (1)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

</details>

<details>
<summary>###### CSTR</summary>

**Description:** Continuous stirred tank reactor

**URI:** `voc4cat:0007019`

#### Slots (1)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

</details>

<details>
<summary>###### PlugFlowReactor</summary>

**Description:** Plug flow reactor model

**URI:** `voc4cat:0007102`

#### Slots (1)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

</details>

<details>
<summary>###### Autoclave</summary>

**Description:** Autoclave reactor

**URI:** `NCIT:C93052`

#### Slots (1)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

</details>

<details>
<summary>###### SlurryReactor</summary>

**Description:** Slurry reactor

**URI:** `catcore:SlurryReactor`

#### Slots (1)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

</details>

<details>
<summary>###### Microreactor</summary>

**Description:** Microreactor

**URI:** `voc4cat:0000234`

#### Slots (1)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

</details>

<details>
<summary>###### FixedBedReactor</summary>

**Description:** Fixed bed reactor

**URI:** `catcore:FixedBedReactor`

#### Slots (1)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

</details>

<details>
<summary>###### FluidizedBedReactor</summary>

**Description:** Fluidized bed reactor

**URI:** `catcore:FluidizedBedReactor`

#### Slots (4)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>gas_distributor_type</strong></summary>

**Description:** Type of gas distributor

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:gas_distributor_type`

</details>

<details>
<summary><strong>bed_expansion_height</strong></summary>

**Description:** Bed expansion height

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:bed_expansion_height`

**Unit:** cm

</details>

<details>
<summary><strong>bubble_size_distribution</strong></summary>

**Description:** No description available

**Range:** string

**Multivalued:** No

**URI:** `catcore:bubble_size_distribution`

</details>

</details>

</details>

<details>
<summary><strong>Reaction_reactant</strong></summary>

**Description:** Reactant used in the reaction

**Range:** string

**Multivalued:** Yes

**URI:** `voc4cat:0000101`

</details>

<details>
<summary><strong>Reaction_operation_parameters</strong></summary>

**Description:** Operation parameters for the reaction

**Range:** OperationParameters

**Multivalued:** Yes

**URI:** `voc4cat:0000142`

**Range Class Details:**

<details>
<summary>##### OperationParameters</summary>

**Description:** Operation parameters for the reaction

**URI:** `catcore:OperationParameters`

#### Slots (6)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>reactor_temperature_range</strong></summary>

**Description:** Temperature range in reactor

**Range:** string

**Multivalued:** Yes

**URI:** `voc4cat:0007032`

</details>

<details>
<summary><strong>atmosphere</strong></summary>

**Description:** Atmospheric conditions

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:atmosphere`

</details>

<details>
<summary><strong>experiment_pressure</strong></summary>

**Description:** Pressure during experiment

**Range:** float

**Multivalued:** Yes

**URI:** `voc4cat:0000118`

**Unit:** bar

</details>

<details>
<summary><strong>feed_composition_range</strong></summary>

**Description:** Range of feed composition

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:feed_composition_range`

</details>

<details>
<summary><strong>experiment_duration</strong></summary>

**Description:** Duration of the experiment

**Range:** float

**Multivalued:** Yes

**URI:** `AFR:0002455`

**Unit:** h

</details>

</details>

</details>

<details>
<summary><strong>Reaction_product_identification_method</strong></summary>

**Description:** Method used for product identification

**Range:** ProductIdentificationMethod

**Multivalued:** Yes

**URI:** `voc4cat:0000129`

**Range Class Details:**

<details>
<summary>##### ProductIdentificationMethod</summary>

**Abstract Class**

**Description:** Method used for product identification

**URI:** `catcore:ProductIdentificationMethod`

#### Slots (1)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

</details>

</details>

<details>
<summary><strong>Reaction_catalyst_type</strong></summary>

**Description:** Type of catalyst

**Range:** string

**Multivalued:** Yes

**URI:** `voc4cat:0007014`

</details>

#### Slot Usage

- **catalyst_quantity**: Required
- **reactor_design_type**: Required
- **reactant**: Required
- **operation_parameters**: Required
- **product_identification_method**: Required
- **catalyst_type**: Recommended

</details>

