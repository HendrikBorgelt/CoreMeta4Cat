# Characterization

**Description:** The data class 'Characterization' describes the minimum information which should be 
reported with research data to describe the nature of the catalyst.

---

## Main Class

<details>
<summary>### Characterization</summary>

**Description:** The data class 'Characterization' describes the minimum information which should be 
reported with research data to describe the nature of the catalyst.

**URI:** `catcore:Characterization`

#### Slots (8)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>Characterization_equipment</strong></summary>

**Description:** Equipment used

**Range:** string

**Multivalued:** Yes

**URI:** `voc4cat:0000187`

</details>

<details>
<summary><strong>Characterization_characterization_technique</strong></summary>

**Description:** Technique used for characterization

**Range:** CharacterizationTechnique

**Multivalued:** Yes

**URI:** `voc4cat:0000066`

**Range Class Details:**

<details>
<summary>##### CharacterizationTechnique</summary>

**Abstract Class**

**Description:** Characterization technique used for catalyst analysis

**URI:** `catcore:CharacterizationTechnique`

#### Slots (1)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

</details>

**Subclasses of CharacterizationTechnique:**

<details>
<summary>###### PowderXRD</summary>

**Description:** Powder X-ray diffraction

**URI:** `CHMO:0000158`

#### Slots (11)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>xray_source</strong></summary>

**Description:** X-ray source used

**Range:** string

**Multivalued:** Yes

**URI:** `OBI:0001138`

</details>

<details>
<summary><strong>atmosphere</strong></summary>

**Description:** Atmospheric conditions

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:atmosphere`

</details>

<details>
<summary><strong>operation_mode</strong></summary>

**Description:** Operation mode of the instrument

**Range:** string

**Multivalued:** Yes

**URI:** `voc4cat:0000108`

</details>

<details>
<summary><strong>minimum_2theta</strong></summary>

**Description:** Minimum 2-theta angle

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:minimum_2theta`

**Unit:** deg

</details>

<details>
<summary><strong>maximum_2theta</strong></summary>

**Description:** Maximum 2-theta angle

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:maximum_2theta`

**Unit:** deg

</details>

<details>
<summary><strong>step_size</strong></summary>

**Description:** Step size for measurements

**Range:** float

**Multivalued:** Yes

**URI:** `AFR:0000950`

</details>

<details>
<summary><strong>monochromator</strong></summary>

**Description:** Monochromator type used

**Range:** string

**Multivalued:** Yes

**URI:** `CHMO:0002120`

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
<summary><strong>sample_spinning_speed</strong></summary>

**Description:** Sample spinning speed

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:sample_spinning_speed`

**Unit:** rpm

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

<details>
<summary>###### XRayAbsorptionSpectroscopy</summary>

**Description:** X-ray absorption spectroscopy

**URI:** `voc4cat:0000286`

#### Slots (12)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>operation_mode</strong></summary>

**Description:** Operation mode of the instrument

**Range:** string

**Multivalued:** Yes

**URI:** `voc4cat:0000108`

</details>

<details>
<summary><strong>element_analyzed</strong></summary>

**Description:** Chemical element being analyzed

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:element_analyzed`

</details>

<details>
<summary><strong>absorption_edge</strong></summary>

**Description:** Absorption edge measured

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:absorption_edge`

</details>

<details>
<summary><strong>monochromator</strong></summary>

**Description:** Monochromator type used

**Range:** string

**Multivalued:** Yes

**URI:** `CHMO:0002120`

</details>

<details>
<summary><strong>minimum_energy</strong></summary>

**Description:** Minimum energy value

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:minimum_energy`

**Unit:** eV

</details>

<details>
<summary><strong>maximum_energy</strong></summary>

**Description:** Maximum energy value

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:maximum_energy`

**Unit:** eV

</details>

<details>
<summary><strong>energy_resolution</strong></summary>

**Description:** Energy resolution of the measurement

**Range:** float

**Multivalued:** Yes

**URI:** `AFR:0000950`

**Unit:** eV

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
<summary><strong>beamline_source</strong></summary>

**Description:** Beamline source identification

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:beamline_source`

</details>

<details>
<summary><strong>noise_of_measurement</strong></summary>

**Description:** Noise level of the measurement

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:noise_of_measurement`

</details>

<details>
<summary><strong>number_of_cycles</strong></summary>

**Description:** Number of cycles in the process

**Range:** integer

**Multivalued:** Yes

**URI:** `catcore:number_of_cycles`

</details>

</details>

<details>
<summary>###### InfraredSpectroscopy</summary>

**Description:** Infrared spectroscopy

**URI:** `catcore:InfraredSpectroscopy`

#### Slots (9)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>operation_mode</strong></summary>

**Description:** Operation mode of the instrument

**Range:** string

**Multivalued:** Yes

**URI:** `voc4cat:0000108`

</details>

<details>
<summary><strong>minimum_wavenumber</strong></summary>

**Description:** Minimum wavenumber

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:minimum_wavenumber`

**Unit:** cm-1

</details>

<details>
<summary><strong>maximum_wavenumber</strong></summary>

**Description:** Maximum wavenumber

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:maximum_wavenumber`

**Unit:** cm-1

</details>

<details>
<summary><strong>step_size</strong></summary>

**Description:** Step size for measurements

**Range:** float

**Multivalued:** Yes

**URI:** `AFR:0000950`

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
<summary><strong>background_correction</strong></summary>

**Description:** Background correction method

**Range:** string

**Multivalued:** Yes

**URI:** `AFP:0003721`

</details>

<details>
<summary><strong>number_of_scans</strong></summary>

**Description:** Number of scans performed

**Range:** integer

**Multivalued:** Yes

**URI:** `AFR:0003051`

</details>

<details>
<summary><strong>atmosphere</strong></summary>

**Description:** Atmospheric conditions

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:atmosphere`

</details>

</details>

<details>
<summary>###### RamanSpectroscopy</summary>

**Description:** Raman spectroscopy

**URI:** `voc4cat:0000069`

#### Slots (9)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>excitation_laser_wavelength</strong></summary>

**Description:** Excitation laser wavelength

**Range:** float

**Multivalued:** Yes

**URI:** `AFR:0001594`

**Unit:** nm

</details>

<details>
<summary><strong>excitation_laser_power</strong></summary>

**Description:** Excitation laser power

**Range:** float

**Multivalued:** Yes

**URI:** `AFR:0001595`

**Unit:** mW

</details>

<details>
<summary><strong>magnification_setting</strong></summary>

**Description:** Magnification setting

**Range:** float

**Multivalued:** Yes

**URI:** `AFR:0002226`

</details>

<details>
<summary><strong>integration_time</strong></summary>

**Description:** Integration time

**Range:** float

**Multivalued:** Yes

**URI:** `AFR:0001671`

**Unit:** s

</details>

<details>
<summary><strong>number_of_scans</strong></summary>

**Description:** Number of scans performed

**Range:** integer

**Multivalued:** Yes

**URI:** `AFR:0003051`

</details>

<details>
<summary><strong>atmosphere</strong></summary>

**Description:** Atmospheric conditions

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:atmosphere`

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
<summary><strong>filter_or_grating</strong></summary>

**Description:** Filter or grating used

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:filter_or_grating`

</details>

</details>

<details>
<summary>###### GCMS</summary>

**Description:** Gas chromatography-mass spectrometry

**URI:** `CHMO:0000497`

#### Slots (18)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>external_standard</strong></summary>

**Description:** External standard used for calibration

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:external_standard`

</details>

<details>
<summary><strong>internal_standard</strong></summary>

**Description:** Internal standard used for calibration

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:internal_standard`

</details>

<details>
<summary><strong>column_type</strong></summary>

**Description:** Type of chromatography column

**Range:** string

**Multivalued:** Yes

**URI:** `AFR:0002026`

</details>

<details>
<summary><strong>carrier_gas</strong></summary>

**Description:** Carrier gas used

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:carrier_gas`

</details>

<details>
<summary><strong>carrier_gas_purity</strong></summary>

**Description:** Purity of carrier gas

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:carrier_gas_purity`

</details>

<details>
<summary><strong>inlet_temperature</strong></summary>

**Description:** Inlet temperature

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:inlet_temperature`

**Unit:** Cel

</details>

<details>
<summary><strong>minimum_oven_temperature</strong></summary>

**Description:** Minimum oven temperature

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:minimum_oven_temperature`

**Unit:** Cel

</details>

<details>
<summary><strong>maximum_oven_temperature</strong></summary>

**Description:** Maximum oven temperature

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:maximum_oven_temperature`

**Unit:** Cel

</details>

<details>
<summary><strong>heating_ramp</strong></summary>

**Description:** Heating ramp rate

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:heating_ramp`

**Unit:** Cel/min

</details>

<details>
<summary><strong>heating_procedure</strong></summary>

**Description:** Heating procedure used

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:heating_procedure`

</details>

<details>
<summary><strong>acquisition_mode</strong></summary>

**Description:** Data acquisition mode

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:acquisition_mode`

</details>

<details>
<summary><strong>solvent_delay</strong></summary>

**Description:** Solvent delay time

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:solvent_delay`

**Unit:** min

</details>

<details>
<summary><strong>trace_ion_detection</strong></summary>

**Description:** Trace ion detection setting

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:trace_ion_detection`

</details>

<details>
<summary><strong>mz_minimum</strong></summary>

**Description:** Minimum m/z value

**Range:** float

**Multivalued:** Yes

**URI:** `AFR:0002652`

</details>

<details>
<summary><strong>mz_maximum</strong></summary>

**Description:** Maximum m/z value

**Range:** float

**Multivalued:** Yes

**URI:** `AFR:0002653`

</details>

<details>
<summary><strong>split_ratio</strong></summary>

**Description:** Split ratio for injection

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:split_ratio`

</details>

<details>
<summary><strong>injection_volume</strong></summary>

**Description:** Injection volume

**Range:** float

**Multivalued:** Yes

**URI:** `AFR:0001577`

**Unit:** uL

</details>

</details>

<details>
<summary>###### NMRSpectroscopy</summary>

**Description:** Nuclear magnetic resonance spectroscopy

**URI:** `voc4cat:0000073`

#### Slots (9)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>nucleus</strong></summary>

**Description:** Nucleus being observed

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:nucleus`

</details>

<details>
<summary><strong>solvent</strong></summary>

**Description:** Solvent used

**Range:** string

**Multivalued:** Yes

**URI:** `voc4cat:0007246`

</details>

<details>
<summary><strong>irradiation_frequency</strong></summary>

**Description:** Irradiation frequency

**Range:** float

**Multivalued:** Yes

**URI:** `nmrCV:1400026`

**Unit:** MHz

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
<summary><strong>nmr_pulse_sequence</strong></summary>

**Description:** NMR pulse sequence used

**Range:** string

**Multivalued:** Yes

**URI:** `nmrCV:1400037`

</details>

<details>
<summary><strong>nmr_sample_tube</strong></summary>

**Description:** NMR sample tube type

**Range:** string

**Multivalued:** Yes

**URI:** `nmrCV:1400132`

</details>

<details>
<summary><strong>number_of_scans</strong></summary>

**Description:** Number of scans performed

**Range:** integer

**Multivalued:** Yes

**URI:** `AFR:0003051`

</details>

<details>
<summary><strong>atmosphere</strong></summary>

**Description:** Atmospheric conditions

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:atmosphere`

</details>

</details>

<details>
<summary>###### TransmissionElectronMicroscopy</summary>

**Description:** Transmission electron microscopy

**URI:** `voc4cat:0000078`

#### Slots (5)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>operation_mode</strong></summary>

**Description:** Operation mode of the instrument

**Range:** string

**Multivalued:** Yes

**URI:** `voc4cat:0000108`

</details>

<details>
<summary><strong>gun_type</strong></summary>

**Description:** Type of electron gun

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:gun_type`

</details>

<details>
<summary><strong>acceleration_voltage</strong></summary>

**Description:** Acceleration voltage

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:acceleration_voltage`

**Unit:** kV

</details>

<details>
<summary><strong>magnification_setting</strong></summary>

**Description:** Magnification setting

**Range:** float

**Multivalued:** Yes

**URI:** `AFR:0002226`

</details>

</details>

<details>
<summary>###### ICPAES</summary>

**Description:** Inductively-coupled plasma atomic emission spectroscopy

**URI:** `CHMO:0000267`

#### Slots (5)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>element_analyzed</strong></summary>

**Description:** Chemical element being analyzed

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:element_analyzed`

</details>

<details>
<summary><strong>calibration_method</strong></summary>

**Description:** Calibration method used

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:calibration_method`

</details>

<details>
<summary><strong>detection_limit</strong></summary>

**Description:** Detection limit

**Range:** float

**Multivalued:** Yes

**URI:** `NCIT:C105701`

</details>

<details>
<summary><strong>matrix_effect_correction</strong></summary>

**Description:** Matrix effect correction method

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:matrix_effect_correction`

</details>

</details>

<details>
<summary>###### ScanningElectronMicroscopy</summary>

**Description:** Scanning electron microscopy

**URI:** `voc4cat:0000075`

#### Slots (5)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>gun_type</strong></summary>

**Description:** Type of electron gun

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:gun_type`

</details>

<details>
<summary><strong>acceleration_voltage</strong></summary>

**Description:** Acceleration voltage

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:acceleration_voltage`

**Unit:** kV

</details>

<details>
<summary><strong>image_resolution</strong></summary>

**Description:** Image resolution

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:image_resolution`

**Unit:** nm

</details>

<details>
<summary><strong>field_emitter</strong></summary>

**Description:** Field emitter type

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:field_emitter`

</details>

</details>

<details>
<summary>###### Thermogravimetry</summary>

**Description:** Thermogravimetry

**URI:** `CHMO:0000690`

#### Slots (8)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>operation_mode</strong></summary>

**Description:** Operation mode of the instrument

**Range:** string

**Multivalued:** Yes

**URI:** `voc4cat:0000108`

</details>

<details>
<summary><strong>atmosphere</strong></summary>

**Description:** Atmospheric conditions

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:atmosphere`

</details>

<details>
<summary><strong>initial_temperature</strong></summary>

**Description:** Initial temperature

**Range:** float

**Multivalued:** Yes

**URI:** `NCIT:C164644`

**Unit:** Cel

</details>

<details>
<summary><strong>final_temperature</strong></summary>

**Description:** Final temperature

**Range:** float

**Multivalued:** Yes

**URI:** `NCIT:C164644`

**Unit:** Cel

</details>

<details>
<summary><strong>heating_rate</strong></summary>

**Description:** Heating rate

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:heating_rate`

**Unit:** Cel/min

</details>

<details>
<summary><strong>heating_procedure</strong></summary>

**Description:** Heating procedure used

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:heating_procedure`

</details>

<details>
<summary><strong>sample_mass</strong></summary>

**Description:** Mass of sample

**Range:** float

**Multivalued:** Yes

**URI:** `voc4cat:0007038`

**Unit:** mg

</details>

</details>

<details>
<summary>###### XPS</summary>

**Description:** X-ray photoelectron spectroscopy

**URI:** `CHMO:0000404`

#### Slots (12)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>xray_source</strong></summary>

**Description:** X-ray source used

**Range:** string

**Multivalued:** Yes

**URI:** `OBI:0001138`

</details>

<details>
<summary><strong>total_acquisition_time</strong></summary>

**Description:** Total acquisition time

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:total_acquisition_time`

**Unit:** s

</details>

<details>
<summary><strong>number_of_scans</strong></summary>

**Description:** Number of scans performed

**Range:** integer

**Multivalued:** Yes

**URI:** `AFR:0003051`

</details>

<details>
<summary><strong>spot_size</strong></summary>

**Description:** Spot size for analysis

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:spot_size`

**Unit:** mm

</details>

<details>
<summary><strong>lense_mode</strong></summary>

**Description:** Lens mode setting

**Range:** string

**Multivalued:** Yes

**URI:** `voc4cat:0000108`

</details>

<details>
<summary><strong>minimum_energy</strong></summary>

**Description:** Minimum energy value

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:minimum_energy`

**Unit:** eV

</details>

<details>
<summary><strong>maximum_energy</strong></summary>

**Description:** Maximum energy value

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:maximum_energy`

**Unit:** eV

</details>

<details>
<summary><strong>step_size</strong></summary>

**Description:** Step size for measurements

**Range:** float

**Multivalued:** Yes

**URI:** `AFR:0000950`

</details>

<details>
<summary><strong>pass_energy</strong></summary>

**Description:** Pass energy setting

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:pass_energy`

**Unit:** eV

</details>

<details>
<summary><strong>charge_compensation</strong></summary>

**Description:** Charge compensation method

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:charge_compensation`

</details>

<details>
<summary><strong>atmosphere</strong></summary>

**Description:** Atmospheric conditions

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:atmosphere`

</details>

</details>

<details>
<summary>###### BET</summary>

**Description:** Brunauer-Emmett-Teller surface area analysis

**URI:** `catcore:BET`

#### Slots (6)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>adsorbate_gas</strong></summary>

**Description:** Adsorbate gas used

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:adsorbate_gas`

</details>

<details>
<summary><strong>degassing_temperature</strong></summary>

**Description:** Degassing temperature

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:degassing_temperature`

**Unit:** Cel

</details>

<details>
<summary><strong>measurement_temperature</strong></summary>

**Description:** Measurement temperature

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:measurement_temperature`

**Unit:** K

</details>

<details>
<summary><strong>pore_size_distribution_method</strong></summary>

**Description:** Method for pore size distribution analysis

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:pore_size_distribution_method`

</details>

<details>
<summary><strong>sample_mass</strong></summary>

**Description:** Mass of sample

**Range:** float

**Multivalued:** Yes

**URI:** `voc4cat:0007038`

**Unit:** mg

</details>

</details>

<details>
<summary>###### ElementalAnalysis</summary>

**Description:** Elemental analysis

**URI:** `CHMO:0001075`

#### Slots (4)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>elements_analyzed</strong></summary>

**Description:** Elements analyzed

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:elements_analyzed`

</details>

<details>
<summary><strong>combustion_temperature</strong></summary>

**Description:** Combustion temperature

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:combustion_temperature`

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
<summary>###### UVVisSpectroscopy</summary>

**Description:** Ultraviolet-visible spectroscopy

**URI:** `voc4cat:0000079`

#### Slots (6)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>minimum_wavelength</strong></summary>

**Description:** Minimum wavelength

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:minimum_wavelength`

**Unit:** nm

</details>

<details>
<summary><strong>maximum_wavelength</strong></summary>

**Description:** Maximum wavelength

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:maximum_wavelength`

**Unit:** nm

</details>

<details>
<summary><strong>path_length</strong></summary>

**Description:** Path length of cell

**Range:** float

**Multivalued:** Yes

**URI:** `AFQ:0000268`

**Unit:** cm

</details>

<details>
<summary><strong>solvent</strong></summary>

**Description:** Solvent used

**Range:** string

**Multivalued:** Yes

**URI:** `voc4cat:0007246`

</details>

<details>
<summary><strong>concentration</strong></summary>

**Description:** Concentration of sample

**Range:** float

**Multivalued:** Yes

**URI:** `voc4cat:0007244`

**Unit:** mol/L

</details>

</details>

<details>
<summary>###### DRIFTS</summary>

**Description:** Diffuse reflectance infrared Fourier transform spectroscopy

**URI:** `CHMO:0000645`

#### Slots (11)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>adsorption_gas</strong></summary>

**Description:** Adsorption gas used

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:adsorption_gas`

</details>

<details>
<summary><strong>atmosphere</strong></summary>

**Description:** Atmospheric conditions

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:atmosphere`

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
<summary><strong>diluting_reference</strong></summary>

**Description:** Diluting reference material

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:diluting_reference`

</details>

<details>
<summary><strong>ratio_reference_sample</strong></summary>

**Description:** Ratio of reference to sample

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:ratio_reference_sample`

</details>

<details>
<summary><strong>step_size</strong></summary>

**Description:** Step size for measurements

**Range:** float

**Multivalued:** Yes

**URI:** `AFR:0000950`

</details>

<details>
<summary><strong>resolution</strong></summary>

**Description:** Spectral resolution

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:resolution`

**Unit:** cm-1

</details>

<details>
<summary><strong>background_correction_method</strong></summary>

**Description:** Background correction method used

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:background_correction_method`

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
<summary><strong>number_of_scans</strong></summary>

**Description:** Number of scans performed

**Range:** integer

**Multivalued:** Yes

**URI:** `AFR:0003051`

</details>

</details>

<details>
<summary>###### CyclicVoltammetry</summary>

**Description:** Cyclic voltammetry

**URI:** `CHMO:0000025`

#### Slots (13)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>scan_rate</strong></summary>

**Description:** Scan rate for voltammetry

**Range:** float

**Multivalued:** Yes

**URI:** `voc4cat:0007213`

**Unit:** mV/s

</details>

<details>
<summary><strong>minimum_potential</strong></summary>

**Description:** Minimum potential

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:minimum_potential`

**Unit:** V

</details>

<details>
<summary><strong>maximum_potential</strong></summary>

**Description:** Maximum potential

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:maximum_potential`

**Unit:** V

</details>

<details>
<summary><strong>step_size_potential</strong></summary>

**Description:** Step size for potential

**Range:** float

**Multivalued:** Yes

**URI:** `voc4cat:0007218`

**Unit:** mV

</details>

<details>
<summary><strong>electrolyte_composition</strong></summary>

**Description:** Composition of electrolyte

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:electrolyte_composition`

</details>

<details>
<summary><strong>electrolyte_concentration</strong></summary>

**Description:** Concentration of electrolyte

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:electrolyte_concentration`

**Unit:** mol/L

</details>

<details>
<summary><strong>reference_electrode</strong></summary>

**Description:** Reference electrode used

**Range:** string

**Multivalued:** Yes

**URI:** `voc4cat:0007204`

</details>

<details>
<summary><strong>number_of_cycles</strong></summary>

**Description:** Number of cycles in the process

**Range:** integer

**Multivalued:** Yes

**URI:** `catcore:number_of_cycles`

</details>

<details>
<summary><strong>working_electrode</strong></summary>

**Description:** Working electrode used

**Range:** string

**Multivalued:** Yes

**URI:** `voc4cat:0007202`

</details>

<details>
<summary><strong>counter_electrode</strong></summary>

**Description:** Counter electrode used

**Range:** string

**Multivalued:** Yes

**URI:** `voc4cat:0007203`

</details>

<details>
<summary><strong>atmosphere</strong></summary>

**Description:** Atmospheric conditions

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:atmosphere`

</details>

<details>
<summary><strong>temperature</strong></summary>

**Description:** Temperature

**Range:** float

**Multivalued:** Yes

**URI:** `AFR:0001584`

**Unit:** Cel

</details>

</details>

<details>
<summary>###### DynamicLightScattering</summary>

**Description:** Dynamic light scattering

**URI:** `CHMO:0000167`

#### Slots (9)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>solvent</strong></summary>

**Description:** Solvent used

**Range:** string

**Multivalued:** Yes

**URI:** `voc4cat:0007246`

</details>

<details>
<summary><strong>concentration</strong></summary>

**Description:** Concentration of sample

**Range:** float

**Multivalued:** Yes

**URI:** `voc4cat:0007244`

**Unit:** mol/L

</details>

<details>
<summary><strong>light_wavelength</strong></summary>

**Description:** Light wavelength used

**Range:** float

**Multivalued:** Yes

**URI:** `voc4cat:0000176`

**Unit:** nm

</details>

<details>
<summary><strong>scattering_angle</strong></summary>

**Description:** Scattering angle

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:scattering_angle`

**Unit:** deg

</details>

<details>
<summary><strong>refractive_index</strong></summary>

**Description:** Refractive index

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:refractive_index`

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
<summary><strong>dispersant</strong></summary>

**Description:** Dispersant used

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:dispersant`

</details>

<details>
<summary><strong>measurement_duration</strong></summary>

**Description:** Duration of measurement

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:measurement_duration`

**Unit:** s

</details>

</details>

<details>
<summary>###### ESI_MS</summary>

**Description:** Electrospray ionisation mass spectrometry

**URI:** `CHMO:0000482`

#### Slots (10)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>operation_mode</strong></summary>

**Description:** Operation mode of the instrument

**Range:** string

**Multivalued:** Yes

**URI:** `voc4cat:0000108`

</details>

<details>
<summary><strong>mz_minimum</strong></summary>

**Description:** Minimum m/z value

**Range:** float

**Multivalued:** Yes

**URI:** `AFR:0002652`

</details>

<details>
<summary><strong>mz_maximum</strong></summary>

**Description:** Maximum m/z value

**Range:** float

**Multivalued:** Yes

**URI:** `AFR:0002653`

</details>

<details>
<summary><strong>spray_voltage</strong></summary>

**Description:** Spray voltage for ionization

**Range:** float

**Multivalued:** Yes

**URI:** `CHMO:0002792`

**Unit:** kV

</details>

<details>
<summary><strong>capillary_temperature</strong></summary>

**Description:** Capillary temperature

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:capillary_temperature`

**Unit:** Cel

</details>

<details>
<summary><strong>solvent_composition</strong></summary>

**Description:** Solvent composition

**Range:** string

**Multivalued:** Yes

**URI:** `voc4cat:0007246`

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
<summary><strong>carrier_gas</strong></summary>

**Description:** Carrier gas used

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:carrier_gas`

</details>

<details>
<summary><strong>concentration</strong></summary>

**Description:** Concentration of sample

**Range:** float

**Multivalued:** Yes

**URI:** `voc4cat:0007244`

**Unit:** mol/L

</details>

</details>

<details>
<summary>###### PhotoluminescenceSpectroscopy</summary>

**Description:** Photoluminescence spectroscopy

**URI:** `catcore:PhotoluminescenceSpectroscopy`

#### Slots (9)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>excitation_wavelength</strong></summary>

**Description:** Excitation wavelength

**Range:** float

**Multivalued:** Yes

**URI:** `AFR:0002479`

**Unit:** nm

</details>

<details>
<summary><strong>emission_wavelength</strong></summary>

**Description:** Emission wavelength

**Range:** float

**Multivalued:** Yes

**URI:** `NCIT:C204101`

**Unit:** nm

</details>

<details>
<summary><strong>optical_filter</strong></summary>

**Description:** Optical filter used

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:optical_filter`

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
<summary><strong>emission_range</strong></summary>

**Description:** Emission range measured

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:emission_range`

</details>

<details>
<summary><strong>slit_width</strong></summary>

**Description:** Slit width setting

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:slit_width`

**Unit:** nm

</details>

<details>
<summary><strong>step_size</strong></summary>

**Description:** Step size for measurements

**Range:** float

**Multivalued:** Yes

**URI:** `AFR:0000950`

</details>

<details>
<summary><strong>integration_time</strong></summary>

**Description:** Integration time

**Range:** float

**Multivalued:** Yes

**URI:** `AFR:0001671`

**Unit:** s

</details>

</details>

<details>
<summary>###### PhotoluminescenceLifetime</summary>

**Description:** Photoluminescence lifetime measurement

**URI:** `catcore:PhotoluminescenceLifetime`

#### Slots (7)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>excitation_wavelength</strong></summary>

**Description:** Excitation wavelength

**Range:** float

**Multivalued:** Yes

**URI:** `AFR:0002479`

**Unit:** nm

</details>

<details>
<summary><strong>emission_wavelength</strong></summary>

**Description:** Emission wavelength

**Range:** float

**Multivalued:** Yes

**URI:** `NCIT:C204101`

**Unit:** nm

</details>

<details>
<summary><strong>optical_filter</strong></summary>

**Description:** Optical filter used

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:optical_filter`

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
<summary><strong>lifetime_fitting_model</strong></summary>

**Description:** Lifetime fitting model used

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:lifetime_fitting_model`

</details>

<details>
<summary><strong>number_of_shots</strong></summary>

**Description:** Number of shots for measurement

**Range:** integer

**Multivalued:** Yes

**URI:** `catcore:number_of_shots`

</details>

</details>

<details>
<summary>###### SizeExclusionChromatography</summary>

**Description:** Size-exclusion chromatography

**URI:** `AFP:0000843`

#### Slots (7)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>column_type</strong></summary>

**Description:** Type of chromatography column

**Range:** string

**Multivalued:** Yes

**URI:** `AFR:0002026`

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
<summary><strong>eluent</strong></summary>

**Description:** Eluent used

**Range:** string

**Multivalued:** Yes

**URI:** `AFRL:0000011`

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
<summary><strong>calibration_standard</strong></summary>

**Description:** Calibration standard used

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:calibration_standard`

</details>

<details>
<summary><strong>injection_volume</strong></summary>

**Description:** Injection volume

**Range:** float

**Multivalued:** Yes

**URI:** `AFR:0001577`

**Unit:** uL

</details>

</details>

<details>
<summary>###### HPLC_MS</summary>

**Description:** High-performance liquid chromatography mass spectrometry

**URI:** `CHMO:0000796`

#### Slots (10)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>column_type</strong></summary>

**Description:** Type of chromatography column

**Range:** string

**Multivalued:** Yes

**URI:** `AFR:0002026`

</details>

<details>
<summary><strong>eluent</strong></summary>

**Description:** Eluent used

**Range:** string

**Multivalued:** Yes

**URI:** `AFRL:0000011`

</details>

<details>
<summary><strong>gradient_program</strong></summary>

**Description:** Gradient program for elution

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:gradient_program`

</details>

<details>
<summary><strong>ionization_mode</strong></summary>

**Description:** Ionization mode used

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:ionization_mode`

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
<summary><strong>flow_rate</strong></summary>

**Description:** Flow rate

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:flow_rate`

**Unit:** mL/min

</details>

<details>
<summary><strong>injection_volume</strong></summary>

**Description:** Injection volume

**Range:** float

**Multivalued:** Yes

**URI:** `AFR:0001577`

**Unit:** uL

</details>

<details>
<summary><strong>external_standard</strong></summary>

**Description:** External standard used for calibration

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:external_standard`

</details>

<details>
<summary><strong>internal_standard</strong></summary>

**Description:** Internal standard used for calibration

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:internal_standard`

</details>

</details>

<details>
<summary>###### SingleCrystalXRD</summary>

**Description:** Single crystal X-ray diffraction

**URI:** `CHMO:0000852`

#### Slots (3)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>xray_source</strong></summary>

**Description:** X-ray source used

**Range:** string

**Multivalued:** Yes

**URI:** `OBI:0001138`

</details>

<details>
<summary><strong>temperature</strong></summary>

**Description:** Temperature

**Range:** float

**Multivalued:** Yes

**URI:** `AFR:0001584`

**Unit:** Cel

</details>

</details>

<details>
<summary>###### EDX</summary>

**Description:** Energy-dispersive X-ray emission spectroscopy

**URI:** `CHMO:0000309`

#### Slots (5)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>primary_energy</strong></summary>

**Description:** Primary energy of electron beam

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:primary_energy`

**Unit:** keV

</details>

<details>
<summary><strong>counting_time</strong></summary>

**Description:** Counting time for detection

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:counting_time`

**Unit:** s

</details>

<details>
<summary><strong>resolution</strong></summary>

**Description:** Spectral resolution

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:resolution`

**Unit:** cm-1

</details>

<details>
<summary><strong>calibration_method</strong></summary>

**Description:** Calibration method used

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:calibration_method`

</details>

</details>

<details>
<summary>###### TPO</summary>

**Description:** Temperature-programmed oxidation

**URI:** `CHMO:0002907`

#### Slots (5)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>oxidizing_gas_composition</strong></summary>

**Description:** Composition of oxidizing gas

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:oxidizing_gas_composition`

</details>

<details>
<summary><strong>heating_rate</strong></summary>

**Description:** Heating rate

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:heating_rate`

**Unit:** Cel/min

</details>

<details>
<summary><strong>minimum_temperature</strong></summary>

**Description:** Minimum temperature

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:minimum_temperature`

**Unit:** Cel

</details>

<details>
<summary><strong>maximum_temperature</strong></summary>

**Description:** Maximum temperature

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:maximum_temperature`

**Unit:** Cel

</details>

</details>

<details>
<summary>###### TPR</summary>

**Description:** Temperature-programmed reduction

**URI:** `CHMO:0002908`

#### Slots (5)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>reducing_gas_composition</strong></summary>

**Description:** Composition of reducing gas

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:reducing_gas_composition`

</details>

<details>
<summary><strong>heating_rate</strong></summary>

**Description:** Heating rate

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:heating_rate`

**Unit:** Cel/min

</details>

<details>
<summary><strong>minimum_temperature</strong></summary>

**Description:** Minimum temperature

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:minimum_temperature`

**Unit:** Cel

</details>

<details>
<summary><strong>maximum_temperature</strong></summary>

**Description:** Maximum temperature

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:maximum_temperature`

**Unit:** Cel

</details>

</details>

<details>
<summary>###### ConductivityMeasurement</summary>

**Description:** Conductivity measurement

**URI:** `catcore:ConductivityMeasurement`

#### Slots (6)

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
<summary><strong>electrode_configuration</strong></summary>

**Description:** Configuration of electrodes

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:electrode_configuration`

</details>

<details>
<summary><strong>frequency</strong></summary>

**Description:** Frequency of measurement

**Range:** float

**Multivalued:** Yes

**URI:** `voc4cat:0007239`

**Unit:** Hz

</details>

<details>
<summary><strong>ac_dc_mode</strong></summary>

**Description:** AC or DC measurement mode

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:ac_dc_mode`

</details>

<details>
<summary><strong>sample_geometry</strong></summary>

**Description:** Geometry of the sample

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:sample_geometry`

</details>

</details>

</details>

<details>
<summary><strong>sample_state</strong></summary>

**Description:** State of the sample

**Range:** SampleStateEnum

**Multivalued:** Yes

**URI:** `catcore:sample_state`

</details>

<details>
<summary><strong>sample_description</strong></summary>

**Description:** Description of the sample

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:sample_description`

</details>

<details>
<summary><strong>detector_type</strong></summary>

**Description:** Type of detector used

**Range:** string

**Multivalued:** Yes

**URI:** `AFR:0000317`

</details>

<details>
<summary><strong>sample_preparation</strong></summary>

**Description:** Preparation of sample

**Range:** string

**Multivalued:** Yes

**URI:** `AFP:0001159`

</details>

<details>
<summary><strong>sample_pretreatment</strong></summary>

**Description:** Pre-treatment of sample

**Range:** string

**Multivalued:** Yes

**URI:** `voc4cat:0000122`

</details>

#### Slot Usage

- **equipment**: Required
- **characterization_technique**: Required

</details>

