# Synthesis

**Description:** The data class 'Synthesis' describes the minimum information which should be reported 
with research data concerning the field of catalyst synthesis.

---

## Main Class

<details>
<summary>### Synthesis</summary>

**Description:** The data class 'Synthesis' describes the minimum information which should be reported 
with research data concerning the field of catalyst synthesis.

**URI:** `catcore:Synthesis`

#### Slots (9)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>Synthesis_nominal_composition</strong></summary>

**Description:** Nominal composition of the catalyst

**Range:** string

**Multivalued:** No

**URI:** `catcore:nominal_composition`

</details>

<details>
<summary><strong>Synthesis_catalyst_measured_properties</strong></summary>

**Description:** Measured properties of the catalyst (e.g., BET, sieve fraction, molar ratio)

**Range:** string

**Multivalued:** No

**URI:** `catcore:catalyst_measured_properties`

</details>

<details>
<summary><strong>Synthesis_precursor</strong></summary>

**Description:** Precursor material used in synthesis

**Range:** Precursor

**Multivalued:** Yes

**URI:** `catcore:precursor`

**Range Class Details:**

<details>
<summary>##### Precursor</summary>

**Description:** Precursor material used in catalyst synthesis

**URI:** `catcore:Precursor`

#### Slots (2)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>Precursor_precursor_quantity</strong></summary>

**Description:** Quantity of precursor used

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:precursor_quantity`

**Unit:** g

</details>

#### Slot Usage

- **precursor_quantity**: Required

</details>

</details>

<details>
<summary><strong>Synthesis_preparation_method</strong></summary>

**Description:** Method used for catalyst preparation

**Range:** PreparationMethod

**Multivalued:** Yes

**URI:** `voc4cat:0007016`

**Range Class Details:**

<details>
<summary>##### PreparationMethod</summary>

**Abstract Class**

**Description:** Method used for catalyst preparation

**URI:** `catcore:PreparationMethod`

#### Slots (1)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

</details>

**Subclasses of PreparationMethod:**

<details>
<summary>###### Impregnation</summary>

**Description:** Impregnation method for catalyst preparation

**URI:** `catcore:Impregnation`

#### Slots (15)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>impregnation_type</strong></summary>

**Description:** Type of impregnation method

**Range:** ImpregnationTypeEnum

**Multivalued:** Yes

**URI:** `catcore:impregnation_type`

</details>

<details>
<summary><strong>impregnation_duration</strong></summary>

**Description:** Duration of impregnation process

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:impregnation_duration`

**Unit:** h

</details>

<details>
<summary><strong>impregnation_temperature</strong></summary>

**Description:** Temperature during impregnation

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:impregnation_temperature`

**Unit:** Cel

</details>

<details>
<summary><strong>drying_device</strong></summary>

**Description:** Device used for drying

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:drying_device`

</details>

<details>
<summary><strong>drying_temperature</strong></summary>

**Description:** Temperature during drying

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:drying_temperature`

**Unit:** Cel

</details>

<details>
<summary><strong>drying_time</strong></summary>

**Description:** Duration of drying process

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:drying_time`

**Unit:** h

</details>

<details>
<summary><strong>drying_atmosphere</strong></summary>

**Description:** Atmosphere during drying

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:drying_atmosphere`

</details>

<details>
<summary><strong>calcination_initial_temperature</strong></summary>

**Description:** Initial temperature for calcination

**Range:** float

**Multivalued:** Yes

**URI:** `voc4cat:0000057`

**Unit:** Cel

</details>

<details>
<summary><strong>calcination_final_temperature</strong></summary>

**Description:** Final temperature for calcination

**Range:** float

**Multivalued:** Yes

**URI:** `voc4cat:0000058`

**Unit:** Cel

</details>

<details>
<summary><strong>calcination_dwelling_time</strong></summary>

**Description:** Dwelling time at calcination temperature

**Range:** float

**Multivalued:** Yes

**URI:** `voc4cat:0000060`

**Unit:** h

</details>

<details>
<summary><strong>number_of_cycles</strong></summary>

**Description:** Number of cycles in the process

**Range:** integer

**Multivalued:** Yes

**URI:** `catcore:number_of_cycles`

</details>

<details>
<summary><strong>calcination_gaseous_environment</strong></summary>

**Description:** Gaseous environment during calcination

**Range:** string

**Multivalued:** Yes

**URI:** `voc4cat:0000055`

</details>

<details>
<summary><strong>calcination_heating_rate</strong></summary>

**Description:** Heating rate during calcination

**Range:** float

**Multivalued:** Yes

**URI:** `voc4cat:0000059`

**Unit:** Cel/min

</details>

<details>
<summary><strong>calcination_gas_flow_rate</strong></summary>

**Description:** Gas flow rate during calcination

**Range:** float

**Multivalued:** Yes

**URI:** `voc4cat:0000056`

**Unit:** mL/min

</details>

</details>

<details>
<summary>###### CoPrecipitation</summary>

**Description:** Co-precipitation method for catalyst preparation

**URI:** `catcore:CoPrecipitation`

#### Slots (23)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>precipitating_agent</strong></summary>

**Description:** Agent used for precipitation

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:precipitating_agent`

</details>

<details>
<summary><strong>precipitating_concentration</strong></summary>

**Description:** Concentration of precipitating agent

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:precipitating_concentration`

**Unit:** mol/L

</details>

<details>
<summary><strong>synthesis_ph</strong></summary>

**Description:** pH during synthesis

**Range:** float

**Multivalued:** Yes

**URI:** `voc4cat:0000052`

</details>

<details>
<summary><strong>mixing_rate</strong></summary>

**Description:** Rate of mixing

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:mixing_rate`

**Unit:** rpm

</details>

<details>
<summary><strong>mixing_time</strong></summary>

**Description:** Duration of mixing

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:mixing_time`

**Unit:** h

</details>

<details>
<summary><strong>mixing_temperature</strong></summary>

**Description:** Temperature during mixing

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:mixing_temperature`

**Unit:** Cel

</details>

<details>
<summary><strong>drying_device</strong></summary>

**Description:** Device used for drying

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:drying_device`

</details>

<details>
<summary><strong>drying_temperature</strong></summary>

**Description:** Temperature during drying

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:drying_temperature`

**Unit:** Cel

</details>

<details>
<summary><strong>drying_time</strong></summary>

**Description:** Duration of drying process

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:drying_time`

**Unit:** h

</details>

<details>
<summary><strong>drying_atmosphere</strong></summary>

**Description:** Atmosphere during drying

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:drying_atmosphere`

</details>

<details>
<summary><strong>calcination_initial_temperature</strong></summary>

**Description:** Initial temperature for calcination

**Range:** float

**Multivalued:** Yes

**URI:** `voc4cat:0000057`

**Unit:** Cel

</details>

<details>
<summary><strong>calcination_final_temperature</strong></summary>

**Description:** Final temperature for calcination

**Range:** float

**Multivalued:** Yes

**URI:** `voc4cat:0000058`

**Unit:** Cel

</details>

<details>
<summary><strong>calcination_dwelling_time</strong></summary>

**Description:** Dwelling time at calcination temperature

**Range:** float

**Multivalued:** Yes

**URI:** `voc4cat:0000060`

**Unit:** h

</details>

<details>
<summary><strong>number_of_cycles</strong></summary>

**Description:** Number of cycles in the process

**Range:** integer

**Multivalued:** Yes

**URI:** `catcore:number_of_cycles`

</details>

<details>
<summary><strong>calcination_gaseous_environment</strong></summary>

**Description:** Gaseous environment during calcination

**Range:** string

**Multivalued:** Yes

**URI:** `voc4cat:0000055`

</details>

<details>
<summary><strong>calcination_heating_rate</strong></summary>

**Description:** Heating rate during calcination

**Range:** float

**Multivalued:** Yes

**URI:** `voc4cat:0000059`

**Unit:** Cel/min

</details>

<details>
<summary><strong>calcination_gas_flow_rate</strong></summary>

**Description:** Gas flow rate during calcination

**Range:** float

**Multivalued:** Yes

**URI:** `voc4cat:0000056`

**Unit:** mL/min

</details>

<details>
<summary><strong>order_of_addition</strong></summary>

**Description:** Order in which components are added

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:order_of_addition`

</details>

<details>
<summary><strong>filtration</strong></summary>

**Description:** Filtration method used

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:filtration`

</details>

<details>
<summary><strong>purification</strong></summary>

**Description:** Purification method used

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:purification`

</details>

<details>
<summary><strong>aging_temperature</strong></summary>

**Description:** Temperature during aging

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:aging_temperature`

**Unit:** Cel

</details>

<details>
<summary><strong>aging_time</strong></summary>

**Description:** Duration of aging process

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:aging_time`

**Unit:** h

</details>

</details>

<details>
<summary>###### SolGel</summary>

**Description:** Sol-gel method for catalyst preparation

**URI:** `catcore:SolGel`

#### Slots (5)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>hydrolysis_ratio</strong></summary>

**Description:** Ratio for hydrolysis

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:hydrolysis_ratio`

</details>

<details>
<summary><strong>aging_time</strong></summary>

**Description:** Duration of aging process

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:aging_time`

**Unit:** h

</details>

<details>
<summary><strong>drying</strong></summary>

**Description:** Drying process description

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:drying`

</details>

<details>
<summary><strong>surfactant_template</strong></summary>

**Description:** Surfactant template used

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:surfactant_template`

</details>

</details>

<details>
<summary>###### Solvothermal</summary>

**Description:** Solvothermal method for catalyst preparation

**URI:** `catcore:Solvothermal`

#### Slots (9)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>filling_volume</strong></summary>

**Description:** Filling volume of vessel

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:filling_volume`

**Unit:** mL

</details>

<details>
<summary><strong>synthesis_temperature</strong></summary>

**Description:** Temperature during synthesis

**Range:** float

**Multivalued:** Yes

**URI:** `voc4cat:0000051`

**Unit:** Cel

</details>

<details>
<summary><strong>synthesis_duration</strong></summary>

**Description:** Duration of synthesis

**Range:** float

**Multivalued:** Yes

**URI:** `voc4cat:0000050`

**Unit:** h

</details>

<details>
<summary><strong>vessel_type</strong></summary>

**Description:** Type of vessel used

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:vessel_type`

</details>

<details>
<summary><strong>equipment</strong></summary>

**Description:** Equipment used

**Range:** string

**Multivalued:** Yes

**URI:** `voc4cat:0000187`

</details>

<details>
<summary><strong>stirring_speed</strong></summary>

**Description:** Speed of stirring

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:stirring_speed`

**Unit:** rpm

</details>

<details>
<summary><strong>stirrer_type</strong></summary>

**Description:** Type of stirrer used

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:stirrer_type`

</details>

<details>
<summary><strong>cooling_rate</strong></summary>

**Description:** Rate of cooling

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:cooling_rate`

**Unit:** Cel/min

</details>

</details>

<details>
<summary>###### PlasmaAssisted</summary>

**Description:** Plasma-assisted method for catalyst preparation

**URI:** `catcore:PlasmaAssisted`

#### Slots (8)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>plasma_type</strong></summary>

**Description:** Type of plasma used

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:plasma_type`

</details>

<details>
<summary><strong>equipment</strong></summary>

**Description:** Equipment used

**Range:** string

**Multivalued:** Yes

**URI:** `voc4cat:0000187`

</details>

<details>
<summary><strong>atmosphere</strong></summary>

**Description:** Atmospheric conditions

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:atmosphere`

</details>

<details>
<summary><strong>power_input</strong></summary>

**Description:** Power input for the process

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:power_input`

**Unit:** W

</details>

<details>
<summary><strong>exposure_time</strong></summary>

**Description:** Time of exposure

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:exposure_time`

**Unit:** min

</details>

<details>
<summary><strong>synthesis_pressure</strong></summary>

**Description:** Pressure during synthesis

**Range:** float

**Multivalued:** Yes

**URI:** `voc4cat:0000053`

**Unit:** bar

</details>

<details>
<summary><strong>synthesis_temperature</strong></summary>

**Description:** Temperature during synthesis

**Range:** float

**Multivalued:** Yes

**URI:** `voc4cat:0000051`

**Unit:** Cel

</details>

</details>

<details>
<summary>###### CombustionSynthesis</summary>

**Description:** Combustion synthesis method for catalyst preparation

**URI:** `catcore:CombustionSynthesis`

#### Slots (9)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>fuel</strong></summary>

**Description:** Fuel used in combustion

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:fuel`

</details>

<details>
<summary><strong>oxidizer</strong></summary>

**Description:** Oxidizer used

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:oxidizer`

</details>

<details>
<summary><strong>fuel_to_oxidizer_ratio</strong></summary>

**Description:** Ratio of fuel to oxidizer

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:fuel_to_oxidizer_ratio`

</details>

<details>
<summary><strong>set_temperature</strong></summary>

**Description:** Set temperature for the process

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:set_temperature`

**Unit:** Cel

</details>

<details>
<summary><strong>post_treatment</strong></summary>

**Description:** Post-treatment process

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:post_treatment`

</details>

<details>
<summary><strong>atmosphere</strong></summary>

**Description:** Atmospheric conditions

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:atmosphere`

</details>

<details>
<summary><strong>vessel_type</strong></summary>

**Description:** Type of vessel used

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:vessel_type`

</details>

<details>
<summary><strong>equipment</strong></summary>

**Description:** Equipment used

**Range:** string

**Multivalued:** Yes

**URI:** `voc4cat:0000187`

</details>

</details>

<details>
<summary>###### AtomicLayerDeposition</summary>

**Description:** Atomic layer deposition method for catalyst preparation

**URI:** `catcore:AtomicLayerDeposition`

#### Slots (7)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>substrate</strong></summary>

**Description:** Substrate material

**Range:** string

**Multivalued:** Yes

**URI:** `voc4cat:0000024`

</details>

<details>
<summary><strong>pulse_time</strong></summary>

**Description:** Pulse time for deposition

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:pulse_time`

**Unit:** s

</details>

<details>
<summary><strong>purging_duration</strong></summary>

**Description:** Duration of purging

**Range:** float

**Multivalued:** Yes

**URI:** `voc4cat:0000112`

**Unit:** s

</details>

<details>
<summary><strong>number_of_cycles</strong></summary>

**Description:** Number of cycles in the process

**Range:** integer

**Multivalued:** Yes

**URI:** `catcore:number_of_cycles`

</details>

<details>
<summary><strong>deposition_temperature</strong></summary>

**Description:** Temperature during deposition

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:deposition_temperature`

**Unit:** Cel

</details>

<details>
<summary><strong>carrier_gas</strong></summary>

**Description:** Carrier gas used

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:carrier_gas`

</details>

</details>

<details>
<summary>###### DepositionPrecipitation</summary>

**Description:** Deposition-precipitation method for catalyst preparation

**URI:** `catcore:DepositionPrecipitation`

#### Slots (24)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>precipitating_agent</strong></summary>

**Description:** Agent used for precipitation

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:precipitating_agent`

</details>

<details>
<summary><strong>synthesis_ph</strong></summary>

**Description:** pH during synthesis

**Range:** float

**Multivalued:** Yes

**URI:** `voc4cat:0000052`

</details>

<details>
<summary><strong>deposition_temperature</strong></summary>

**Description:** Temperature during deposition

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:deposition_temperature`

**Unit:** Cel

</details>

<details>
<summary><strong>deposition_time</strong></summary>

**Description:** Time for deposition

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:deposition_time`

**Unit:** h

</details>

<details>
<summary><strong>mixing_rate</strong></summary>

**Description:** Rate of mixing

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:mixing_rate`

**Unit:** rpm

</details>

<details>
<summary><strong>mixing_time</strong></summary>

**Description:** Duration of mixing

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:mixing_time`

**Unit:** h

</details>

<details>
<summary><strong>mixing_temperature</strong></summary>

**Description:** Temperature during mixing

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:mixing_temperature`

**Unit:** Cel

</details>

<details>
<summary><strong>drying_device</strong></summary>

**Description:** Device used for drying

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:drying_device`

</details>

<details>
<summary><strong>drying_temperature</strong></summary>

**Description:** Temperature during drying

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:drying_temperature`

**Unit:** Cel

</details>

<details>
<summary><strong>drying_time</strong></summary>

**Description:** Duration of drying process

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:drying_time`

**Unit:** h

</details>

<details>
<summary><strong>drying_atmosphere</strong></summary>

**Description:** Atmosphere during drying

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:drying_atmosphere`

</details>

<details>
<summary><strong>calcination_initial_temperature</strong></summary>

**Description:** Initial temperature for calcination

**Range:** float

**Multivalued:** Yes

**URI:** `voc4cat:0000057`

**Unit:** Cel

</details>

<details>
<summary><strong>calcination_final_temperature</strong></summary>

**Description:** Final temperature for calcination

**Range:** float

**Multivalued:** Yes

**URI:** `voc4cat:0000058`

**Unit:** Cel

</details>

<details>
<summary><strong>calcination_dwelling_time</strong></summary>

**Description:** Dwelling time at calcination temperature

**Range:** float

**Multivalued:** Yes

**URI:** `voc4cat:0000060`

**Unit:** h

</details>

<details>
<summary><strong>number_of_cycles</strong></summary>

**Description:** Number of cycles in the process

**Range:** integer

**Multivalued:** Yes

**URI:** `catcore:number_of_cycles`

</details>

<details>
<summary><strong>calcination_gaseous_environment</strong></summary>

**Description:** Gaseous environment during calcination

**Range:** string

**Multivalued:** Yes

**URI:** `voc4cat:0000055`

</details>

<details>
<summary><strong>calcination_heating_rate</strong></summary>

**Description:** Heating rate during calcination

**Range:** float

**Multivalued:** Yes

**URI:** `voc4cat:0000059`

**Unit:** Cel/min

</details>

<details>
<summary><strong>calcination_gas_flow_rate</strong></summary>

**Description:** Gas flow rate during calcination

**Range:** float

**Multivalued:** Yes

**URI:** `voc4cat:0000056`

**Unit:** mL/min

</details>

<details>
<summary><strong>order_of_addition</strong></summary>

**Description:** Order in which components are added

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:order_of_addition`

</details>

<details>
<summary><strong>filtration</strong></summary>

**Description:** Filtration method used

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:filtration`

</details>

<details>
<summary><strong>purification</strong></summary>

**Description:** Purification method used

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:purification`

</details>

<details>
<summary><strong>aging_temperature</strong></summary>

**Description:** Temperature during aging

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:aging_temperature`

**Unit:** Cel

</details>

<details>
<summary><strong>aging_time</strong></summary>

**Description:** Duration of aging process

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:aging_time`

**Unit:** h

</details>

</details>

<details>
<summary>###### MicrowaveAssisted</summary>

**Description:** Microwave-assisted method for catalyst preparation

**URI:** `catcore:MicrowaveAssisted`

#### Slots (7)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>equipment</strong></summary>

**Description:** Equipment used

**Range:** string

**Multivalued:** Yes

**URI:** `voc4cat:0000187`

</details>

<details>
<summary><strong>power</strong></summary>

**Description:** Power setting

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:power`

**Unit:** W

</details>

<details>
<summary><strong>synthesis_duration</strong></summary>

**Description:** Duration of synthesis

**Range:** float

**Multivalued:** Yes

**URI:** `voc4cat:0000050`

**Unit:** h

</details>

<details>
<summary><strong>synthesis_temperature</strong></summary>

**Description:** Temperature during synthesis

**Range:** float

**Multivalued:** Yes

**URI:** `voc4cat:0000051`

**Unit:** Cel

</details>

<details>
<summary><strong>microwave_frequency</strong></summary>

**Description:** Frequency of microwave

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:microwave_frequency`

**Unit:** GHz

</details>

<details>
<summary><strong>vessel_type</strong></summary>

**Description:** Type of vessel used

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:vessel_type`

</details>

</details>

<details>
<summary>###### SonochemicalSynthesis</summary>

**Description:** Sonochemical synthesis method for catalyst preparation

**URI:** `catcore:SonochemicalSynthesis`

#### Slots (16)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>stirring_duration</strong></summary>

**Description:** Duration of stirring

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:stirring_duration`

**Unit:** h

</details>

<details>
<summary><strong>sonication_power</strong></summary>

**Description:** Power of sonication

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:sonication_power`

**Unit:** W

</details>

<details>
<summary><strong>sonication_duration</strong></summary>

**Description:** Duration of sonication

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:sonication_duration`

**Unit:** min

</details>

<details>
<summary><strong>temperature</strong></summary>

**Description:** Temperature

**Range:** float

**Multivalued:** Yes

**URI:** `AFR:0001584`

**Unit:** Cel

</details>

<details>
<summary><strong>drying_device</strong></summary>

**Description:** Device used for drying

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:drying_device`

</details>

<details>
<summary><strong>drying_temperature</strong></summary>

**Description:** Temperature during drying

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:drying_temperature`

**Unit:** Cel

</details>

<details>
<summary><strong>drying_time</strong></summary>

**Description:** Duration of drying process

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:drying_time`

**Unit:** h

</details>

<details>
<summary><strong>drying_atmosphere</strong></summary>

**Description:** Atmosphere during drying

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:drying_atmosphere`

</details>

<details>
<summary><strong>calcination_initial_temperature</strong></summary>

**Description:** Initial temperature for calcination

**Range:** float

**Multivalued:** Yes

**URI:** `voc4cat:0000057`

**Unit:** Cel

</details>

<details>
<summary><strong>calcination_final_temperature</strong></summary>

**Description:** Final temperature for calcination

**Range:** float

**Multivalued:** Yes

**URI:** `voc4cat:0000058`

**Unit:** Cel

</details>

<details>
<summary><strong>calcination_dwelling_time</strong></summary>

**Description:** Dwelling time at calcination temperature

**Range:** float

**Multivalued:** Yes

**URI:** `voc4cat:0000060`

**Unit:** h

</details>

<details>
<summary><strong>number_of_cycles</strong></summary>

**Description:** Number of cycles in the process

**Range:** integer

**Multivalued:** Yes

**URI:** `catcore:number_of_cycles`

</details>

<details>
<summary><strong>calcination_gaseous_environment</strong></summary>

**Description:** Gaseous environment during calcination

**Range:** string

**Multivalued:** Yes

**URI:** `voc4cat:0000055`

</details>

<details>
<summary><strong>calcination_heating_rate</strong></summary>

**Description:** Heating rate during calcination

**Range:** float

**Multivalued:** Yes

**URI:** `voc4cat:0000059`

**Unit:** Cel/min

</details>

<details>
<summary><strong>calcination_gas_flow_rate</strong></summary>

**Description:** Gas flow rate during calcination

**Range:** float

**Multivalued:** Yes

**URI:** `voc4cat:0000056`

**Unit:** mL/min

</details>

</details>

<details>
<summary>###### FlameSprayPyrolysis</summary>

**Description:** Flame spray pyrolysis method for catalyst preparation

**URI:** `voc4cat:0007031`

#### Slots (10)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>flame_type</strong></summary>

**Description:** Type of flame used

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:flame_type`

</details>

<details>
<summary><strong>flow_rate</strong></summary>

**Description:** Flow rate

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:flow_rate`

**Unit:** mL/min

</details>

<details>
<summary><strong>inlet_system</strong></summary>

**Description:** Inlet system configuration

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:inlet_system`

</details>

<details>
<summary><strong>flame_ring</strong></summary>

**Description:** Flame ring configuration

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:flame_ring`

</details>

<details>
<summary><strong>dispersant</strong></summary>

**Description:** Dispersant used

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:dispersant`

</details>

<details>
<summary><strong>capillary_pressure</strong></summary>

**Description:** Capillary pressure

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:capillary_pressure`

**Unit:** bar

</details>

<details>
<summary><strong>fuel_dispersant_ratio</strong></summary>

**Description:** Ratio of fuel to dispersant

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:fuel_dispersant_ratio`

</details>

<details>
<summary><strong>filtration_device</strong></summary>

**Description:** Device used for filtration

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:filtration_device`

</details>

<details>
<summary><strong>filter_type</strong></summary>

**Description:** Type of filter used

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:filter_type`

</details>

</details>

<details>
<summary>###### MechanochemicalSynthesis</summary>

**Description:** Mechanochemical synthesis method for catalyst preparation

**URI:** `catcore:MechanochemicalSynthesis`

#### Slots (11)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>equipment</strong></summary>

**Description:** Equipment used

**Range:** string

**Multivalued:** Yes

**URI:** `voc4cat:0000187`

</details>

<details>
<summary><strong>vessel_volume</strong></summary>

**Description:** Volume of vessel

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:vessel_volume`

**Unit:** mL

</details>

<details>
<summary><strong>size_and_material</strong></summary>

**Description:** Size and material of components

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:size_and_material`

</details>

<details>
<summary><strong>milling_speed</strong></summary>

**Description:** Speed of milling

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:milling_speed`

**Unit:** rpm

</details>

<details>
<summary><strong>milling_duration</strong></summary>

**Description:** Duration of milling

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:milling_duration`

**Unit:** h

</details>

<details>
<summary><strong>synthesis_temperature</strong></summary>

**Description:** Temperature during synthesis

**Range:** float

**Multivalued:** Yes

**URI:** `voc4cat:0000051`

**Unit:** Cel

</details>

<details>
<summary><strong>atmosphere</strong></summary>

**Description:** Atmospheric conditions

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:atmosphere`

</details>

<details>
<summary><strong>ball_material</strong></summary>

**Description:** Material of milling balls

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:ball_material`

</details>

<details>
<summary><strong>ball_size</strong></summary>

**Description:** Size of milling balls

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:ball_size`

**Unit:** mm

</details>

<details>
<summary><strong>ball_to_powder_ratio</strong></summary>

**Description:** Ratio of ball to powder

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:ball_to_powder_ratio`

</details>

</details>

<details>
<summary>###### Sublimation</summary>

**Description:** Sublimation method for catalyst preparation

**URI:** `catcore:Sublimation`

#### Slots (4)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>temperature</strong></summary>

**Description:** Temperature

**Range:** float

**Multivalued:** Yes

**URI:** `AFR:0001584`

**Unit:** Cel

</details>

<details>
<summary><strong>synthesis_pressure</strong></summary>

**Description:** Pressure during synthesis

**Range:** float

**Multivalued:** Yes

**URI:** `voc4cat:0000053`

**Unit:** bar

</details>

<details>
<summary><strong>synthesis_duration</strong></summary>

**Description:** Duration of synthesis

**Range:** float

**Multivalued:** Yes

**URI:** `voc4cat:0000050`

**Unit:** h

</details>

</details>

<details>
<summary>###### MolecularSynthesis</summary>

**Description:** Molecular synthesis method for catalyst preparation

**URI:** `catcore:MolecularSynthesis`

#### Slots (19)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>atmosphere</strong></summary>

**Description:** Atmospheric conditions

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:atmosphere`

</details>

<details>
<summary><strong>synthesis_duration</strong></summary>

**Description:** Duration of synthesis

**Range:** float

**Multivalued:** Yes

**URI:** `voc4cat:0000050`

**Unit:** h

</details>

<details>
<summary><strong>reaction_vessel</strong></summary>

**Description:** Vessel used for reaction

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:reaction_vessel`

</details>

<details>
<summary><strong>mixing_device</strong></summary>

**Description:** Device used for mixing

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:mixing_device`

</details>

<details>
<summary><strong>stirring_duration</strong></summary>

**Description:** Duration of stirring

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:stirring_duration`

**Unit:** h

</details>

<details>
<summary><strong>stirring_speed</strong></summary>

**Description:** Speed of stirring

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:stirring_speed`

**Unit:** rpm

</details>

<details>
<summary><strong>mixing_temperature</strong></summary>

**Description:** Temperature during mixing

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:mixing_temperature`

**Unit:** Cel

</details>

<details>
<summary><strong>filtration_device</strong></summary>

**Description:** Device used for filtration

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:filtration_device`

</details>

<details>
<summary><strong>filter_type</strong></summary>

**Description:** Type of filter used

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:filter_type`

</details>

<details>
<summary><strong>crystallisation_solvents</strong></summary>

**Description:** Solvents used for crystallisation

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:crystallisation_solvents`

</details>

<details>
<summary><strong>precipitation_agent</strong></summary>

**Description:** Agent used for precipitation

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:precipitation_agent`

</details>

<details>
<summary><strong>crystallisation_duration</strong></summary>

**Description:** Duration of crystallisation

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:crystallisation_duration`

**Unit:** h

</details>

<details>
<summary><strong>purification_solvent</strong></summary>

**Description:** Solvent used for purification

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:purification_solvent`

</details>

<details>
<summary><strong>number_of_cycles</strong></summary>

**Description:** Number of cycles in the process

**Range:** integer

**Multivalued:** Yes

**URI:** `catcore:number_of_cycles`

</details>

<details>
<summary><strong>drying_device</strong></summary>

**Description:** Device used for drying

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:drying_device`

</details>

<details>
<summary><strong>drying_temperature</strong></summary>

**Description:** Temperature during drying

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:drying_temperature`

**Unit:** Cel

</details>

<details>
<summary><strong>temperature_ramp</strong></summary>

**Description:** Temperature ramp rate

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:temperature_ramp`

**Unit:** Cel/min

</details>

<details>
<summary><strong>drying_time</strong></summary>

**Description:** Duration of drying process

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:drying_time`

**Unit:** h

</details>

</details>

<details>
<summary>###### ExsolutionSynthesis</summary>

**Description:** Exsolution synthesis method for catalyst preparation

**URI:** `catcore:ExsolutionSynthesis`

#### Slots (7)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>calcination_initial_temperature</strong></summary>

**Description:** Initial temperature for calcination

**Range:** float

**Multivalued:** Yes

**URI:** `voc4cat:0000057`

**Unit:** Cel

</details>

<details>
<summary><strong>calcination_final_temperature</strong></summary>

**Description:** Final temperature for calcination

**Range:** float

**Multivalued:** Yes

**URI:** `voc4cat:0000058`

**Unit:** Cel

</details>

<details>
<summary><strong>calcination_dwelling_time</strong></summary>

**Description:** Dwelling time at calcination temperature

**Range:** float

**Multivalued:** Yes

**URI:** `voc4cat:0000060`

**Unit:** h

</details>

<details>
<summary><strong>calcination_gaseous_environment</strong></summary>

**Description:** Gaseous environment during calcination

**Range:** string

**Multivalued:** Yes

**URI:** `voc4cat:0000055`

</details>

<details>
<summary><strong>calcination_heating_rate</strong></summary>

**Description:** Heating rate during calcination

**Range:** float

**Multivalued:** Yes

**URI:** `voc4cat:0000059`

**Unit:** Cel/min

</details>

<details>
<summary><strong>calcination_gas_flow_rate</strong></summary>

**Description:** Gas flow rate during calcination

**Range:** float

**Multivalued:** Yes

**URI:** `voc4cat:0000056`

**Unit:** mL/min

</details>

</details>

</details>

<details>
<summary><strong>Synthesis_storage_conditions</strong></summary>

**Description:** Conditions for storage

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:storage_conditions`

</details>

<details>
<summary><strong>support</strong></summary>

**Description:** Support material

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:support`

</details>

<details>
<summary><strong>solvent</strong></summary>

**Description:** Solvent used

**Range:** string

**Multivalued:** Yes

**URI:** `voc4cat:0007246`

</details>

<details>
<summary><strong>sample_pretreatment</strong></summary>

**Description:** Pre-treatment of sample

**Range:** string

**Multivalued:** Yes

**URI:** `voc4cat:0000122`

</details>

#### Slot Usage

- **nominal_composition**: Required
- **catalyst_measured_properties**: Required
- **precursor**: Required
- **preparation_method**: Required
- **storage_conditions**: Recommended

</details>

