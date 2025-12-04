# Synthesis

The data class 'Synthesis' describes the minimum information which should be reported 
with research data concerning the field of catalyst synthesis.

**Schema Reference:** [Synthesis](https://w3id.org/nfdi4cat/catcore/elements/Synthesis)

## Slots

<details markdown="1">
<summary><strong>nominal composition (Required)</strong></summary>

**Description:** Nominal composition of the catalyst

**Range:** string

**URI:** [`catcore:nominal_composition`](https://w3id.org/nfdi4cat/catcore/nominal_composition)

**Schema Reference:** [nominal_composition](./elements/nominal_composition.md)

</details>

<details markdown="1">
<summary><strong>catalyst measured properties (Required)</strong></summary>

**Description:** Measured properties of the catalyst (e.g., BET, sieve fraction, molar ratio)

**Range:** string

**URI:** [`catcore:catalyst_measured_properties`](https://w3id.org/nfdi4cat/catcore/catalyst_measured_properties)

**Schema Reference:** [catalyst_measured_properties](./elements/catalyst_measured_properties.md)

</details>

<details markdown="1">
<summary><strong>precursor (Required, Multivalued)</strong></summary>

**Description:** Precursor material used in synthesis

**Range:** Precursor

**URI:** [`catcore:precursor`](https://w3id.org/nfdi4cat/catcore/precursor)

**Schema Reference:** [precursor](./elements/precursor.md)

**Range Class Details:**

<details markdown="1">
<summary><strong>Precursor</strong></summary>

**Description:** Precursor material used in catalyst synthesis

**Schema Reference:** [Precursor](./elements/Precursor.md)

**Slots**

<details markdown="1">
<summary><strong>precursor quantity (Required, Multivalued)</strong></summary>

**Description:** Quantity of precursor used

**Range:** float

**URI:** [`catcore:precursor_quantity`](https://w3id.org/nfdi4cat/catcore/precursor_quantity)

**Schema Reference:** [precursor_quantity](./elements/precursor_quantity.md)

**Unit:** g

</details>

</details>

</details>

<details markdown="1">
<summary><strong>preparation method (Required, Multivalued)</strong></summary>

**Description:** Method used for catalyst preparation

**Range:** PreparationMethod

**URI:** [`voc4cat:0007016`](https://w3id.org/nfdi4cat/voc4cat_0007016)

**Schema Reference:** [preparation_method](./elements/preparation_method.md)

**Range Class Details:**

<details markdown="1">
<summary><strong>PreparationMethod</strong></summary>

**Abstract Class**

**Description:** Method used for catalyst preparation

**Schema Reference:** [PreparationMethod](./elements/PreparationMethod.md)

</details>

**Subclasses of PreparationMethod:**

<details markdown="1">
<summary><strong>Impregnation</strong></summary>

**Description:** Impregnation method for catalyst preparation

**URI:** [`catcore:Impregnation`](https://w3id.org/nfdi4cat/catcore/Impregnation)

**Schema Reference:** [Impregnation](./elements/Impregnation.md)

**Slots**

<details markdown="1">
<summary><strong>impregnation type (Optional, Multivalued)</strong></summary>

**Description:** Type of impregnation method

**Range:** ImpregnationTypeEnum

**URI:** [`catcore:impregnation_type`](https://w3id.org/nfdi4cat/catcore/impregnation_type)

**Schema Reference:** [impregnation_type](./elements/impregnation_type.md)

</details>

<details markdown="1">
<summary><strong>impregnation duration (Optional, Multivalued)</strong></summary>

**Description:** Duration of impregnation process

**Range:** float

**URI:** [`catcore:impregnation_duration`](https://w3id.org/nfdi4cat/catcore/impregnation_duration)

**Schema Reference:** [impregnation_duration](./elements/impregnation_duration.md)

**Unit:** h

</details>

<details markdown="1">
<summary><strong>impregnation temperature (Optional, Multivalued)</strong></summary>

**Description:** Temperature during impregnation

**Range:** float

**URI:** [`catcore:impregnation_temperature`](https://w3id.org/nfdi4cat/catcore/impregnation_temperature)

**Schema Reference:** [impregnation_temperature](./elements/impregnation_temperature.md)

**Unit:** Cel

</details>

<details markdown="1">
<summary><strong>drying device (Optional, Multivalued)</strong></summary>

**Description:** Device used for drying

**Range:** string

**URI:** [`catcore:drying_device`](https://w3id.org/nfdi4cat/catcore/drying_device)

**Schema Reference:** [drying_device](./elements/drying_device.md)

</details>

<details markdown="1">
<summary><strong>drying temperature (Optional, Multivalued)</strong></summary>

**Description:** Temperature during drying

**Range:** float

**URI:** [`catcore:drying_temperature`](https://w3id.org/nfdi4cat/catcore/drying_temperature)

**Schema Reference:** [drying_temperature](./elements/drying_temperature.md)

**Unit:** Cel

</details>

<details markdown="1">
<summary><strong>drying time (Optional, Multivalued)</strong></summary>

**Description:** Duration of drying process

**Range:** float

**URI:** [`catcore:drying_time`](https://w3id.org/nfdi4cat/catcore/drying_time)

**Schema Reference:** [drying_time](./elements/drying_time.md)

**Unit:** h

</details>

<details markdown="1">
<summary><strong>drying atmosphere (Optional, Multivalued)</strong></summary>

**Description:** Atmosphere during drying

**Range:** string

**URI:** [`catcore:drying_atmosphere`](https://w3id.org/nfdi4cat/catcore/drying_atmosphere)

**Schema Reference:** [drying_atmosphere](./elements/drying_atmosphere.md)

</details>

<details markdown="1">
<summary><strong>calcination initial temperature (Optional, Multivalued)</strong></summary>

**Description:** Initial temperature for calcination

**Range:** float

**URI:** [`voc4cat:0000057`](https://w3id.org/nfdi4cat/voc4cat_0000057)

**Schema Reference:** [calcination_initial_temperature](./elements/calcination_initial_temperature.md)

**Unit:** Cel

</details>

<details markdown="1">
<summary><strong>calcination final temperature (Optional, Multivalued)</strong></summary>

**Description:** Final temperature for calcination

**Range:** float

**URI:** [`voc4cat:0000058`](https://w3id.org/nfdi4cat/voc4cat_0000058)

**Schema Reference:** [calcination_final_temperature](./elements/calcination_final_temperature.md)

**Unit:** Cel

</details>

<details markdown="1">
<summary><strong>calcination dwelling time (Optional, Multivalued)</strong></summary>

**Description:** Dwelling time at calcination temperature

**Range:** float

**URI:** [`voc4cat:0000060`](https://w3id.org/nfdi4cat/voc4cat_0000060)

**Schema Reference:** [calcination_dwelling_time](./elements/calcination_dwelling_time.md)

**Unit:** h

</details>

<details markdown="1">
<summary><strong>number of cycles (Optional, Multivalued)</strong></summary>

**Description:** Number of cycles in the process

**Range:** integer

**URI:** [`catcore:number_of_cycles`](https://w3id.org/nfdi4cat/catcore/number_of_cycles)

**Schema Reference:** [number_of_cycles](./elements/number_of_cycles.md)

</details>

<details markdown="1">
<summary><strong>calcination gaseous environment (Optional, Multivalued)</strong></summary>

**Description:** Gaseous environment during calcination

**Range:** string

**URI:** [`voc4cat:0000055`](https://w3id.org/nfdi4cat/voc4cat_0000055)

**Schema Reference:** [calcination_gaseous_environment](./elements/calcination_gaseous_environment.md)

</details>

<details markdown="1">
<summary><strong>calcination heating rate (Optional, Multivalued)</strong></summary>

**Description:** Heating rate during calcination

**Range:** float

**URI:** [`voc4cat:0000059`](https://w3id.org/nfdi4cat/voc4cat_0000059)

**Schema Reference:** [calcination_heating_rate](./elements/calcination_heating_rate.md)

**Unit:** Cel/min

</details>

<details markdown="1">
<summary><strong>calcination gas flow rate (Optional, Multivalued)</strong></summary>

**Description:** Gas flow rate during calcination

**Range:** float

**URI:** [`voc4cat:0000056`](https://w3id.org/nfdi4cat/voc4cat_0000056)

**Schema Reference:** [calcination_gas_flow_rate](./elements/calcination_gas_flow_rate.md)

**Unit:** mL/min

</details>

</details>

<details markdown="1">
<summary><strong>CoPrecipitation</strong></summary>

**Description:** Co-precipitation method for catalyst preparation

**URI:** [`catcore:CoPrecipitation`](https://w3id.org/nfdi4cat/catcore/CoPrecipitation)

**Schema Reference:** [CoPrecipitation](./elements/CoPrecipitation.md)

**Slots**

<details markdown="1">
<summary><strong>precipitating agent (Optional, Multivalued)</strong></summary>

**Description:** Agent used for precipitation

**Range:** string

**URI:** [`catcore:precipitating_agent`](https://w3id.org/nfdi4cat/catcore/precipitating_agent)

**Schema Reference:** [precipitating_agent](./elements/precipitating_agent.md)

</details>

<details markdown="1">
<summary><strong>precipitating concentration (Optional, Multivalued)</strong></summary>

**Description:** Concentration of precipitating agent

**Range:** float

**URI:** [`catcore:precipitating_concentration`](https://w3id.org/nfdi4cat/catcore/precipitating_concentration)

**Schema Reference:** [precipitating_concentration](./elements/precipitating_concentration.md)

**Unit:** mol/L

</details>

<details markdown="1">
<summary><strong>synthesis ph (Optional, Multivalued)</strong></summary>

**Description:** pH during synthesis

**Range:** float

**URI:** [`voc4cat:0000052`](https://w3id.org/nfdi4cat/voc4cat_0000052)

**Schema Reference:** [synthesis_ph](./elements/synthesis_ph.md)

</details>

<details markdown="1">
<summary><strong>mixing rate (Optional, Multivalued)</strong></summary>

**Description:** Rate of mixing

**Range:** float

**URI:** [`catcore:mixing_rate`](https://w3id.org/nfdi4cat/catcore/mixing_rate)

**Schema Reference:** [mixing_rate](./elements/mixing_rate.md)

**Unit:** rpm

</details>

<details markdown="1">
<summary><strong>mixing time (Optional, Multivalued)</strong></summary>

**Description:** Duration of mixing

**Range:** float

**URI:** [`catcore:mixing_time`](https://w3id.org/nfdi4cat/catcore/mixing_time)

**Schema Reference:** [mixing_time](./elements/mixing_time.md)

**Unit:** h

</details>

<details markdown="1">
<summary><strong>mixing temperature (Optional, Multivalued)</strong></summary>

**Description:** Temperature during mixing

**Range:** float

**URI:** [`catcore:mixing_temperature`](https://w3id.org/nfdi4cat/catcore/mixing_temperature)

**Schema Reference:** [mixing_temperature](./elements/mixing_temperature.md)

**Unit:** Cel

</details>

<details markdown="1">
<summary><strong>drying device (Optional, Multivalued)</strong></summary>

**Description:** Device used for drying

**Range:** string

**URI:** [`catcore:drying_device`](https://w3id.org/nfdi4cat/catcore/drying_device)

**Schema Reference:** [drying_device](./elements/drying_device.md)

</details>

<details markdown="1">
<summary><strong>drying temperature (Optional, Multivalued)</strong></summary>

**Description:** Temperature during drying

**Range:** float

**URI:** [`catcore:drying_temperature`](https://w3id.org/nfdi4cat/catcore/drying_temperature)

**Schema Reference:** [drying_temperature](./elements/drying_temperature.md)

**Unit:** Cel

</details>

<details markdown="1">
<summary><strong>drying time (Optional, Multivalued)</strong></summary>

**Description:** Duration of drying process

**Range:** float

**URI:** [`catcore:drying_time`](https://w3id.org/nfdi4cat/catcore/drying_time)

**Schema Reference:** [drying_time](./elements/drying_time.md)

**Unit:** h

</details>

<details markdown="1">
<summary><strong>drying atmosphere (Optional, Multivalued)</strong></summary>

**Description:** Atmosphere during drying

**Range:** string

**URI:** [`catcore:drying_atmosphere`](https://w3id.org/nfdi4cat/catcore/drying_atmosphere)

**Schema Reference:** [drying_atmosphere](./elements/drying_atmosphere.md)

</details>

<details markdown="1">
<summary><strong>calcination initial temperature (Optional, Multivalued)</strong></summary>

**Description:** Initial temperature for calcination

**Range:** float

**URI:** [`voc4cat:0000057`](https://w3id.org/nfdi4cat/voc4cat_0000057)

**Schema Reference:** [calcination_initial_temperature](./elements/calcination_initial_temperature.md)

**Unit:** Cel

</details>

<details markdown="1">
<summary><strong>calcination final temperature (Optional, Multivalued)</strong></summary>

**Description:** Final temperature for calcination

**Range:** float

**URI:** [`voc4cat:0000058`](https://w3id.org/nfdi4cat/voc4cat_0000058)

**Schema Reference:** [calcination_final_temperature](./elements/calcination_final_temperature.md)

**Unit:** Cel

</details>

<details markdown="1">
<summary><strong>calcination dwelling time (Optional, Multivalued)</strong></summary>

**Description:** Dwelling time at calcination temperature

**Range:** float

**URI:** [`voc4cat:0000060`](https://w3id.org/nfdi4cat/voc4cat_0000060)

**Schema Reference:** [calcination_dwelling_time](./elements/calcination_dwelling_time.md)

**Unit:** h

</details>

<details markdown="1">
<summary><strong>number of cycles (Optional, Multivalued)</strong></summary>

**Description:** Number of cycles in the process

**Range:** integer

**URI:** [`catcore:number_of_cycles`](https://w3id.org/nfdi4cat/catcore/number_of_cycles)

**Schema Reference:** [number_of_cycles](./elements/number_of_cycles.md)

</details>

<details markdown="1">
<summary><strong>calcination gaseous environment (Optional, Multivalued)</strong></summary>

**Description:** Gaseous environment during calcination

**Range:** string

**URI:** [`voc4cat:0000055`](https://w3id.org/nfdi4cat/voc4cat_0000055)

**Schema Reference:** [calcination_gaseous_environment](./elements/calcination_gaseous_environment.md)

</details>

<details markdown="1">
<summary><strong>calcination heating rate (Optional, Multivalued)</strong></summary>

**Description:** Heating rate during calcination

**Range:** float

**URI:** [`voc4cat:0000059`](https://w3id.org/nfdi4cat/voc4cat_0000059)

**Schema Reference:** [calcination_heating_rate](./elements/calcination_heating_rate.md)

**Unit:** Cel/min

</details>

<details markdown="1">
<summary><strong>calcination gas flow rate (Optional, Multivalued)</strong></summary>

**Description:** Gas flow rate during calcination

**Range:** float

**URI:** [`voc4cat:0000056`](https://w3id.org/nfdi4cat/voc4cat_0000056)

**Schema Reference:** [calcination_gas_flow_rate](./elements/calcination_gas_flow_rate.md)

**Unit:** mL/min

</details>

<details markdown="1">
<summary><strong>order of addition (Optional, Multivalued)</strong></summary>

**Description:** Order in which components are added

**Range:** string

**URI:** [`catcore:order_of_addition`](https://w3id.org/nfdi4cat/catcore/order_of_addition)

**Schema Reference:** [order_of_addition](./elements/order_of_addition.md)

</details>

<details markdown="1">
<summary><strong>filtration (Optional, Multivalued)</strong></summary>

**Description:** Filtration method used

**Range:** string

**URI:** [`catcore:filtration`](https://w3id.org/nfdi4cat/catcore/filtration)

**Schema Reference:** [filtration](./elements/filtration.md)

</details>

<details markdown="1">
<summary><strong>purification (Optional, Multivalued)</strong></summary>

**Description:** Purification method used

**Range:** string

**URI:** [`catcore:purification`](https://w3id.org/nfdi4cat/catcore/purification)

**Schema Reference:** [purification](./elements/purification.md)

</details>

<details markdown="1">
<summary><strong>aging temperature (Optional, Multivalued)</strong></summary>

**Description:** Temperature during aging

**Range:** float

**URI:** [`catcore:aging_temperature`](https://w3id.org/nfdi4cat/catcore/aging_temperature)

**Schema Reference:** [aging_temperature](./elements/aging_temperature.md)

**Unit:** Cel

</details>

<details markdown="1">
<summary><strong>aging time (Optional, Multivalued)</strong></summary>

**Description:** Duration of aging process

**Range:** float

**URI:** [`catcore:aging_time`](https://w3id.org/nfdi4cat/catcore/aging_time)

**Schema Reference:** [aging_time](./elements/aging_time.md)

**Unit:** h

</details>

</details>

<details markdown="1">
<summary><strong>SolGel</strong></summary>

**Description:** Sol-gel method for catalyst preparation

**URI:** [`catcore:SolGel`](https://w3id.org/nfdi4cat/catcore/SolGel)

**Schema Reference:** [SolGel](./elements/SolGel.md)

**Slots**

<details markdown="1">
<summary><strong>hydrolysis ratio (Optional, Multivalued)</strong></summary>

**Description:** Ratio for hydrolysis

**Range:** float

**URI:** [`catcore:hydrolysis_ratio`](https://w3id.org/nfdi4cat/catcore/hydrolysis_ratio)

**Schema Reference:** [hydrolysis_ratio](./elements/hydrolysis_ratio.md)

</details>

<details markdown="1">
<summary><strong>aging time (Optional, Multivalued)</strong></summary>

**Description:** Duration of aging process

**Range:** float

**URI:** [`catcore:aging_time`](https://w3id.org/nfdi4cat/catcore/aging_time)

**Schema Reference:** [aging_time](./elements/aging_time.md)

**Unit:** h

</details>

<details markdown="1">
<summary><strong>drying (Optional, Multivalued)</strong></summary>

**Description:** Drying process description

**Range:** string

**URI:** [`catcore:drying`](https://w3id.org/nfdi4cat/catcore/drying)

**Schema Reference:** [drying](./elements/drying.md)

</details>

<details markdown="1">
<summary><strong>surfactant template (Optional, Multivalued)</strong></summary>

**Description:** Surfactant template used

**Range:** string

**URI:** [`catcore:surfactant_template`](https://w3id.org/nfdi4cat/catcore/surfactant_template)

**Schema Reference:** [surfactant_template](./elements/surfactant_template.md)

</details>

</details>

<details markdown="1">
<summary><strong>Solvothermal</strong></summary>

**Description:** Solvothermal method for catalyst preparation

**URI:** [`catcore:Solvothermal`](https://w3id.org/nfdi4cat/catcore/Solvothermal)

**Schema Reference:** [Solvothermal](./elements/Solvothermal.md)

**Slots**

<details markdown="1">
<summary><strong>filling volume (Optional, Multivalued)</strong></summary>

**Description:** Filling volume of vessel

**Range:** float

**URI:** [`catcore:filling_volume`](https://w3id.org/nfdi4cat/catcore/filling_volume)

**Schema Reference:** [filling_volume](./elements/filling_volume.md)

**Unit:** mL

</details>

<details markdown="1">
<summary><strong>synthesis temperature (Optional, Multivalued)</strong></summary>

**Description:** Temperature during synthesis

**Range:** float

**URI:** [`voc4cat:0000051`](https://w3id.org/nfdi4cat/voc4cat_0000051)

**Schema Reference:** [synthesis_temperature](./elements/synthesis_temperature.md)

**Unit:** Cel

</details>

<details markdown="1">
<summary><strong>synthesis duration (Optional, Multivalued)</strong></summary>

**Description:** Duration of synthesis

**Range:** float

**URI:** [`voc4cat:0000050`](https://w3id.org/nfdi4cat/voc4cat_0000050)

**Schema Reference:** [synthesis_duration](./elements/synthesis_duration.md)

**Unit:** h

</details>

<details markdown="1">
<summary><strong>vessel type (Optional, Multivalued)</strong></summary>

**Description:** Type of vessel used

**Range:** string

**URI:** [`catcore:vessel_type`](https://w3id.org/nfdi4cat/catcore/vessel_type)

**Schema Reference:** [vessel_type](./elements/vessel_type.md)

</details>

<details markdown="1">
<summary><strong>equipment (Optional, Multivalued)</strong></summary>

**Description:** Equipment used

**Range:** string

**URI:** [`voc4cat:0000187`](https://w3id.org/nfdi4cat/voc4cat_0000187)

**Schema Reference:** [equipment](./elements/equipment.md)

</details>

<details markdown="1">
<summary><strong>stirring speed (Optional, Multivalued)</strong></summary>

**Description:** Speed of stirring

**Range:** float

**URI:** [`catcore:stirring_speed`](https://w3id.org/nfdi4cat/catcore/stirring_speed)

**Schema Reference:** [stirring_speed](./elements/stirring_speed.md)

**Unit:** rpm

</details>

<details markdown="1">
<summary><strong>stirrer type (Optional, Multivalued)</strong></summary>

**Description:** Type of stirrer used

**Range:** string

**URI:** [`catcore:stirrer_type`](https://w3id.org/nfdi4cat/catcore/stirrer_type)

**Schema Reference:** [stirrer_type](./elements/stirrer_type.md)

</details>

<details markdown="1">
<summary><strong>cooling rate (Optional, Multivalued)</strong></summary>

**Description:** Rate of cooling

**Range:** float

**URI:** [`catcore:cooling_rate`](https://w3id.org/nfdi4cat/catcore/cooling_rate)

**Schema Reference:** [cooling_rate](./elements/cooling_rate.md)

**Unit:** Cel/min

</details>

</details>

<details markdown="1">
<summary><strong>PlasmaAssisted</strong></summary>

**Description:** Plasma-assisted method for catalyst preparation

**URI:** [`catcore:PlasmaAssisted`](https://w3id.org/nfdi4cat/catcore/PlasmaAssisted)

**Schema Reference:** [PlasmaAssisted](./elements/PlasmaAssisted.md)

**Slots**

<details markdown="1">
<summary><strong>plasma type (Optional, Multivalued)</strong></summary>

**Description:** Type of plasma used

**Range:** string

**URI:** [`catcore:plasma_type`](https://w3id.org/nfdi4cat/catcore/plasma_type)

**Schema Reference:** [plasma_type](./elements/plasma_type.md)

</details>

<details markdown="1">
<summary><strong>equipment (Optional, Multivalued)</strong></summary>

**Description:** Equipment used

**Range:** string

**URI:** [`voc4cat:0000187`](https://w3id.org/nfdi4cat/voc4cat_0000187)

**Schema Reference:** [equipment](./elements/equipment.md)

</details>

<details markdown="1">
<summary><strong>atmosphere (Optional, Multivalued)</strong></summary>

**Description:** Atmospheric conditions

**Range:** string

**URI:** [`catcore:atmosphere`](https://w3id.org/nfdi4cat/catcore/atmosphere)

**Schema Reference:** [atmosphere](./elements/atmosphere.md)

</details>

<details markdown="1">
<summary><strong>power input (Optional, Multivalued)</strong></summary>

**Description:** Power input for the process

**Range:** float

**URI:** [`catcore:power_input`](https://w3id.org/nfdi4cat/catcore/power_input)

**Schema Reference:** [power_input](./elements/power_input.md)

**Unit:** W

</details>

<details markdown="1">
<summary><strong>exposure time (Optional, Multivalued)</strong></summary>

**Description:** Time of exposure

**Range:** float

**URI:** [`catcore:exposure_time`](https://w3id.org/nfdi4cat/catcore/exposure_time)

**Schema Reference:** [exposure_time](./elements/exposure_time.md)

**Unit:** min

</details>

<details markdown="1">
<summary><strong>synthesis pressure (Optional, Multivalued)</strong></summary>

**Description:** Pressure during synthesis

**Range:** float

**URI:** [`voc4cat:0000053`](https://w3id.org/nfdi4cat/voc4cat_0000053)

**Schema Reference:** [synthesis_pressure](./elements/synthesis_pressure.md)

**Unit:** bar

</details>

<details markdown="1">
<summary><strong>synthesis temperature (Optional, Multivalued)</strong></summary>

**Description:** Temperature during synthesis

**Range:** float

**URI:** [`voc4cat:0000051`](https://w3id.org/nfdi4cat/voc4cat_0000051)

**Schema Reference:** [synthesis_temperature](./elements/synthesis_temperature.md)

**Unit:** Cel

</details>

</details>

<details markdown="1">
<summary><strong>CombustionSynthesis</strong></summary>

**Description:** Combustion synthesis method for catalyst preparation

**URI:** [`catcore:CombustionSynthesis`](https://w3id.org/nfdi4cat/catcore/CombustionSynthesis)

**Schema Reference:** [CombustionSynthesis](./elements/CombustionSynthesis.md)

**Slots**

<details markdown="1">
<summary><strong>fuel (Optional, Multivalued)</strong></summary>

**Description:** Fuel used in combustion

**Range:** string

**URI:** [`catcore:fuel`](https://w3id.org/nfdi4cat/catcore/fuel)

**Schema Reference:** [fuel](./elements/fuel.md)

</details>

<details markdown="1">
<summary><strong>oxidizer (Optional, Multivalued)</strong></summary>

**Description:** Oxidizer used

**Range:** string

**URI:** [`catcore:oxidizer`](https://w3id.org/nfdi4cat/catcore/oxidizer)

**Schema Reference:** [oxidizer](./elements/oxidizer.md)

</details>

<details markdown="1">
<summary><strong>fuel to oxidizer ratio (Optional, Multivalued)</strong></summary>

**Description:** Ratio of fuel to oxidizer

**Range:** float

**URI:** [`catcore:fuel_to_oxidizer_ratio`](https://w3id.org/nfdi4cat/catcore/fuel_to_oxidizer_ratio)

**Schema Reference:** [fuel_to_oxidizer_ratio](./elements/fuel_to_oxidizer_ratio.md)

</details>

<details markdown="1">
<summary><strong>set temperature (Optional, Multivalued)</strong></summary>

**Description:** Set temperature for the process

**Range:** float

**URI:** [`catcore:set_temperature`](https://w3id.org/nfdi4cat/catcore/set_temperature)

**Schema Reference:** [set_temperature](./elements/set_temperature.md)

**Unit:** Cel

</details>

<details markdown="1">
<summary><strong>post treatment (Optional, Multivalued)</strong></summary>

**Description:** Post-treatment process

**Range:** string

**URI:** [`catcore:post_treatment`](https://w3id.org/nfdi4cat/catcore/post_treatment)

**Schema Reference:** [post_treatment](./elements/post_treatment.md)

</details>

<details markdown="1">
<summary><strong>atmosphere (Optional, Multivalued)</strong></summary>

**Description:** Atmospheric conditions

**Range:** string

**URI:** [`catcore:atmosphere`](https://w3id.org/nfdi4cat/catcore/atmosphere)

**Schema Reference:** [atmosphere](./elements/atmosphere.md)

</details>

<details markdown="1">
<summary><strong>vessel type (Optional, Multivalued)</strong></summary>

**Description:** Type of vessel used

**Range:** string

**URI:** [`catcore:vessel_type`](https://w3id.org/nfdi4cat/catcore/vessel_type)

**Schema Reference:** [vessel_type](./elements/vessel_type.md)

</details>

<details markdown="1">
<summary><strong>equipment (Optional, Multivalued)</strong></summary>

**Description:** Equipment used

**Range:** string

**URI:** [`voc4cat:0000187`](https://w3id.org/nfdi4cat/voc4cat_0000187)

**Schema Reference:** [equipment](./elements/equipment.md)

</details>

</details>

<details markdown="1">
<summary><strong>AtomicLayerDeposition</strong></summary>

**Description:** Atomic layer deposition method for catalyst preparation

**URI:** [`catcore:AtomicLayerDeposition`](https://w3id.org/nfdi4cat/catcore/AtomicLayerDeposition)

**Schema Reference:** [AtomicLayerDeposition](./elements/AtomicLayerDeposition.md)

**Slots**

<details markdown="1">
<summary><strong>substrate (Optional, Multivalued)</strong></summary>

**Description:** Substrate material

**Range:** string

**URI:** [`voc4cat:0000024`](https://w3id.org/nfdi4cat/voc4cat_0000024)

**Schema Reference:** [substrate](./elements/substrate.md)

</details>

<details markdown="1">
<summary><strong>pulse time (Optional, Multivalued)</strong></summary>

**Description:** Pulse time for deposition

**Range:** float

**URI:** [`catcore:pulse_time`](https://w3id.org/nfdi4cat/catcore/pulse_time)

**Schema Reference:** [pulse_time](./elements/pulse_time.md)

**Unit:** s

</details>

<details markdown="1">
<summary><strong>purging duration (Optional, Multivalued)</strong></summary>

**Description:** Duration of purging

**Range:** float

**URI:** [`voc4cat:0000112`](https://w3id.org/nfdi4cat/voc4cat_0000112)

**Schema Reference:** [purging_duration](./elements/purging_duration.md)

**Unit:** s

</details>

<details markdown="1">
<summary><strong>number of cycles (Optional, Multivalued)</strong></summary>

**Description:** Number of cycles in the process

**Range:** integer

**URI:** [`catcore:number_of_cycles`](https://w3id.org/nfdi4cat/catcore/number_of_cycles)

**Schema Reference:** [number_of_cycles](./elements/number_of_cycles.md)

</details>

<details markdown="1">
<summary><strong>deposition temperature (Optional, Multivalued)</strong></summary>

**Description:** Temperature during deposition

**Range:** float

**URI:** [`catcore:deposition_temperature`](https://w3id.org/nfdi4cat/catcore/deposition_temperature)

**Schema Reference:** [deposition_temperature](./elements/deposition_temperature.md)

**Unit:** Cel

</details>

<details markdown="1">
<summary><strong>carrier gas (Optional, Multivalued)</strong></summary>

**Description:** Carrier gas used

**Range:** string

**URI:** [`catcore:carrier_gas`](https://w3id.org/nfdi4cat/catcore/carrier_gas)

**Schema Reference:** [carrier_gas](./elements/carrier_gas.md)

</details>

</details>

<details markdown="1">
<summary><strong>DepositionPrecipitation</strong></summary>

**Description:** Deposition-precipitation method for catalyst preparation

**URI:** [`catcore:DepositionPrecipitation`](https://w3id.org/nfdi4cat/catcore/DepositionPrecipitation)

**Schema Reference:** [DepositionPrecipitation](./elements/DepositionPrecipitation.md)

**Slots**

<details markdown="1">
<summary><strong>precipitating agent (Optional, Multivalued)</strong></summary>

**Description:** Agent used for precipitation

**Range:** string

**URI:** [`catcore:precipitating_agent`](https://w3id.org/nfdi4cat/catcore/precipitating_agent)

**Schema Reference:** [precipitating_agent](./elements/precipitating_agent.md)

</details>

<details markdown="1">
<summary><strong>synthesis ph (Optional, Multivalued)</strong></summary>

**Description:** pH during synthesis

**Range:** float

**URI:** [`voc4cat:0000052`](https://w3id.org/nfdi4cat/voc4cat_0000052)

**Schema Reference:** [synthesis_ph](./elements/synthesis_ph.md)

</details>

<details markdown="1">
<summary><strong>deposition temperature (Optional, Multivalued)</strong></summary>

**Description:** Temperature during deposition

**Range:** float

**URI:** [`catcore:deposition_temperature`](https://w3id.org/nfdi4cat/catcore/deposition_temperature)

**Schema Reference:** [deposition_temperature](./elements/deposition_temperature.md)

**Unit:** Cel

</details>

<details markdown="1">
<summary><strong>deposition time (Optional, Multivalued)</strong></summary>

**Description:** Time for deposition

**Range:** float

**URI:** [`catcore:deposition_time`](https://w3id.org/nfdi4cat/catcore/deposition_time)

**Schema Reference:** [deposition_time](./elements/deposition_time.md)

**Unit:** h

</details>

<details markdown="1">
<summary><strong>mixing rate (Optional, Multivalued)</strong></summary>

**Description:** Rate of mixing

**Range:** float

**URI:** [`catcore:mixing_rate`](https://w3id.org/nfdi4cat/catcore/mixing_rate)

**Schema Reference:** [mixing_rate](./elements/mixing_rate.md)

**Unit:** rpm

</details>

<details markdown="1">
<summary><strong>mixing time (Optional, Multivalued)</strong></summary>

**Description:** Duration of mixing

**Range:** float

**URI:** [`catcore:mixing_time`](https://w3id.org/nfdi4cat/catcore/mixing_time)

**Schema Reference:** [mixing_time](./elements/mixing_time.md)

**Unit:** h

</details>

<details markdown="1">
<summary><strong>mixing temperature (Optional, Multivalued)</strong></summary>

**Description:** Temperature during mixing

**Range:** float

**URI:** [`catcore:mixing_temperature`](https://w3id.org/nfdi4cat/catcore/mixing_temperature)

**Schema Reference:** [mixing_temperature](./elements/mixing_temperature.md)

**Unit:** Cel

</details>

<details markdown="1">
<summary><strong>drying device (Optional, Multivalued)</strong></summary>

**Description:** Device used for drying

**Range:** string

**URI:** [`catcore:drying_device`](https://w3id.org/nfdi4cat/catcore/drying_device)

**Schema Reference:** [drying_device](./elements/drying_device.md)

</details>

<details markdown="1">
<summary><strong>drying temperature (Optional, Multivalued)</strong></summary>

**Description:** Temperature during drying

**Range:** float

**URI:** [`catcore:drying_temperature`](https://w3id.org/nfdi4cat/catcore/drying_temperature)

**Schema Reference:** [drying_temperature](./elements/drying_temperature.md)

**Unit:** Cel

</details>

<details markdown="1">
<summary><strong>drying time (Optional, Multivalued)</strong></summary>

**Description:** Duration of drying process

**Range:** float

**URI:** [`catcore:drying_time`](https://w3id.org/nfdi4cat/catcore/drying_time)

**Schema Reference:** [drying_time](./elements/drying_time.md)

**Unit:** h

</details>

<details markdown="1">
<summary><strong>drying atmosphere (Optional, Multivalued)</strong></summary>

**Description:** Atmosphere during drying

**Range:** string

**URI:** [`catcore:drying_atmosphere`](https://w3id.org/nfdi4cat/catcore/drying_atmosphere)

**Schema Reference:** [drying_atmosphere](./elements/drying_atmosphere.md)

</details>

<details markdown="1">
<summary><strong>calcination initial temperature (Optional, Multivalued)</strong></summary>

**Description:** Initial temperature for calcination

**Range:** float

**URI:** [`voc4cat:0000057`](https://w3id.org/nfdi4cat/voc4cat_0000057)

**Schema Reference:** [calcination_initial_temperature](./elements/calcination_initial_temperature.md)

**Unit:** Cel

</details>

<details markdown="1">
<summary><strong>calcination final temperature (Optional, Multivalued)</strong></summary>

**Description:** Final temperature for calcination

**Range:** float

**URI:** [`voc4cat:0000058`](https://w3id.org/nfdi4cat/voc4cat_0000058)

**Schema Reference:** [calcination_final_temperature](./elements/calcination_final_temperature.md)

**Unit:** Cel

</details>

<details markdown="1">
<summary><strong>calcination dwelling time (Optional, Multivalued)</strong></summary>

**Description:** Dwelling time at calcination temperature

**Range:** float

**URI:** [`voc4cat:0000060`](https://w3id.org/nfdi4cat/voc4cat_0000060)

**Schema Reference:** [calcination_dwelling_time](./elements/calcination_dwelling_time.md)

**Unit:** h

</details>

<details markdown="1">
<summary><strong>number of cycles (Optional, Multivalued)</strong></summary>

**Description:** Number of cycles in the process

**Range:** integer

**URI:** [`catcore:number_of_cycles`](https://w3id.org/nfdi4cat/catcore/number_of_cycles)

**Schema Reference:** [number_of_cycles](./elements/number_of_cycles.md)

</details>

<details markdown="1">
<summary><strong>calcination gaseous environment (Optional, Multivalued)</strong></summary>

**Description:** Gaseous environment during calcination

**Range:** string

**URI:** [`voc4cat:0000055`](https://w3id.org/nfdi4cat/voc4cat_0000055)

**Schema Reference:** [calcination_gaseous_environment](./elements/calcination_gaseous_environment.md)

</details>

<details markdown="1">
<summary><strong>calcination heating rate (Optional, Multivalued)</strong></summary>

**Description:** Heating rate during calcination

**Range:** float

**URI:** [`voc4cat:0000059`](https://w3id.org/nfdi4cat/voc4cat_0000059)

**Schema Reference:** [calcination_heating_rate](./elements/calcination_heating_rate.md)

**Unit:** Cel/min

</details>

<details markdown="1">
<summary><strong>calcination gas flow rate (Optional, Multivalued)</strong></summary>

**Description:** Gas flow rate during calcination

**Range:** float

**URI:** [`voc4cat:0000056`](https://w3id.org/nfdi4cat/voc4cat_0000056)

**Schema Reference:** [calcination_gas_flow_rate](./elements/calcination_gas_flow_rate.md)

**Unit:** mL/min

</details>

<details markdown="1">
<summary><strong>order of addition (Optional, Multivalued)</strong></summary>

**Description:** Order in which components are added

**Range:** string

**URI:** [`catcore:order_of_addition`](https://w3id.org/nfdi4cat/catcore/order_of_addition)

**Schema Reference:** [order_of_addition](./elements/order_of_addition.md)

</details>

<details markdown="1">
<summary><strong>filtration (Optional, Multivalued)</strong></summary>

**Description:** Filtration method used

**Range:** string

**URI:** [`catcore:filtration`](https://w3id.org/nfdi4cat/catcore/filtration)

**Schema Reference:** [filtration](./elements/filtration.md)

</details>

<details markdown="1">
<summary><strong>purification (Optional, Multivalued)</strong></summary>

**Description:** Purification method used

**Range:** string

**URI:** [`catcore:purification`](https://w3id.org/nfdi4cat/catcore/purification)

**Schema Reference:** [purification](./elements/purification.md)

</details>

<details markdown="1">
<summary><strong>aging temperature (Optional, Multivalued)</strong></summary>

**Description:** Temperature during aging

**Range:** float

**URI:** [`catcore:aging_temperature`](https://w3id.org/nfdi4cat/catcore/aging_temperature)

**Schema Reference:** [aging_temperature](./elements/aging_temperature.md)

**Unit:** Cel

</details>

<details markdown="1">
<summary><strong>aging time (Optional, Multivalued)</strong></summary>

**Description:** Duration of aging process

**Range:** float

**URI:** [`catcore:aging_time`](https://w3id.org/nfdi4cat/catcore/aging_time)

**Schema Reference:** [aging_time](./elements/aging_time.md)

**Unit:** h

</details>

</details>

<details markdown="1">
<summary><strong>MicrowaveAssisted</strong></summary>

**Description:** Microwave-assisted method for catalyst preparation

**URI:** [`catcore:MicrowaveAssisted`](https://w3id.org/nfdi4cat/catcore/MicrowaveAssisted)

**Schema Reference:** [MicrowaveAssisted](./elements/MicrowaveAssisted.md)

**Slots**

<details markdown="1">
<summary><strong>equipment (Optional, Multivalued)</strong></summary>

**Description:** Equipment used

**Range:** string

**URI:** [`voc4cat:0000187`](https://w3id.org/nfdi4cat/voc4cat_0000187)

**Schema Reference:** [equipment](./elements/equipment.md)

</details>

<details markdown="1">
<summary><strong>power (Optional, Multivalued)</strong></summary>

**Description:** Power setting

**Range:** float

**URI:** [`catcore:power`](https://w3id.org/nfdi4cat/catcore/power)

**Schema Reference:** [power](./elements/power.md)

**Unit:** W

</details>

<details markdown="1">
<summary><strong>synthesis duration (Optional, Multivalued)</strong></summary>

**Description:** Duration of synthesis

**Range:** float

**URI:** [`voc4cat:0000050`](https://w3id.org/nfdi4cat/voc4cat_0000050)

**Schema Reference:** [synthesis_duration](./elements/synthesis_duration.md)

**Unit:** h

</details>

<details markdown="1">
<summary><strong>synthesis temperature (Optional, Multivalued)</strong></summary>

**Description:** Temperature during synthesis

**Range:** float

**URI:** [`voc4cat:0000051`](https://w3id.org/nfdi4cat/voc4cat_0000051)

**Schema Reference:** [synthesis_temperature](./elements/synthesis_temperature.md)

**Unit:** Cel

</details>

<details markdown="1">
<summary><strong>microwave frequency (Optional, Multivalued)</strong></summary>

**Description:** Frequency of microwave

**Range:** float

**URI:** [`catcore:microwave_frequency`](https://w3id.org/nfdi4cat/catcore/microwave_frequency)

**Schema Reference:** [microwave_frequency](./elements/microwave_frequency.md)

**Unit:** GHz

</details>

<details markdown="1">
<summary><strong>vessel type (Optional, Multivalued)</strong></summary>

**Description:** Type of vessel used

**Range:** string

**URI:** [`catcore:vessel_type`](https://w3id.org/nfdi4cat/catcore/vessel_type)

**Schema Reference:** [vessel_type](./elements/vessel_type.md)

</details>

</details>

<details markdown="1">
<summary><strong>SonochemicalSynthesis</strong></summary>

**Description:** Sonochemical synthesis method for catalyst preparation

**URI:** [`catcore:SonochemicalSynthesis`](https://w3id.org/nfdi4cat/catcore/SonochemicalSynthesis)

**Schema Reference:** [SonochemicalSynthesis](./elements/SonochemicalSynthesis.md)

**Slots**

<details markdown="1">
<summary><strong>stirring duration (Optional, Multivalued)</strong></summary>

**Description:** Duration of stirring

**Range:** float

**URI:** [`catcore:stirring_duration`](https://w3id.org/nfdi4cat/catcore/stirring_duration)

**Schema Reference:** [stirring_duration](./elements/stirring_duration.md)

**Unit:** h

</details>

<details markdown="1">
<summary><strong>sonication power (Optional, Multivalued)</strong></summary>

**Description:** Power of sonication

**Range:** float

**URI:** [`catcore:sonication_power`](https://w3id.org/nfdi4cat/catcore/sonication_power)

**Schema Reference:** [sonication_power](./elements/sonication_power.md)

**Unit:** W

</details>

<details markdown="1">
<summary><strong>sonication duration (Optional, Multivalued)</strong></summary>

**Description:** Duration of sonication

**Range:** float

**URI:** [`catcore:sonication_duration`](https://w3id.org/nfdi4cat/catcore/sonication_duration)

**Schema Reference:** [sonication_duration](./elements/sonication_duration.md)

**Unit:** min

</details>

<details markdown="1">
<summary><strong>temperature (Optional, Multivalued)</strong></summary>

**Description:** Temperature

**Range:** float

**URI:** [`AFR:0001584`](http://purl.allotrope.org/ontologies/result#AFR_0001584)

**Schema Reference:** [temperature](./elements/temperature.md)

**Unit:** Cel

</details>

<details markdown="1">
<summary><strong>drying device (Optional, Multivalued)</strong></summary>

**Description:** Device used for drying

**Range:** string

**URI:** [`catcore:drying_device`](https://w3id.org/nfdi4cat/catcore/drying_device)

**Schema Reference:** [drying_device](./elements/drying_device.md)

</details>

<details markdown="1">
<summary><strong>drying temperature (Optional, Multivalued)</strong></summary>

**Description:** Temperature during drying

**Range:** float

**URI:** [`catcore:drying_temperature`](https://w3id.org/nfdi4cat/catcore/drying_temperature)

**Schema Reference:** [drying_temperature](./elements/drying_temperature.md)

**Unit:** Cel

</details>

<details markdown="1">
<summary><strong>drying time (Optional, Multivalued)</strong></summary>

**Description:** Duration of drying process

**Range:** float

**URI:** [`catcore:drying_time`](https://w3id.org/nfdi4cat/catcore/drying_time)

**Schema Reference:** [drying_time](./elements/drying_time.md)

**Unit:** h

</details>

<details markdown="1">
<summary><strong>drying atmosphere (Optional, Multivalued)</strong></summary>

**Description:** Atmosphere during drying

**Range:** string

**URI:** [`catcore:drying_atmosphere`](https://w3id.org/nfdi4cat/catcore/drying_atmosphere)

**Schema Reference:** [drying_atmosphere](./elements/drying_atmosphere.md)

</details>

<details markdown="1">
<summary><strong>calcination initial temperature (Optional, Multivalued)</strong></summary>

**Description:** Initial temperature for calcination

**Range:** float

**URI:** [`voc4cat:0000057`](https://w3id.org/nfdi4cat/voc4cat_0000057)

**Schema Reference:** [calcination_initial_temperature](./elements/calcination_initial_temperature.md)

**Unit:** Cel

</details>

<details markdown="1">
<summary><strong>calcination final temperature (Optional, Multivalued)</strong></summary>

**Description:** Final temperature for calcination

**Range:** float

**URI:** [`voc4cat:0000058`](https://w3id.org/nfdi4cat/voc4cat_0000058)

**Schema Reference:** [calcination_final_temperature](./elements/calcination_final_temperature.md)

**Unit:** Cel

</details>

<details markdown="1">
<summary><strong>calcination dwelling time (Optional, Multivalued)</strong></summary>

**Description:** Dwelling time at calcination temperature

**Range:** float

**URI:** [`voc4cat:0000060`](https://w3id.org/nfdi4cat/voc4cat_0000060)

**Schema Reference:** [calcination_dwelling_time](./elements/calcination_dwelling_time.md)

**Unit:** h

</details>

<details markdown="1">
<summary><strong>number of cycles (Optional, Multivalued)</strong></summary>

**Description:** Number of cycles in the process

**Range:** integer

**URI:** [`catcore:number_of_cycles`](https://w3id.org/nfdi4cat/catcore/number_of_cycles)

**Schema Reference:** [number_of_cycles](./elements/number_of_cycles.md)

</details>

<details markdown="1">
<summary><strong>calcination gaseous environment (Optional, Multivalued)</strong></summary>

**Description:** Gaseous environment during calcination

**Range:** string

**URI:** [`voc4cat:0000055`](https://w3id.org/nfdi4cat/voc4cat_0000055)

**Schema Reference:** [calcination_gaseous_environment](./elements/calcination_gaseous_environment.md)

</details>

<details markdown="1">
<summary><strong>calcination heating rate (Optional, Multivalued)</strong></summary>

**Description:** Heating rate during calcination

**Range:** float

**URI:** [`voc4cat:0000059`](https://w3id.org/nfdi4cat/voc4cat_0000059)

**Schema Reference:** [calcination_heating_rate](./elements/calcination_heating_rate.md)

**Unit:** Cel/min

</details>

<details markdown="1">
<summary><strong>calcination gas flow rate (Optional, Multivalued)</strong></summary>

**Description:** Gas flow rate during calcination

**Range:** float

**URI:** [`voc4cat:0000056`](https://w3id.org/nfdi4cat/voc4cat_0000056)

**Schema Reference:** [calcination_gas_flow_rate](./elements/calcination_gas_flow_rate.md)

**Unit:** mL/min

</details>

</details>

<details markdown="1">
<summary><strong>FlameSprayPyrolysis</strong></summary>

**Description:** Flame spray pyrolysis method for catalyst preparation

**URI:** [`voc4cat:0007031`](https://w3id.org/nfdi4cat/voc4cat_0007031)

**Schema Reference:** [FlameSprayPyrolysis](./elements/FlameSprayPyrolysis.md)

**Slots**

<details markdown="1">
<summary><strong>flame type (Optional, Multivalued)</strong></summary>

**Description:** Type of flame used

**Range:** string

**URI:** [`catcore:flame_type`](https://w3id.org/nfdi4cat/catcore/flame_type)

**Schema Reference:** [flame_type](./elements/flame_type.md)

</details>

<details markdown="1">
<summary><strong>flow rate (Optional, Multivalued)</strong></summary>

**Description:** Flow rate

**Range:** float

**URI:** [`catcore:flow_rate`](https://w3id.org/nfdi4cat/catcore/flow_rate)

**Schema Reference:** [flow_rate](./elements/flow_rate.md)

**Unit:** mL/min

</details>

<details markdown="1">
<summary><strong>inlet system (Optional, Multivalued)</strong></summary>

**Description:** Inlet system configuration

**Range:** string

**URI:** [`catcore:inlet_system`](https://w3id.org/nfdi4cat/catcore/inlet_system)

**Schema Reference:** [inlet_system](./elements/inlet_system.md)

</details>

<details markdown="1">
<summary><strong>flame ring (Optional, Multivalued)</strong></summary>

**Description:** Flame ring configuration

**Range:** string

**URI:** [`catcore:flame_ring`](https://w3id.org/nfdi4cat/catcore/flame_ring)

**Schema Reference:** [flame_ring](./elements/flame_ring.md)

</details>

<details markdown="1">
<summary><strong>dispersant (Optional, Multivalued)</strong></summary>

**Description:** Dispersant used

**Range:** string

**URI:** [`catcore:dispersant`](https://w3id.org/nfdi4cat/catcore/dispersant)

**Schema Reference:** [dispersant](./elements/dispersant.md)

</details>

<details markdown="1">
<summary><strong>capillary pressure (Optional, Multivalued)</strong></summary>

**Description:** Capillary pressure

**Range:** float

**URI:** [`catcore:capillary_pressure`](https://w3id.org/nfdi4cat/catcore/capillary_pressure)

**Schema Reference:** [capillary_pressure](./elements/capillary_pressure.md)

**Unit:** bar

</details>

<details markdown="1">
<summary><strong>fuel dispersant ratio (Optional, Multivalued)</strong></summary>

**Description:** Ratio of fuel to dispersant

**Range:** float

**URI:** [`catcore:fuel_dispersant_ratio`](https://w3id.org/nfdi4cat/catcore/fuel_dispersant_ratio)

**Schema Reference:** [fuel_dispersant_ratio](./elements/fuel_dispersant_ratio.md)

</details>

<details markdown="1">
<summary><strong>filtration device (Optional, Multivalued)</strong></summary>

**Description:** Device used for filtration

**Range:** string

**URI:** [`catcore:filtration_device`](https://w3id.org/nfdi4cat/catcore/filtration_device)

**Schema Reference:** [filtration_device](./elements/filtration_device.md)

</details>

<details markdown="1">
<summary><strong>filter type (Optional, Multivalued)</strong></summary>

**Description:** Type of filter used

**Range:** string

**URI:** [`catcore:filter_type`](https://w3id.org/nfdi4cat/catcore/filter_type)

**Schema Reference:** [filter_type](./elements/filter_type.md)

</details>

</details>

<details markdown="1">
<summary><strong>MechanochemicalSynthesis</strong></summary>

**Description:** Mechanochemical synthesis method for catalyst preparation

**URI:** [`catcore:MechanochemicalSynthesis`](https://w3id.org/nfdi4cat/catcore/MechanochemicalSynthesis)

**Schema Reference:** [MechanochemicalSynthesis](./elements/MechanochemicalSynthesis.md)

**Slots**

<details markdown="1">
<summary><strong>equipment (Optional, Multivalued)</strong></summary>

**Description:** Equipment used

**Range:** string

**URI:** [`voc4cat:0000187`](https://w3id.org/nfdi4cat/voc4cat_0000187)

**Schema Reference:** [equipment](./elements/equipment.md)

</details>

<details markdown="1">
<summary><strong>vessel volume (Optional, Multivalued)</strong></summary>

**Description:** Volume of vessel

**Range:** float

**URI:** [`catcore:vessel_volume`](https://w3id.org/nfdi4cat/catcore/vessel_volume)

**Schema Reference:** [vessel_volume](./elements/vessel_volume.md)

**Unit:** mL

</details>

<details markdown="1">
<summary><strong>size and material (Optional, Multivalued)</strong></summary>

**Description:** Size and material of components

**Range:** string

**URI:** [`catcore:size_and_material`](https://w3id.org/nfdi4cat/catcore/size_and_material)

**Schema Reference:** [size_and_material](./elements/size_and_material.md)

</details>

<details markdown="1">
<summary><strong>milling speed (Optional, Multivalued)</strong></summary>

**Description:** Speed of milling

**Range:** float

**URI:** [`catcore:milling_speed`](https://w3id.org/nfdi4cat/catcore/milling_speed)

**Schema Reference:** [milling_speed](./elements/milling_speed.md)

**Unit:** rpm

</details>

<details markdown="1">
<summary><strong>milling duration (Optional, Multivalued)</strong></summary>

**Description:** Duration of milling

**Range:** float

**URI:** [`catcore:milling_duration`](https://w3id.org/nfdi4cat/catcore/milling_duration)

**Schema Reference:** [milling_duration](./elements/milling_duration.md)

**Unit:** h

</details>

<details markdown="1">
<summary><strong>synthesis temperature (Optional, Multivalued)</strong></summary>

**Description:** Temperature during synthesis

**Range:** float

**URI:** [`voc4cat:0000051`](https://w3id.org/nfdi4cat/voc4cat_0000051)

**Schema Reference:** [synthesis_temperature](./elements/synthesis_temperature.md)

**Unit:** Cel

</details>

<details markdown="1">
<summary><strong>atmosphere (Optional, Multivalued)</strong></summary>

**Description:** Atmospheric conditions

**Range:** string

**URI:** [`catcore:atmosphere`](https://w3id.org/nfdi4cat/catcore/atmosphere)

**Schema Reference:** [atmosphere](./elements/atmosphere.md)

</details>

<details markdown="1">
<summary><strong>ball material (Optional, Multivalued)</strong></summary>

**Description:** Material of milling balls

**Range:** string

**URI:** [`catcore:ball_material`](https://w3id.org/nfdi4cat/catcore/ball_material)

**Schema Reference:** [ball_material](./elements/ball_material.md)

</details>

<details markdown="1">
<summary><strong>ball size (Optional, Multivalued)</strong></summary>

**Description:** Size of milling balls

**Range:** float

**URI:** [`catcore:ball_size`](https://w3id.org/nfdi4cat/catcore/ball_size)

**Schema Reference:** [ball_size](./elements/ball_size.md)

**Unit:** mm

</details>

<details markdown="1">
<summary><strong>ball to powder ratio (Optional, Multivalued)</strong></summary>

**Description:** Ratio of ball to powder

**Range:** float

**URI:** [`catcore:ball_to_powder_ratio`](https://w3id.org/nfdi4cat/catcore/ball_to_powder_ratio)

**Schema Reference:** [ball_to_powder_ratio](./elements/ball_to_powder_ratio.md)

</details>

</details>

<details markdown="1">
<summary><strong>Sublimation</strong></summary>

**Description:** Sublimation method for catalyst preparation

**URI:** [`catcore:Sublimation`](https://w3id.org/nfdi4cat/catcore/Sublimation)

**Schema Reference:** [Sublimation](./elements/Sublimation.md)

**Slots**

<details markdown="1">
<summary><strong>temperature (Optional, Multivalued)</strong></summary>

**Description:** Temperature

**Range:** float

**URI:** [`AFR:0001584`](http://purl.allotrope.org/ontologies/result#AFR_0001584)

**Schema Reference:** [temperature](./elements/temperature.md)

**Unit:** Cel

</details>

<details markdown="1">
<summary><strong>synthesis pressure (Optional, Multivalued)</strong></summary>

**Description:** Pressure during synthesis

**Range:** float

**URI:** [`voc4cat:0000053`](https://w3id.org/nfdi4cat/voc4cat_0000053)

**Schema Reference:** [synthesis_pressure](./elements/synthesis_pressure.md)

**Unit:** bar

</details>

<details markdown="1">
<summary><strong>synthesis duration (Optional, Multivalued)</strong></summary>

**Description:** Duration of synthesis

**Range:** float

**URI:** [`voc4cat:0000050`](https://w3id.org/nfdi4cat/voc4cat_0000050)

**Schema Reference:** [synthesis_duration](./elements/synthesis_duration.md)

**Unit:** h

</details>

</details>

<details markdown="1">
<summary><strong>MolecularSynthesis</strong></summary>

**Description:** Molecular synthesis method for catalyst preparation

**URI:** [`catcore:MolecularSynthesis`](https://w3id.org/nfdi4cat/catcore/MolecularSynthesis)

**Schema Reference:** [MolecularSynthesis](./elements/MolecularSynthesis.md)

**Slots**

<details markdown="1">
<summary><strong>atmosphere (Optional, Multivalued)</strong></summary>

**Description:** Atmospheric conditions

**Range:** string

**URI:** [`catcore:atmosphere`](https://w3id.org/nfdi4cat/catcore/atmosphere)

**Schema Reference:** [atmosphere](./elements/atmosphere.md)

</details>

<details markdown="1">
<summary><strong>synthesis duration (Optional, Multivalued)</strong></summary>

**Description:** Duration of synthesis

**Range:** float

**URI:** [`voc4cat:0000050`](https://w3id.org/nfdi4cat/voc4cat_0000050)

**Schema Reference:** [synthesis_duration](./elements/synthesis_duration.md)

**Unit:** h

</details>

<details markdown="1">
<summary><strong>reaction vessel (Optional, Multivalued)</strong></summary>

**Description:** Vessel used for reaction

**Range:** string

**URI:** [`catcore:reaction_vessel`](https://w3id.org/nfdi4cat/catcore/reaction_vessel)

**Schema Reference:** [reaction_vessel](./elements/reaction_vessel.md)

</details>

<details markdown="1">
<summary><strong>mixing device (Optional, Multivalued)</strong></summary>

**Description:** Device used for mixing

**Range:** string

**URI:** [`catcore:mixing_device`](https://w3id.org/nfdi4cat/catcore/mixing_device)

**Schema Reference:** [mixing_device](./elements/mixing_device.md)

</details>

<details markdown="1">
<summary><strong>stirring duration (Optional, Multivalued)</strong></summary>

**Description:** Duration of stirring

**Range:** float

**URI:** [`catcore:stirring_duration`](https://w3id.org/nfdi4cat/catcore/stirring_duration)

**Schema Reference:** [stirring_duration](./elements/stirring_duration.md)

**Unit:** h

</details>

<details markdown="1">
<summary><strong>stirring speed (Optional, Multivalued)</strong></summary>

**Description:** Speed of stirring

**Range:** float

**URI:** [`catcore:stirring_speed`](https://w3id.org/nfdi4cat/catcore/stirring_speed)

**Schema Reference:** [stirring_speed](./elements/stirring_speed.md)

**Unit:** rpm

</details>

<details markdown="1">
<summary><strong>mixing temperature (Optional, Multivalued)</strong></summary>

**Description:** Temperature during mixing

**Range:** float

**URI:** [`catcore:mixing_temperature`](https://w3id.org/nfdi4cat/catcore/mixing_temperature)

**Schema Reference:** [mixing_temperature](./elements/mixing_temperature.md)

**Unit:** Cel

</details>

<details markdown="1">
<summary><strong>filtration device (Optional, Multivalued)</strong></summary>

**Description:** Device used for filtration

**Range:** string

**URI:** [`catcore:filtration_device`](https://w3id.org/nfdi4cat/catcore/filtration_device)

**Schema Reference:** [filtration_device](./elements/filtration_device.md)

</details>

<details markdown="1">
<summary><strong>filter type (Optional, Multivalued)</strong></summary>

**Description:** Type of filter used

**Range:** string

**URI:** [`catcore:filter_type`](https://w3id.org/nfdi4cat/catcore/filter_type)

**Schema Reference:** [filter_type](./elements/filter_type.md)

</details>

<details markdown="1">
<summary><strong>crystallisation solvents (Optional, Multivalued)</strong></summary>

**Description:** Solvents used for crystallisation

**Range:** string

**URI:** [`catcore:crystallisation_solvents`](https://w3id.org/nfdi4cat/catcore/crystallisation_solvents)

**Schema Reference:** [crystallisation_solvents](./elements/crystallisation_solvents.md)

</details>

<details markdown="1">
<summary><strong>precipitation agent (Optional, Multivalued)</strong></summary>

**Description:** Agent used for precipitation

**Range:** string

**URI:** [`catcore:precipitation_agent`](https://w3id.org/nfdi4cat/catcore/precipitation_agent)

**Schema Reference:** [precipitation_agent](./elements/precipitation_agent.md)

</details>

<details markdown="1">
<summary><strong>crystallisation duration (Optional, Multivalued)</strong></summary>

**Description:** Duration of crystallisation

**Range:** float

**URI:** [`catcore:crystallisation_duration`](https://w3id.org/nfdi4cat/catcore/crystallisation_duration)

**Schema Reference:** [crystallisation_duration](./elements/crystallisation_duration.md)

**Unit:** h

</details>

<details markdown="1">
<summary><strong>purification solvent (Optional, Multivalued)</strong></summary>

**Description:** Solvent used for purification

**Range:** string

**URI:** [`catcore:purification_solvent`](https://w3id.org/nfdi4cat/catcore/purification_solvent)

**Schema Reference:** [purification_solvent](./elements/purification_solvent.md)

</details>

<details markdown="1">
<summary><strong>number of cycles (Optional, Multivalued)</strong></summary>

**Description:** Number of cycles in the process

**Range:** integer

**URI:** [`catcore:number_of_cycles`](https://w3id.org/nfdi4cat/catcore/number_of_cycles)

**Schema Reference:** [number_of_cycles](./elements/number_of_cycles.md)

</details>

<details markdown="1">
<summary><strong>drying device (Optional, Multivalued)</strong></summary>

**Description:** Device used for drying

**Range:** string

**URI:** [`catcore:drying_device`](https://w3id.org/nfdi4cat/catcore/drying_device)

**Schema Reference:** [drying_device](./elements/drying_device.md)

</details>

<details markdown="1">
<summary><strong>drying temperature (Optional, Multivalued)</strong></summary>

**Description:** Temperature during drying

**Range:** float

**URI:** [`catcore:drying_temperature`](https://w3id.org/nfdi4cat/catcore/drying_temperature)

**Schema Reference:** [drying_temperature](./elements/drying_temperature.md)

**Unit:** Cel

</details>

<details markdown="1">
<summary><strong>temperature ramp (Optional, Multivalued)</strong></summary>

**Description:** Temperature ramp rate

**Range:** float

**URI:** [`catcore:temperature_ramp`](https://w3id.org/nfdi4cat/catcore/temperature_ramp)

**Schema Reference:** [temperature_ramp](./elements/temperature_ramp.md)

**Unit:** Cel/min

</details>

<details markdown="1">
<summary><strong>drying time (Optional, Multivalued)</strong></summary>

**Description:** Duration of drying process

**Range:** float

**URI:** [`catcore:drying_time`](https://w3id.org/nfdi4cat/catcore/drying_time)

**Schema Reference:** [drying_time](./elements/drying_time.md)

**Unit:** h

</details>

</details>

<details markdown="1">
<summary><strong>ExsolutionSynthesis</strong></summary>

**Description:** Exsolution synthesis method for catalyst preparation

**URI:** [`catcore:ExsolutionSynthesis`](https://w3id.org/nfdi4cat/catcore/ExsolutionSynthesis)

**Schema Reference:** [ExsolutionSynthesis](./elements/ExsolutionSynthesis.md)

**Slots**

<details markdown="1">
<summary><strong>calcination initial temperature (Optional, Multivalued)</strong></summary>

**Description:** Initial temperature for calcination

**Range:** float

**URI:** [`voc4cat:0000057`](https://w3id.org/nfdi4cat/voc4cat_0000057)

**Schema Reference:** [calcination_initial_temperature](./elements/calcination_initial_temperature.md)

**Unit:** Cel

</details>

<details markdown="1">
<summary><strong>calcination final temperature (Optional, Multivalued)</strong></summary>

**Description:** Final temperature for calcination

**Range:** float

**URI:** [`voc4cat:0000058`](https://w3id.org/nfdi4cat/voc4cat_0000058)

**Schema Reference:** [calcination_final_temperature](./elements/calcination_final_temperature.md)

**Unit:** Cel

</details>

<details markdown="1">
<summary><strong>calcination dwelling time (Optional, Multivalued)</strong></summary>

**Description:** Dwelling time at calcination temperature

**Range:** float

**URI:** [`voc4cat:0000060`](https://w3id.org/nfdi4cat/voc4cat_0000060)

**Schema Reference:** [calcination_dwelling_time](./elements/calcination_dwelling_time.md)

**Unit:** h

</details>

<details markdown="1">
<summary><strong>calcination gaseous environment (Optional, Multivalued)</strong></summary>

**Description:** Gaseous environment during calcination

**Range:** string

**URI:** [`voc4cat:0000055`](https://w3id.org/nfdi4cat/voc4cat_0000055)

**Schema Reference:** [calcination_gaseous_environment](./elements/calcination_gaseous_environment.md)

</details>

<details markdown="1">
<summary><strong>calcination heating rate (Optional, Multivalued)</strong></summary>

**Description:** Heating rate during calcination

**Range:** float

**URI:** [`voc4cat:0000059`](https://w3id.org/nfdi4cat/voc4cat_0000059)

**Schema Reference:** [calcination_heating_rate](./elements/calcination_heating_rate.md)

**Unit:** Cel/min

</details>

<details markdown="1">
<summary><strong>calcination gas flow rate (Optional, Multivalued)</strong></summary>

**Description:** Gas flow rate during calcination

**Range:** float

**URI:** [`voc4cat:0000056`](https://w3id.org/nfdi4cat/voc4cat_0000056)

**Schema Reference:** [calcination_gas_flow_rate](./elements/calcination_gas_flow_rate.md)

**Unit:** mL/min

</details>

</details>

</details>

<details markdown="1">
<summary><strong>storage conditions (Recommended, Multivalued)</strong></summary>

**Description:** Conditions for storage

**Range:** string

**URI:** [`catcore:storage_conditions`](https://w3id.org/nfdi4cat/catcore/storage_conditions)

**Schema Reference:** [storage_conditions](./elements/storage_conditions.md)

</details>

<details markdown="1">
<summary><strong>support (Optional, Multivalued)</strong></summary>

**Description:** Support material

**Range:** string

**URI:** [`catcore:support`](https://w3id.org/nfdi4cat/catcore/support)

**Schema Reference:** [support](./elements/support.md)

</details>

<details markdown="1">
<summary><strong>solvent (Optional, Multivalued)</strong></summary>

**Description:** Solvent used

**Range:** string

**URI:** [`voc4cat:0007246`](https://w3id.org/nfdi4cat/voc4cat_0007246)

**Schema Reference:** [solvent](./elements/solvent.md)

</details>

<details markdown="1">
<summary><strong>sample pretreatment (Optional, Multivalued)</strong></summary>

**Description:** Pre-treatment of sample

**Range:** string

**URI:** [`voc4cat:0000122`](https://w3id.org/nfdi4cat/voc4cat_0000122)

**Schema Reference:** [sample_pretreatment](./elements/sample_pretreatment.md)

</details>

